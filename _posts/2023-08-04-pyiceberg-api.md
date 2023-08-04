---
layout: single
title: "Using Your Favorite Snake for Insights From Iceberg"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2023-08-04 20:00:00 +0000
categories: iceberg
tags: iceberg api apache cloudera ds

---
*From Apache, "Iceberg is a high-performance format for huge analytic tables. Iceberg brings the reliability and simplicity of SQL tables to big data, while making it possible for engines like Spark, Trino, Flink, Presto, Hive and Impala to safely work with the same tables, at the same time." This article addresses the benefits and usability for real development use cases that the developmental Iceberg Python (aka the "Snake") API helps to solve.*

![](/assets/posts/2023-08-04-pyiceberg-api/PyIceberg.png)

## Wrestling the Iceberg Snake
Building on my last article about Iceberg, one of the key components in any data scientist's toolkit is their ability to use SQL to extract meaningful insights from massive datasets with speed and point-in-time accuracy that is defensible. To boot, many engines include Java as a standard library with a feature rich API set but will often neglect the snake in the room until the product comes further along. Currently in development, the Python API for Iceberg, "PyIceberg" offers most of the features its Java sister offers with a few notable limitations that the open source community plans to address in upcoming releases. As a library, it offers programmatic access to Iceberg table metadata and table data stored in Iceberg format.

From a metadata perspective, the Python API allows users to get schema and snapshots, plan scan and plan scan for snapshots, create and drop tables, and create, set, and drop namespaces. It supports all the major primitive types and most of the nested types (does not yet support ListType and MapType). Some of the other features like updating current snapshots, setting table properties, and altering tables that the Java companion offers with regard to metadata are a part of the future plans for Iceberg's Python API development. For a full list of supported functionality by the API, check out their [Feature Support](https://py.iceberg.apache.org/feature-support/) page as well.

## Understanding PyIceberg Through its Use Cases
Perhaps one of the most effective ways to understand the "why" of any product or library is to understand its use cases. Developers and data analysts need to quickly extract meaningful data from their extremely large tables. The use cases that define data access are not particularly unique and don't set Iceberg apart; however, they are essential if it is ever to be considered a replacement for its longstanding industry companions. PyArrow (which I address again later on) and pyODBC both offer pythonic ways to run queries over Iceberg tables and give these developers and data analysts easy, programmatic access to large sets of data. 

The benefit to Iceberg becomes so much greater when you consider use cases that exceed the industry norms. For a financial client, the Iceberg table format allows for querying data over time, meaning data provenance and data governance can be understandable, solvable tasks for DBAs to track changes to their data. Additionally, and this would be beneficial to not just financial clients, but government and health care clients as well, the ACID nature of Iceberg allows for use cases that need highly reliable, strong data integrity queries, and PyIceberg puts that capability right into the hands of the developers. 

While in its current state, the problems being solved by PyIceberg and its companions are largely "read only" problems, but in many cases this covers the vast majority of developmental applications, and there is still much work being done in the background by the open source community to help enable Pythonic "write" use cases as well. 

## How can I leverage the Iceberg Python API in my development efforts?
The [PyIceberg Python Library](https://github.com/apache/iceberg/tree/master/python) can be installed via Pip by either of the following commands: 

<code>
pip3 install "pyiceberg[*]"
</code> 

*or*

<code>
pip install "git+https://github.com/apache/iceberg.git#subdirectory=python&egg=pyiceberg[*]"
</code>

*Note that in both cases above, the * represents the optional dependencies you may need to get started in the enviroment of your choosing (pyarrow, etc.)*

Apache's detailed [docs](https://py.iceberg.apache.org/) on PyIceberg extensively cover the settings, variables and configuration sets to effectively use PyIceberg against data in the public cloud or through an on-premise deployment. The [api docs](https://py.iceberg.apache.org/api/) provide sample code as well to kick start your querying. The project also allows for filtering down a large table into a PyArrow table, assuming you have the requisite Apache Arrow installation. I highly recommend you spend some time on that last link. It walks through a standard instantiation of PyIceberg and how to structure your code to ultimately create a table and query some data using a table scan.


## Want to Read More and Get Started?
If any of the features I discussed sound interesting to you, I would encourage you to check out the links below and get hands on. Additionally, if you have not read my article last week, I hope you'll take some time to read it and see how Iceberg provides valuable capabilities that set it apart from other engines in the big data space today.

[Source Repo for the Apache Iceberg Product](https://github.com/apache/iceberg)

[Getting Started with PyIceberg (Code Snips)](https://py.iceberg.apache.org/api/)

[Iceberg in CDP](https://docs.cloudera.com/cdp-public-cloud/cloud/cdp-iceberg/topics/iceberg-in-cdp.html)

[Vendors Supporting Apache Iceberg](https://iceberg.apache.org/vendors/#clouderahttpclouderacom)