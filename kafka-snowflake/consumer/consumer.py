import json
import logging
import pandas as pd
from kafka import KafkaConsumer
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from transformations import clean_data

# Load configuration from JSON file
def load_config(config_file="config.json"):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Set up logging
def setup_logging(config):
    log_file = config['logging']['consumer_log_file']
    log_level = getattr(logging, config['logging']['log_level'].upper(), logging.INFO)

    # Ensure logs directory exists
    import os
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Add console logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

# Connect to Snowflake
def connect_snowflake(config):
    try:
        snowflake_config = config["snowflake"]
        conn = snowflake.connector.connect(
            user=snowflake_config["user"],
            password=snowflake_config["password"],
            account=snowflake_config["account"],
            warehouse=snowflake_config["warehouse"],
            database=snowflake_config["database"],
            schema=snowflake_config["schema"]
        )
        logging.info("Successfully connected to Snowflake.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to Snowflake: {e}")
        raise

# Consume Kafka messages and insert into Snowflake using write_pandas
def consume_kafka():
    config = load_config()  # Load config
    setup_logging(config)   # Setup logging
    conn = connect_snowflake(config)  # Connect to Snowflake

    topic = config['kafka']['topic']
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=config['kafka']['bootstrap_servers'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    logging.info(f"Connected to Kafka topic: {topic}")

    batch_data = []  # Store messages for batch insertion

    for message in consumer:
      try:
          raw_data = message.value
          batch_data.append(raw_data)

        # Process and insert data in batches of 10
          if len(batch_data) >= 10:
            df = pd.DataFrame(batch_data)
            cleaned_df = clean_data(df)  # ✅ Clean data here

            logging.info(f"🔥 Cleaned Data Before Insert:\n{cleaned_df}")  # ✅ Log cleaned data

            # Bulk insert into Snowflake
            cleaned_df.reset_index(drop=True, inplace=True)  # Reset index before writing
            success, num_rows, _ = write_pandas(conn, cleaned_df, "YOUR_TABLE", auto_create_table=True) #give ur own snowflake table name
            logging.info(f"✅ Inserted {num_rows} rows into Snowflake successfully.")

            batch_data.clear()  # Reset batch

      except Exception as e:
         logging.error(f"❌ Error processing message: {e}")

    conn.close()
    logging.info("Kafka consumer stopped.")

# Run the consumer
if __name__ == '__main__':
    consume_kafka()

