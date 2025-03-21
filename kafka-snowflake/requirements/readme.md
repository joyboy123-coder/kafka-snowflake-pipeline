# 📌 Kafka-Snowflake Pipeline  

This project sets up a real-time data pipeline using Kafka and Snowflake.  

## 📂 Project Structure  

- **requirements/** → Contains dependencies required for the project  
- **config.json** → Stores credentials and configuration settings  
- **samples/** → Sample data used for testing  
- **producer/** → Kafka producer scripts  
  - **logging/** → Logging for producer processes  
- **consumer/** → Kafka consumer scripts  
  - **logging/** → Logging for consumer processes  
- **transformations/** → Data cleaning and transformation  

## ⚙️ What We Are Doing  

- **Kafka Producers** → Sending real-time data  
- **Kafka Consumers** → Receiving data from Kafka  
- **Data Transformation** → Cleaning and structuring messy data  
- **Uploading to Snowflake** → Using `write_pandas` for efficient uploads  
- **Logging** → Tracking producer and consumer activities  

## 🚀 How to Run the Project  

### 1️⃣ Install Dependencies  
Open **CMD** and run:  
```sh
pip install -r requirements.txt
