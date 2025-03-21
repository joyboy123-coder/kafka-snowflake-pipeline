# Kafka Producer Data Flow

## Overview

This project demonstrates how a **Kafka producer** generates and sends data to a Kafka topic. The logs track each message sent.

---

## Data Flow Process

1. **config.json**  
   - Stores Kafka and logging settings.  
   
2. **producer.py**  
   - Reads `config.json`.  
   - Sets up logging.  
   - Creates a Kafka producer.  

3. **Data Generation**  
   - Uses Faker to generate random messy data.  

4. **Kafka Producer**  
   - Sends the generated data to a Kafka topic.  

5. **Logging**  
   - Logs messages being sent to a `.log` file.  

6. **Kafka Topic**  
   - Stores incoming messages.  

7. **Kafka Consumer (Optional)**  
   - Can be used to read the stored messages.  

---

## Example: How Data is Sent and Logged

### Sample Generated Data (Before Sending to Kafka)

```json
{
    "id": 1234,
    "name": "John Doe",
    "age": 29,
    "city": "New York",
    "email": "johndoe@example.com",
    "phone_number": "123-456-7890",
    "random_field": null,
    "special_chars": "!@#$%",
    "date": "2024-03-21",
    "time": "14:30:00",
    "invalid_data": "N/A",
    "zipcode": 10001
}


# Log File Content (Tracking Sent Messages)

2025-03-21 12:00:01 - INFO - Sending message to Kafka topic KAFKA_STREAMING: {"id": 1234, "name": "John Doe", "age": 29, "city": "New York", ...}
2025-03-21 12:00:03 - INFO - Message sent to topic KAFKA_STREAMING
2025-03-21 12:00:05 - INFO - Sending message to Kafka topic KAFKA_STREAMING: {"id": 5678, "name": "Jane Smith", "age": 34, "city": "Los Angeles", ...}


---

# Expected Data Flow Visualization

| Step | Action    | Description                          |
|------|----------|--------------------------------------|
| 1    | Producer | Generates messy data using Faker   |
| 2    | Kafka    | Receives data from the producer    |
| 3    | Log File | Stores information about messages  |

