# Project_1

## Data Engineering Pipeline - Personal learning project 

This is a small, self-contained data engineering project for practice and learning purposes. The goal is to simulate a basic batch ETL (Extract, Transform, Load) pipeline using a static dataset, AWS services, and lightweight data transformation logic.

The dataset is processed in batches, transformed for cleanliness and consistency, and stored in a queryable format for analysis using AWS Athena or other tools.

https://trello.com/b/3lIfOuWe/project1 

---

## Tech Stack

| Component       | Tool/Service         |
|----------------|----------------------|
| **Language**    | Python               |
| **Storage**     | Amazon S3            |
| **Transformation** | Python (Pandas or PySpark (!!!)) |
| **Query Layer** | AWS Athena (!!!)         |
| **Serverless compute**    | AWS Lambda, Glue (!!!), Step Functions |
| **Data Format** | CSV (raw) → Parquet (processed) |

---

## Dataset

- **Name**: LEGO Database
- **Source**: (https://www.kaggle.com/datasets/rtatman/lego-database)
- **Size**: 12.99MB
- **Format**: CSV
- **Description**: This dataset contains the LEGO Parts/Sets/Colors and Inventories of every official LEGO set in the Rebrickable database. These files are current as of July 2017.

---

## The ETL Pipeline Overview

1. **Extract**
   - Database is replicated via csv exports saved to a s3 (file-storage-bucket/Project-1)
   - Files are read and loaded into pandas DataFrames
   - Includes error handling.
   - Data saved to extract s3 bucket

2. **Transform**
   - Clean data (e.g., handle nulls, fix date formats, normalize values)
   - Convert to Parquet

3. **Load**
   - Store cleaned data in a separate S3 folder
   - (checkout querying with AWS Athena)

---
### Local Dev Environment

#### Clone the repo
git clone https://github.com/sarah-larkin/Project_1.git <br>
cd Project_1

#### Create virtual environment
python -m venv venv <br>
source venv/bin/activate  (Ubuntu)

#### Install dependencies
pip install -r requirements.txt

## Learning/Practice objectives

- How to structure a basic data pipeline
- Working with AWS S3 and Athena
- Converting CSV to Parquet for efficiency
- Cleaning and validating datasets with Python
- Writing and organizing project code for reuse
- Basic cost-awareness using free-tier AWS services

## Reflection 

- challenges? 
- successes? 
- what would you change next time? 
- other ideas? 