
# Netflix Data Engineering Project (Azure + Delta Live Tables)

This project demonstrates an **end-to-end Data Engineering pipeline** using **Azure Data Services**, **Databricks Delta Live Tables**, and **Power BI** to build a robust data pipeline for streaming and batch processing of Netflix data.

## Architecture Overview

![Architecture Diagram](./images/architecture.png)

---

## Components

### 1. **Data Ingestion**
- Source: Raw Netflix CSV files.
- Ingestion Tools:  
  - **Azure Data Factory (ADF)** – Orchestrates and schedules ingestion.  
  - **Databricks** – Performs incremental loading and processing.
  - **Python Script** - Perform automation.
- Data stored in:  
  - **Azure Data Lake Storage Gen2** (bronze)

---

### 2. **Incremental Data Load**
- Raw data is stored in **Bronze Tables**.
- Delta Lake is used for **versioned and transactional data handling**.

---

### 3. **Data Transformation**
- **Delta Live Tables (DLT)** orchestrate transformations:
  - Clean and enrich data.
  - Store in **Silver Tables** in Data Lake Gen2.
- Transformations follow **PySpark logic** for modularity and maintainability.

---

### 4. **Data Modeling**
- Structured into a **Star Schema** for analytics:
  - Fact & Dimension tables.
  - Stored in **Gold Tables** using Delta Lake.

---

### 5. **Serving Layer**
- Cleaned and modeled data is pushed to:
  - **Azure Synapse Analytics** (Warehouse).
  - Used for advanced queries and BI integration.

---

### 6. **Reporting**
- Final data consumed via:
  - **Power BI Dashboards**
  - Real-time analytics and executive insights.

---

## Tech Stack

| Layer            | Tool/Service             |
|------------------|--------------------------|
| Storage          | Azure Data Lake Gen2     |
| Processing       | Azure Data Factory, Databricks |
| Transformation   | Delta Lake, Delta Live Tables |
| Data Modeling    | Star Schema, Delta Tables |
| Serving          | Azure Synapse Analytics  |
| Visualization    | Power BI                 |

---

## Sample Use Cases

- Track most watched Netflix shows by region.
- Identify viewing trends over time.
- Analyze genres with highest engagement.
- Create reports segmented by country, device, age group, etc.

---

## Prerequisites

- Azure Subscription.
- Databricks Workspace linked to Azure.
- Azure Data Lake Gen2.
- Azure Synapse Analytics.
- Power BI Desktop.

---

## How to Run

1. **Upload raw Netflix data to Azure Data Lake Gen2 (Bronze zone).**
2. **Trigger ADF pipeline** to move data to Databricks.
3. **Run Delta Live Tables** pipelines to perform transformation.
4. **Model data using Star Schema** and publish to Gold layer.
5. **Connect Azure Synapse & Power BI** to query and visualize.

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change or improve.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
