# Exploratory Data Analysis (EDA) & Business Intelligence Project

## Project Overview

This project focuses on performing **Exploratory Data Analysis (EDA)** and generating **Business Intelligence insights** from multiple business datasets.
The goal is to identify patterns, trends, and relationships in the data and present useful insights using data analysis and visualization tools.

The project includes:

* Data exploration and statistical analysis
* SQL queries to answer business questions
* Visualization using a Power BI dashboard

---

## Project Objectives

* Understand the structure and distribution of datasets.
* Perform **descriptive statistics and univariate analysis**.
* Use **SQL queries** to answer business-related questions.
* Identify relationships between variables through **multivariate analysis**.
* Create a **Power BI dashboard** to present key insights.

---

## Tools and Technologies Used

* Python – Data analysis and preprocessing
* SQL – Data querying and business analysis
* Power BI – Data visualization and dashboard creation
* GitHub – Version control and project hosting

---

## Datasets Used

### 1. Superstore Sales Dataset

Contains information about product sales including:

* Order details
* Product categories
* Sales amount
* Quantity and customer information

### 2. E-commerce Sales Dataset

Includes online sales transaction data such as:

* Orders and products
* Revenue and sales information
* Shipping and delivery details

### 3. Customer Purchase Dataset

Provides insights into customer purchasing behavior including:

* Customer IDs
* Purchase history
* Product preferences
* Transaction records

---

## Project Structure

```
eda-business-intelligence-project/
│
├── data/
│   ├── Superstore_Sales.csv
│   ├── E-commerce_Sales.csv
│   └── Customer_Purchase.csv
│
├── eda_analysis.py
├── sql_queries.sql
├── dashboard_mockup.pbix
└── README.md
```

### Folder and File Description

**data/**
This folder contains all datasets used in the project.

* Superstore_Sales.csv – Sales data of products and orders
* E-commerce_Sales.csv – Online sales transaction dataset
* Customer_Purchase.csv – Customer purchase behavior dataset

**eda_analysis.py**
Python script used to perform exploratory data analysis including data cleaning, statistical analysis, and data visualization.

**sql_queries.sql**
Contains SQL queries written to answer important business questions such as sales trends, product performance, and customer analysis.

**dashboard_mockup.pbix**
Power BI dashboard file that visualizes key insights such as sales trends, category performance, and order distribution.

**README.md**
Project documentation explaining the project details, datasets, tools used, and analysis process.

---

## Exploratory Data Analysis

EDA was performed using Python to better understand the datasets.

Key steps included:

* Loading datasets
* Checking for missing values
* Summary statistics of numerical data
* Distribution analysis using histograms
* Category analysis using bar charts
* Correlation analysis between variables

Python libraries used:

* pandas
* numpy
* matplotlib
* seaborn

---

## SQL Business Queries

SQL queries were written to answer several business questions such as:

* What are the top performing product categories?
* Which customers generate the highest revenue?
* What is the monthly sales trend?
* Which regions generate the most orders?
* Which products are sold the most?

These queries help extract useful insights from structured data.

---

## Power BI Dashboard

A Power BI dashboard was created to visualize key business insights.

### Dashboard Features

* Total Sales and Total Orders KPI
* Sales trend analysis
* Category-wise sales performance
* Quantity sold by product category
* State-wise order distribution
* Order status analysis
* Courier or shipment status tracking

The dashboard helps stakeholders quickly understand business performance through visual analytics.

---

## Key Insights

* Identification of high-performing product categories.
* Analysis of customer purchasing patterns.
* Understanding regional sales distribution.
* Monitoring order and shipment status.

These insights support **data-driven decision making**.

---

## Future Improvements

* Implement predictive models for sales forecasting.
* Add more advanced data visualizations.
* Create interactive dashboards with filters.
* Integrate additional datasets for deeper analysis.

---

## Conclusion

This project demonstrates how **Exploratory Data Analysis, SQL, and Business Intelligence tools** can transform raw data into meaningful insights.
It highlights the importance of data analytics in improving business strategies and supporting better decision-making.
