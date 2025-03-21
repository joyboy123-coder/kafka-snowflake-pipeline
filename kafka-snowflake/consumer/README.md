# 📌 Kafka Consumer to Snowflake Pipeline  

## 🔍 Overview  
This project is designed to **consume real-time data** from a **Kafka topic**, process and clean the data, and then **insert it into Snowflake** in batches. The pipeline ensures **efficient data processing, logging, and fault tolerance** while handling streaming data.  

---

## 🏗️ How It Works  

### 1️⃣ **Connecting to Kafka**  
The consumer connects to **Kafka** using the broker details provided in `config.json`.  
- It listens for incoming **JSON messages** from a specific **Kafka topic**.  
- Messages are **deserialized** (converted from raw Kafka format into a usable JSON object).  

### 2️⃣ **Batch Processing**  
- Instead of inserting each message one by one (which is inefficient), the script **collects 10 messages at a time**.  
- Once the batch reaches **10 records**, it processes the data in one go, reducing **database write overhead**.  

### 3️⃣ **Using `transformations.py` for Data Cleaning**  
- Raw messages from Kafka often contain **missing values, incorrect formats, or unwanted characters**.  
- Instead of writing all cleaning logic inside the main script, we use a separate module: **`transformations.py`**.  
- This function **`clean_data(df)`** is imported from `transformations.py` and is responsible for:  
  - **Removing null values**  
  - **Standardizing date formats**  
  - **Fixing incorrect data types**  
  - **Handling missing fields**  

By keeping data transformation logic in a separate file (`transformations.py`), the code becomes **modular and reusable**. If we need to modify the cleaning process, we update **only `transformations.py`** instead of touching the main consumer script.  

### 4️⃣ **Inserting Data into Snowflake**  
- After cleaning, the data is **bulk inserted** into Snowflake using `write_pandas()`.  
- This is **much faster** than inserting records one by one.  
- The table in Snowflake is named **dynamically**, which means you can replace `"YOUR_TABLE"` in the script with your desired table name.  

### 5️⃣ **Logging and Error Handling**  
- Every important step (Kafka connection, data processing, Snowflake insertion) is logged in a **log file** for debugging.  
- If an error occurs (e.g., connection failure, invalid data), it is logged, and the script **continues running** instead of stopping.  

---

## 🔧 Configuration (`config.json`)  
The script does not store sensitive information directly in the code. Instead, we load it from `config.json`, which contains:  
- **Kafka details** (broker, topic name)  
- **Snowflake credentials** (username, password, account details)  
- **Logging file path and level**  

By using a config file, it becomes **easier to change settings** without modifying the script.  

---

## 🚀 Running the Consumer  

### ✅ **Step 1: Install Dependencies**  
Run this in terminal (CMD):
```bash
python consumer.py