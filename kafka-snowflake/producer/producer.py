import json
import logging
from kafka import KafkaProducer
from faker import Faker
import time
import os
import random

# Load configuration from a JSON file
def load_config(config_file="config.json"):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Set up logging using values from the config file
def setup_logging(config):
    log_file = config['logging']['log_file']
    log_level = getattr(logging, config['logging']['log_level'].upper(), logging.INFO)

    # Ensure logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Create a logger
    logging.basicConfig(filename=log_file, level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Adding console logging too
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

def create_producer(config):
    producer = KafkaProducer(
        bootstrap_servers=config['kafka']['bootstrap_servers'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

# Function to generate messy data
def generate_messy_data():
    fake = Faker()
    data = {
        "id": random.randint(1000, 9999),
        "name": fake.name(),
        "age": random.randint(18, 80),
        "city": fake.city(),
        "email": fake.email(),
        "address": fake.address().replace("\n", " "),
        "phone_number": fake.phone_number(),
        "random_field": random.choice([None, fake.text(), "", random.randint(100000, 999999)]),
        "special_chars": ''.join(random.choices("!@#$%^&*()<>", k=5)),
        "date": fake.date_this_decade().strftime('%Y-%m-%d'),  # Convert date to string in 'YYYY-MM-DD' format
        "time": fake.time(),
        "invalid_data": random.choice([None, "N/A", "invalid", "", 0, -1]),
        "zipcode": random.randint(10000, 99999),
    }
    return data


# Send data to Kafka
def send_data_to_kafka(producer, config):
    topic = config['kafka']['topic']
    try:
        while True:
            message = generate_messy_data()

            logging.info(f"Sending message to Kafka topic {topic}: {message}")

            producer.send(topic, value=message)

            logging.info(f"Message sent to topic {topic}")

            time.sleep(2)
    except Exception as e:
        logging.error(f"Error sending data to Kafka: {e}")
    finally:
        producer.close()

# Main execution
if __name__ == '__main__':
    config = load_config()  # Load the config
    setup_logging(config)    # Set up logging
    producer = create_producer(config)  # Create the Kafka producer
    send_data_to_kafka(producer, config)  # Send data to Kafka
