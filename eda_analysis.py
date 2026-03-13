import pandas as pd

# Load datasets
superstore = pd.read_csv("data/Superstore_Sales.csv")
ecommerce = pd.read_csv("data/E-commerce_Sales.csv")
customer = pd.read_csv("data/Customer_Purchase.csv")

print(superstore.head())
print(ecommerce.head())
print(customer.head())
