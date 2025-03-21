# 📌 Project Dependencies  

Below are the key libraries used in this project and their purposes:  

### 🔹 Kafka Client Library  
- **`kafka-python`** → Used to connect with **Apache Kafka**, send data (producer), and consume data (consumer).  

### 🔹 Snowflake Connector  
- **`snowflake-connector-python`** → Helps in establishing a connection between Python and **Snowflake**, allowing queries and data transfers.  

### 🔹 Data Manipulation  
- **`pandas`** → Used for handling, transforming, and preparing **structured data** before sending it to Snowflake.  

### 🔹 JSON Parsing  
- **`json`** → Helps in reading and writing **JSON-formatted** data, often used for configurations and messages.  

### 🔹 Logging Framework  
- **`logging`** → Used to track errors, warnings, and execution flow for both producers and consumers.  

### 🔹 Snowflake + Pandas  
- **`snowflake-connector-python[pandas]`** → Adds support for **write_pandas**, allowing **efficient DataFrame uploads** to Snowflake.  

---

## 🚀 How to Run the Project  

### 1️⃣ Install Dependencies  
Open **Command Prompt** and run:  
```bash
pip install -r requirements.txt
