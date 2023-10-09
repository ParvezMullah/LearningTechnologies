# Introduction
1. What is Azure Data factory
    1. Azure Data factory is Azure's cloud ETL service for scale-out serverless data integration and data transformation. you can also lift and shift exisiting SSIS packages to Azure and run them with full compatibility in ADF.
    2. It is the cloud based ETL and data integration service that allows you to create data-driven workflows for orchestrating data movement and transforming data at scale.
2. What is ETL
2. Why Azure Data factory
4. Discuss an example to understand it better

# Top Lvel concepts in Azure Data factory
1. Pipelines
    A pipeline is a logical grouping of activities that together perform a task. A pipeline defines the order in which the activities are executed, and you can parameterize pipelines to execute the same logic for different values.

    For example, a pipeline can contain a group of activities that ingests data from an Azure blob, and then runs a Hive query on a HDInsight cluster to partition and store the data in an Azure SQL database.
2. Activities
    1. Activities represents a processing step in a pipeline. For Example, a copy activity that copies data from one location to another location.
3. Datasets
    1. Datasets represent data structures within Data Factory. For example, a dataset could be a single table or a file that you want to copy or transform.
4. Linked Services
    1. Linked services are much like connection strings, which define the connection information needed for Data Factory to connect to external resources. For example, a linked service for an Azure Storage account specifies the information needed for Data Factory to connect to an Azure Storage account.
5. Triggers
    1. Triggers are used to execute a pipeline or invoke a logic app at a specified time or in response to an event, and you can parameterize triggers to execute the same logic for different values. For example, you can create a trigger that executes a pipeline every hour, or a trigger that executes a pipeline when a file is added to an Azure blob container.

# Create your first azure data factory
    1. create linked service
    2. create source
    3. create destination
    4. create pipeline
    5. create trigger

# Different ways to work with Azure Data factory
    1. Azure portal UI
    2. Azure powershell
    3. .NET
    4. Python
    5. REST API
    6. Resource Manager Templates

# Pipelines and Activities in Azure Data Factory
    1. Datasets identify data within different data stores, such as tables, files, folders, and documents.
    2. Types of activities
        1. Data movement activities
        2. data transformation activities
        3. control activities