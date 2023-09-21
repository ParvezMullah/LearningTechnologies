### Certification Details
 Integrating, transforming and consolidating data from various structured and unstructured data systems into structures that are suitable for building analytical solutions.

 #### Architecture pattern
    1. Modern data warehouse
    2. Big data
    3. Lakehouse architecture

#### Data processing solutions
    1. Azure Data Factory
    2. Azure Synapse Analytics
    3. Azure Stream Analytics
    4. Azure Event Hubs
    5. Azure Datalake Storage
    6. Azure Data Bricks


# Microsoft Azure Data Fundamentals: Explore core data concepts

## Explore core data concepts

### Introduction
#### Learning objectives
    1. Identify common data formats
    2. Describe options for storing data in files
    3. Describe options for storing data in databases
    4. Describe characteristics of transactional data processing solutions
    5. Describe characteristics of analytical data processing solutions

### Identify data formats
Data is the collection of facts such as number, description and observation used to record information. Data can be stored in various formats. The most common data formats are:
    1. Structured data
    2. Semi-structured data
    3. Unstructured data
#### Data stores
1. File stores
2. Database stores

### Explore file storage
1. Delimited text files
2. JSON files
3. XML files
4. Blob storage(Binary large object)

#### Optimised file formats
Some specialised file formats that enable compression, indexing and efficient storage and processing. These include:
1. Avro
    Row based.each record contins a header in json format that describes the structure of the data in the record. good for compressing data and minimizing storage space and network bandwidth.
2. ORC(optimized row columnar)
    columnar. optimised for read and write in apache hive.
3. Parquet
    columnar.  contains row gropus.specialises in storing and processing nested data types efficiently. very efficient compression and encoding schemes.

### Explore databases
1. Reational Databases
2. Non-relational Databases
    1. key value database.
    2. Document databases.
    3. Column family databases.
    4. Graph databases.

### Explore Transactional data processing
1. Atomicity
2. Consistency
3. Isolation
4. Durability

### Analytical data processing
ready-only system of historical data.
1. Data files may be stored in a central data lake for analysis.
2. ETL(Extract, Transform, Load) process is used to move data from the source system to the data lake.
3. Data from warehouse is loaded into OLAP cubes for analysis.
4. Data in the data lake, warehouse and analytical model can be queried to produce reports, visualizations and dashboards.

#### Data lakes are common in large scale data analytical procesing scenarios, where a large volumne of filebased data must be collection and analyised.

#### Data warehouses are an established way to store data in a relational schema that is optimised for read operations. primaryily queries to support reporting and data visualisation.

## Explore data roles and services

### Introduction
1. Identify common data professional roles.
2. Identify common cloud services used by data professionals.

### Explore job roles in the world of data
### Identify data services
1. Azure SQL 
    It is a collective name for a family of relational database solutions based on the Microsoft SQL server database engine.
    1. Azure SQL Database - Fully managed PAAS
    2. Azure SQL Managed Instance - hosted instance of SQL with more flexibility.
    3. Azure SQL VM- a virutal machine with an installlation of SQL Server with maximum configurability.
2. Azure Database for open-source relational databases
    1. Azure Database for MySQL
    2. Azure Database for PostgreSQL
    3. Azure Database for MariaDB
3. Azure Cosmos DB
    global scale non relational database service.
4. Azure storage
    1. Azure Blob storage
    2. Azure Files
    4. Azure Table storage
5. Azure Data Factory
    schedule data pipelines to transfer and transform data. you can integrate your pipellines with other Azure services, enabling you to ingest data from cloud data stores, process the data using cloud based compute, and perisist the result to into data store. ETL Solution.
6. Azure Synapse Analytics
Unified data analytical solutions that combines data ingestion pipelines, data warehouse storage and data lake storage though a single service.
    1. Azure Synapse SQL
    2. Azure Synapse Spark
    3. Azure Synapse Pipelines
    4. Azure Synapse Data explorer - high performant data analytical solution for real time querying the log and telemetry data using KQL.
7. Azure Databrick
    Apache Spark based analytics platform optimized for the Microsoft Azure cloud services platform.
8. Azure HDInsight
    cloud based service for open source analytics. it is a managed hadoop, spark, kafka, Hbase, and storm clusters.
9. Azure Stream Analytics
    real time analytics and complex event processing over streaming data.
10. Azure Data Explorer
    fast and highly scalable data exploration service for log and telemetry data.
11. Microsoft Purview
    unified data governance service that helps you manage and govern your on-premises, multi-cloud and software-as-a-service(SaaS) data.
12. Microsoft Power BI
    business analytics service that delivers insights to enable fast, informed decisions.
### Knowledge check
### summary

# Microsoft Azure Data Fundamentals: Explore relational data in Azure

## Explore fundamental relational database concepts

### Introduction
### Understand relational data
### Understand normalization
### Explore SQL
### Describe database objects


## Explore relational database services in Azure

### Introduction
enables multiple database services such as SQL Server, MySQL, PostgreSQL, MariaDB to run on virtual machines in Azure.
#### Learning objectives
1. Identify options for Azure SQL Services.
2. Identify options for open source databases.
3. Provision a database service on Azure.

### Describe Azure SQL services and capabilities
![Alt Text](./images/SQL%20Services.png)

### Describe Azure services for open-source databases
1. Azure database for MySQL
2. Azure database for PostgreSQL
3. Azure database for MariaDB
### Exercise: Explore Azure relational database services

# Microsoft Azure Data Fundamentals: Explore non-relational data in Azure

# Microsoft Azure Data Fundamentals: Explore data analysis in Azure