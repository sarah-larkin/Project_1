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

- **Name**: AI Powered Job Market Insights
- **Source**: (https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights)
- **Size**: 47.41kb
- **Format**: CSV
- **Description**: The "AI-Powered Job Market Insights" dataset provides a synthetic but realistic snapshot of the modern job market, particularly focusing on the role of artificial intelligence (AI) and automation across various industries. This dataset includes 500 unique job listings, each characterized by different factors like industry, company size, AI adoption level, automation risk, required skills, and job growth projections. It is designed to be a valuable resource for researchers, data scientists, and policymakers exploring the impact of AI on employment, job market trends, and the future of work.

---

## The ETL Pipeline Overview

1. **Extract**
   - csv file to Amazon S3

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