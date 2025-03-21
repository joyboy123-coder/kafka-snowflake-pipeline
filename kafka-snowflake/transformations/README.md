# 🛠️ Data Cleaning Script – Transforming Raw JSON Data into Gold ✨

## 📌 Overview  
This script takes messy JSON data and **cleans it up** 🧹 before sending it further down the pipeline. It processes names, emails, addresses, and timestamps while ensuring consistency and accuracy.  

## 🚀 Features  

### 🔠 Column Name Standardization  
✅ **Converts all column names to uppercase** for uniformity 📢  

### 🔢 Sorting Data  
✅ **Sorts records by `ID`** to maintain order 📊  

### ✂️ Cleaning Text Fields  
✅ **Formats names & cities properly** – Converts to title case and removes extra spaces 🏙️  

### 🔄 Data Type Conversion  
✅ **Ensures `AGE` is an integer** for consistency 🔢  

### 📧 Email Standardization  
✅ **Reformats all email addresses** to use `@gmail.com` 📩  

### 🏡 Address Cleaning  
✅ **Removes unnecessary details from addresses** and keeps only relevant parts 🏠  

### 🕒 Timestamp Generation  
✅ **Creates a `TIME_STAMP` column** by combining `DATE` and `TIME` 📅⏳  

### 🗑️ Removing Unwanted Columns  
✅ **Drops irrelevant fields** (`PHONE_NUMBER`, `RANDOM_FIELD`, `SPECIAL_CHARS`, `DATE`, `TIME`, `INVALID_DATA`) for cleaner data 🧹  

## 🎯 Why This Matters  
🚀 This script **automates** data cleaning, making it **ready for analysis, storage, or further transformations**. It ensures structured, standardized, and meaningful data, saving time & effort!  

  
🚀 **Power up your ETL pipeline with clean & structured data!**  

