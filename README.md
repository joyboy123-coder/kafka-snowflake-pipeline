# 📌 Kafka to Snowflake Streaming Pipeline  

## 🚀 Overview  
This project builds a **real-time data pipeline** that streams data from **Kafka**, processes it, and stores it in **Snowflake**.  

- **Producer** → Generates and sends data to Kafka.  
- **Consumer** → Reads, processes, and inserts data into Snowflake.  
- **Transformations** → Cleans and formats the data.  
- **Configuration** → Manages Kafka, Snowflake, and logging settings.  

---

## 📂 Project Structure (Follow in Order)  

```
📦 Kafka-Snowflake-Pipeline
│-- 📂 requirements    # Dependencies & Setup Instructions (Start Here)
│-- 📄 config.json     # Configuration File (Kafka, Snowflake, Logging)
│-- 📂 producer        # Kafka Producer - Generates & Sends Data
│-- 📂 transformations # Data Cleaning & Processing
│-- 📂 consumer        # Kafka Consumer - Reads & Inserts Data
│-- 📄 README.md       # Project Documentation (You are here!)
```

---

## 🔹 1️⃣ Install Dependencies → `requirements/`  
- This folder contains the required **Python libraries**.  
- Before running the project, install them using:  
  ```bash
  pip install -r requirements.txt
  ```

---

## 🔹 2️⃣ Configure the Pipeline → `config.json`  
- Contains **Kafka, Snowflake, and Logging** settings.  
- **Modify credentials** before running.  

---

## 🔹 3️⃣ Start Kafka Producer → `producer/producer.py`  
- Generates **random mock data**.  
- Sends it to **Kafka in real time**.  
- **Run this first before the consumer!**  
  ```bash
  python producer/producer.py
  ```

---

## 🔹 4️⃣ Handle Data Cleaning → `transformations/transformations.py`  
- Cleans null values, special characters, and incorrect formats.  
- Standardizes **email, date, and numeric formats**.  
- This file is **automatically used by the consumer**, so no need to run it manually!  

---

## 🔹 5️⃣ Start Kafka Consumer → `consumer/consumer.py`  
- Reads messages from Kafka.  
- Cleans & formats the data using **transformations**.  
- Inserts the data into **Snowflake** in batches.  
  ```bash
  python consumer/consumer.py
  ```

---

## 🛑 How to Stop the Pipeline  

1. **Stop the Producer** → Press `CTRL + C` in the terminal.  
2. **Stop the Consumer** → Press `CTRL + C` in the terminal.  
3. **Stop Kafka** → Run:  
   ```bash
   kafka-server-stop.sh
   ```
4. **Stop Zookeeper** → Run:  
   ```bash
   zookeeper-server-stop.sh
   ```
5. **If everything is still running, close VS Code** → This force-stops all processes.  

---

## 🎯 Next Steps  
✅ **Test with real-time data sources** (APIs, logs, IoT).  
✅ **Improve error handling** to handle failed inserts.  
✅ **Optimize performance** by increasing batch sizes.  
✅ **Automate deployment** using Docker/Kubernetes.  

---
