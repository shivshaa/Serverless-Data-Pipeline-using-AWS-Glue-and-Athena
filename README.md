# 🚀 AWS ETL Pipeline: CSV to Analytics

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![Glue](https://img.shields.io/badge/AWS-Glue-blueviolet)](https://aws.amazon.com/glue/)
[![Athena](https://img.shields.io/badge/AWS-Athena-blue)](https://aws.amazon.com/athena/)
[![CloudFormation](https://img.shields.io/badge/IaC-CloudFormation-green)](https://aws.amazon.com/cloudformation/)

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

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Local CSV  │────▶│  S3 Raw Zone │────▶│  Glue Job   │────▶│Curated Zone  │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                    ┌──────────────┐     ┌─────────────┐      ┌──────────────┐
                    │  Athena      │◀────│Glue Catalog │◀────│Glue Crawler  │
                    └─────────────-┘     └──────────────┘     └─────────────-┘    
```

**Data Flow:**
1. Upload CSV files to S3 raw bucket
2. Glue ETL job transforms CSV → Parquet format
3. Glue Crawler scans curated data and registers schema
4. Glue Data Catalog stores table metadata
5. Athena queries data using SQL

[![Athena]](AthenaQuery1.png)
[![Athena]](AthenaQuery2.png)
[![Athena]](Athena-output-files.png)
[![Glue]](GlueJob.png)
[![Glue](Glue-output-files.png)
[![Athena](https://aws.amazon.com/athena/)
[![CloudFormation](CloudFormation.png)
[![Script](python-script.png)
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
