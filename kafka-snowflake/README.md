## 🔹 Overview  

## 🔹 1️⃣ Setup Configuration → `config.json`  
- **This file is required for everything to work.**  
- It contains **Kafka, Snowflake, and logging settings**.  
- You **must update your credentials** before running.  

---

## 🔹 2️⃣ Run Kafka Producer → `producer/producer.py`  
The producer:  
✅ Reads **config.json** to get Kafka details.  
✅ Generates **random mock data**.  
✅ Sends data **every 2 seconds** to the Kafka topic.  

Run it first before starting the consumer:  
```bash
python producer/producer.py
```

---

## 🔹 3️⃣ Data Cleaning with Transformations → `transformations/transformations.py`  
✅ We **don’t run this manually**.  
✅ The **consumer automatically imports it** when processing messages.  
✅ It **cleans** incorrect emails, dates, and null values before inserting into Snowflake.  

---

## 🔹 4️⃣ Run Kafka Consumer → `consumer/consumer.py`  
The consumer:  
✅ Reads **config.json** for Kafka & Snowflake credentials.  
✅ Listens for messages from **Kafka**.  
✅ **Uses `transformations.py`** to clean data.  
✅ Inserts cleaned data into **Snowflake** in batches.  

Run it after the producer is sending data:  
```bash
python consumer/consumer.py
```

---

## 🔄 How Everything Connects  

1️⃣ **Producer (`producer.py`)** gets Kafka details from **config.json**.  
2️⃣ It generates **mock data** and sends it to Kafka.  
3️⃣ **Consumer (`consumer.py`)** reads from Kafka using **config.json**.  
4️⃣ Consumer **calls `transformations.py`** to clean the data.  
5️⃣ Cleaned data is **inserted into Snowflake** using `write_pandas()`.  

---

