# 🚀 Kafka Producer Data Flow

## 📌 Overview
This project demonstrates how a **Kafka Producer** generates and sends data to a Kafka topic. The logs track each message sent.

## 🔄 Data Flow Process

### 1️⃣ Load Configuration (`config.json`)  
📂 Reads Kafka and logging settings from `config.json`.  
🛠️ Stores Kafka details like `bootstrap_servers` and log file settings.  

### 2️⃣ Set Up Logging  
📜 Logging is configured based on `config.json`.  
📝 Creates a **log file** to store Kafka producer messages.  
📌 Logs messages both in the `.log` file and in the **terminal**.  

### 3️⃣ Create Kafka Producer (`producer.py`)  
🔧 Initializes a Kafka producer with **JSON serialization**.  
🔗 Reads Kafka broker details from `config.json`.  

### 4️⃣ Generate Messy Data  
🎲 Uses the **Faker** library to create **realistic but messy data**.  
📦 Includes:
- 🧑‍💻 Names, emails, phone numbers, and addresses.
- 🔀 Random special characters, invalid data, and missing values.  

### 5️⃣ Send Messages to Kafka  
📤 Data is **serialized as JSON** and sent to the Kafka topic.  
📌 Each sent message is **logged** in the `.log` file.  

---

## 🔥 Expected Data Flow

| 🔢 Step | 🏗️ Action  | 📋 Description                  |
|---------|------------|--------------------------------|
| 1️⃣    | 🎭 Producer  | Generates messy data using Faker |
| 2️⃣    | 🔗 Kafka     | Receives data from the producer |
| 3️⃣    | 📜 Log File  | Stores information about messages |

---

## 🛠️ Requirements
✅ **Python 3.x**  
✅ **Kafka Installed**  
✅ **Required Libraries:**  
```sh
pip install kafka-python faker
