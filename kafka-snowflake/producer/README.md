# Kafka Producer Data Flow

## Overview  
A Kafka producer that generates and sends messy data to a Kafka topic, logging each message.

---

## 📁 Project Structure  
/project-folder │── config.json # Kafka & logging configurations
│── producer.py # Kafka producer script
│── logs/ # Log storage directory
│ ├── producer.log # Log file (generated during execution)

yaml
Copy
Edit

---

## ⚙️ Configuration (config.json)  
```json
{
  "kafka": {
    "bootstrap_servers": "localhost:9092",
    "topic": "your_topic_name",
    "group_id": "your_consumer_group"
  },
  "logging": {
    "log_file": "logs/producer.log",
    "log_level": "INFO"
  }
}
🔄 Data Flow
1️⃣ Producer generates messy data using Faker
2️⃣ Kafka receives data from the producer
3️⃣ Log File stores sent messages

Step	Component	Description
1️⃣	producer.py	Generates and sends data to Kafka
2️⃣	Kafka	Stores incoming messages
3️⃣	logs/producer.log	Tracks sent messages
📜 Sample Log Output
plaintext
Copy
Edit
2025-03-21 12:00:01 - INFO - Sending message to Kafka topic your_topic_name: {"id": 1234, "name": "John Doe", "age": 29, ...}
2025-03-21 12:00:03 - INFO - Message sent to topic your_topic_name
🚀 Running the Producer
bash
Copy
Edit
python producer.py

