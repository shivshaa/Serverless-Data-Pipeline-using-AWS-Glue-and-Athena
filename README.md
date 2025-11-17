# 🚀 AWS ETL Pipeline: CSV to Analytics


An end-to-end serverless ETL data pipeline demonstrating how to ingest, transform, and analyze CSV data using AWS managed services. Built with infrastructure-as-code principles using CloudFormation.

## 🏗️ Architecture

<img src="screenshots/data-pipeline-arch.png" alt="Architecture" width="800">


## 📋 Project Overview

This project showcases a complete data engineering workflow that processes locally stored CSV files through a fully automated AWS pipeline:

- **CSV Ingestion** → Amazon S3
- **Data Transformation** → AWS Glue (CSV to Parquet)
- **Schema Discovery** → Glue Crawler
- **Metadata Cataloging** → Glue Data Catalog
- **Analytical Querying** → Amazon Athena
- **Infrastructure Automation** → CloudFormation (IaC)
- **Local Upload Utilities** → Python (Boto3)



**Data Flow:**
1. Upload CSV files to S3 raw bucket
2. Glue ETL job transforms CSV → Parquet format
3. Glue Crawler scans curated data and registers schema
4. Glue Data Catalog stores table metadata
5. Athena queries data using SQL


<img src="screenshots/AthenaQuery1.png" alt="Athena Query 1" width="600">

<img src="screenshots/AthenaQuery2.png" alt="Athena Query 2" width="600">

<img src="screenshots/Athena-output-files.png" alt="Athena Output Files" width="600">

<img src="screenshots/GlueJob.png" alt="Glue Job" width="600">

<img src="screenshots/Glue-output-files.png" alt="Glue Output Files" width="600">

<img src="screenshots/CloudFormation.png" alt="CloudFormation" width="600">

<img src="screenshots/python-script.png" alt="Python Script" width="600">

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---------|---------|
| **Amazon S3** | Data lake storage (raw & curated zones) |
| **AWS Glue** | Serverless ETL processing |
| **Glue Crawler** | Automated schema discovery |
| **Glue Data Catalog** | Centralized metadata repository |
| **Amazon Athena** | Serverless SQL analytics engine |
| **AWS CloudFormation** | Infrastructure as Code deployment |
| **AWS IAM** | Permissions and access control |

---

---
# 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Project Link: [https://github.com/yourusername/aws-etl-pipeline](https://github.com/shivshaa/Serverless-Data-Pipeline-using-AWS-Glue-and-Athena)

---

## 🙏 Acknowledgments

- AWS Documentation
- AWS Glue Best Practices
- Serverless Data Engineering Community

---

**⭐ If you found this project helpful, please consider giving it a star!**
