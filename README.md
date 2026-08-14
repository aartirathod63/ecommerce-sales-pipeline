# E-commerce Sales Data Pipeline

## Project Overview

This project implements an end-to-end data engineering pipeline for processing e-commerce sales data.

The pipeline extracts raw CSV data, cleans and transforms it using Python and Pandas, validates data quality, rejects invalid records, loads the processed data into MySQL, and performs SQL analytics to generate business insights.

## Tech Stack

- Python
- Pandas
- MySQL
- SQL
- Git & GitHub
- Python-dotenv

## Pipeline Architecture

Raw CSV Data
    |
    v
Extraction
    |
    v
Data Cleaning & Validation
    |
    v
Transformation
    |
    +----> Rejected Records
    |
    v
Processed CSV Data
    |
    v
MySQL Database
    |
    v
SQL Analytics
    |
    v
Business Insights

## Project Structure

ecommerce-sales-pipeline/
|
├── app/
├── data/
│   ├── raw/
│   ├── processed/
│   └── rejected/
├── sql/
│   └── create_tables.sql
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run_transform.py
├── .gitignore
├── requirements.txt
└── README.md

## Data Quality

The pipeline performs:

- Duplicate removal
- Column name standardization
- Data validation
- Foreign-key validation
- Invalid order detection
- Invalid order-item detection
- Rejected-record handling

## Database

The MySQL database contains:

- customers
- products
- orders
- order_items

The tables use primary keys and foreign-key relationships to maintain data integrity.

## SQL Analytics

The project includes SQL analysis for:

- Monthly revenue
- Product sales performance
- Category revenue
- Average order value
- Customer lifetime value
- One-time vs repeat customers
- Customer revenue ranking
- City-wise customer ranking
- Month-over-month revenue growth
- Latest order per customer
- Latest order value per customer

## Data Quality Results

During transformation:

- 111 valid orders were processed
- 7 invalid orders were rejected
- 183 valid order items were loaded
- 15 invalid order items were rejected

Invalid records were stored separately under `data/rejected/`.

## How to Run

### 1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>

cd ecommerce-sales-pipeline

### 2. Create virtual environment

python3 -m venv .venv

source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file containing your MySQL connection details.

Example:

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=ecommerce_db

### 5. Run transformation

python src/run_transform.py

### 6. Load data into MySQL

python src/load.py

## Key Outcome

This project demonstrates a practical ETL workflow with Python, Pandas, MySQL, data quality validation, error handling, relational database design, and analytical SQL.

## Author

Aarti S Rathod
