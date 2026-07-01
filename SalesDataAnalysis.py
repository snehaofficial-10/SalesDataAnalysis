import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use("default")
sns.set_theme()


df = pd.read_csv(
    r"C:\Users\pc\Downloads\Sales Data Analysis Dashboard\Sample - Superstore.csv",
    encoding="latin1")
print(df.head())
print(df.info())
print(df.isnull().sum())

print("Duplicate:", df.duplicated().sum())
df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()

print(df.shape)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print(f"Total Sales : ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print("Total Orders:",total_orders)
print("Total Customers:",total_customers)

print(df.head())
print(df.describe())

category_sales = df.groupby("Category")['Sales'].sum().sort_values()
plt.figure(figsize=(8,5))
category_sales.plot(kind="barh")
plt.title("Sales by Category")
plt.xlabel("Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



profit_cat = df.groupby("Category")['Profit'].sum()
plt.figure(figsize=(8,5))
sns.barplot(x=profit_cat.index, y=profit_cat.values)
plt.title("Profit by Category")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()




top_products = df.groupby("Product Name")['Sales']\
               .sum()\
               .sort_values(ascending=False)\
               .head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values , y=top_products.index)
plt.title("Top 10 Products by Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()





top_states = df.groupby("State")['Sales']\
               .sum()\
               .sort_values(ascending=False)\
               .head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_states.values , y=top_states.index)
plt.title("Top 10 States by Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()




monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
      .sort_index()
)
monthly_sales.plot(figsize=(12,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



year_sales = (
    df.groupby("Year")["Sales"]
      .sum()
      .sort_index()
)
plt.figure(figsize=(8,5))
sns.lineplot(x=year_sales.index,
             y=year_sales.values,
             marker='o')
plt.title("Yearly Sales Trend")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


segment_sales = df.groupby("Segment")["Sales"].sum()
plt.figure(figsize=(8,5))
plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.axis("equal")
plt.title("Sales Contribution by segment")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.6
)
plt.title("Discount vs Profit")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))
sns.heatmap(
    df[["Sales","Quantity","Discount","Profit"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(
    df["Profit"],
    bins=30,
    kde=True
)
plt.title("Profit Distribution")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


top_customer = df.groupby("Customer Name")['Sales']\
               .sum()\
               .sort_values(ascending=False)\
               .head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_customer.values , y=top_customer.index)
plt.title("Top  Customers by Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


loss_subcat= df.groupby("Sub-Category")["Profit"]\
             .sum()\
             .sort_values()
print(loss_subcat.head())


ship_sales = df.groupby("Ship Mode")["Sales"].sum()
plt.figure(figsize=(8,5))
sns.barplot(
    x=ship_sales.index,
    y=ship_sales.values
)
plt.xticks(rotation=20)
plt.title("Sales by Ship Mode")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



df.to_csv("cleaned_superstore.csv", index=False)











