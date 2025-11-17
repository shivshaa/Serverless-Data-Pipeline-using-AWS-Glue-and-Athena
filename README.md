# 🚀 AWS ETL Pipeline: CSV to Analytics


An end-to-end serverless ETL data pipeline demonstrating how to ingest, transform, and analyze CSV data using AWS managed services. Built with infrastructure-as-code principles using CloudFormation.

---

## 📋 Project Overview

This project showcases a complete data engineering workflow that processes locally stored CSV files through a fully automated AWS pipeline:

- **CSV Ingestion** → Amazon S3
- **Data Transformation** → AWS Glue (CSV to Parquet)
- **Schema Discovery** → Glue Crawler
- **Metadata Cataloging** → Glue Data Catalog
- **Analytical Querying** → Amazon Athena
- **Infrastructure Automation** → CloudFormation (IaC)
- **Local Upload Utilities** → Python (Boto3)

---

## 🏗️ Architecture

![Architecture](screenshot/data-pipeline-arch.png)


**Data Flow:**
1. Upload CSV files to S3 raw bucket
2. Glue ETL job transforms CSV → Parquet format
3. Glue Crawler scans curated data and registers schema
4. Glue Data Catalog stores table metadata
5. Athena queries data using SQL

![Athena Query 1](screenshot/AthenaQuery1.png)
![Athena Query 2](screenshot/AthenaQuery2.png)
![Athena Output Files](screenshot/Athena-output-files.png)

![Glue Job](screenshot/GlueJob.png)
![Glue Output Files](screenshot/Glue-output-files.png)

![CloudFormation](screenshot/CloudFormation.png)

![Python Script](screenshot/python-script.png)

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
