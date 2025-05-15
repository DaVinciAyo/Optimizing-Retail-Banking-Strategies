import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import os

# Load data
data_path = "../data/bank_data_C.csv"
bank = pd.read_csv(data_path)

# Date conversion
bank["CustomerDOB"] = bank["CustomerDOB"].astype(str).str.replace("-", "/")
bank["CustomerDOB"] = pd.to_datetime(bank["CustomerDOB"], format="%d/%m/%y", errors='coerce')
bank["TransactionDate"] = pd.to_datetime(bank["TransactionDate"], format = '%d/%m/%y')
# Create 'Age' column
today = pd.to_datetime("today")
bank['Age'] = (today - bank['CustomerDOB']).dt.days // 365
bank = bank[(bank['Age'] >= 18) & (bank['Age'] <= 100)]


# Plot: daily transaction trend
daily_transactions = bank.groupby('TransactionDate')['TransactionAmount (INR)'].sum().reset_index()
daily_transactions.columns = ["TransactionDate", "TransactionAmount (INR)"]
plt.figure(figsize=(30, 7))
plt.plot(daily_transactions["TransactionDate"], daily_transactions["TransactionAmount (INR)"], marker='o', linestyle='-')

plt.xlabel('Date')
plt.ylabel('Total Transaction Amount (INR)')
plt.title('Daily Transaction Amount Trend')
plt.xticks(daily_transactions["TransactionDate"][::1], rotation=45)
plt.grid(True)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.show()


# Plot: Top 10 locations
location_counts = bank['CustLocation'].value_counts()
top_locations = location_counts.head(15)
plt.figure(figsize=(10, 6))
top_locations.plot(kind='bar', color='skyblue')
plt.title("Top 15 Customer Locations")
plt.xlabel("Location")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot: CUSTOMER LOCATION BASED ON THEIR TRANSACTION AMOUNT
location_data = bank.groupby("CustLocation")["TransactionAmount (INR)"].sum().sort_values(ascending=False).reset_index()
top10 = location_data.head(10)
plt.figure(figsize=(12,8))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
sns.barplot( x = 'CustLocation', y = 'TransactionAmount (INR)', data=top10, color='green')
plt.title('top 10 location')
plt.xlabel('Location')
plt.ylabel('Transaction Amount (INR)')
plt.show()

# Save cleaned data
data.to_csv("../output/cleaned_data.csv", index=False)