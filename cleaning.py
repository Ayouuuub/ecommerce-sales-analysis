# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load dataset
df = pd.read_csv("cleaned_to_Valid_Transactions.csv", encoding="ISO-8859-1")

'''
# Remove duplicates 
 df_no_duplicates = df.drop_duplicates()

#Handle Missing Values
df = df.dropna(subset=['CustomerID'])


# Convert InvoiceDate to DateTime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Extract useful time features
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['MonthName'] = df['InvoiceDate'].dt.strftime('%b-%Y')
df['Weekday'] = df['InvoiceDate'].dt.day_name()

# Create Revenue Column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Remove negative quantities (returns/cancellations)
df = df[df['Quantity'] > 0]

# Optional: remove transactions with 0 or negative prices
df = df[df['UnitPrice'] > 0]
df.to_csv('cleaned_to_Valid_Transactions.csv', index=False)


print(df.shape)
print(df.isnull().sum())
print(df.describe())
'''


# Set style for visuals
sns.set(style="whitegrid", palette="muted")

weekday_sales = df.groupby('Weekday')['Revenue'].sum().reindex([
    "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
])

plt.figure(figsize=(10,6))
sns.barplot(x=weekday_sales.index, y=weekday_sales.values, palette="Set2")
plt.title("Revenue by Day of the Week", fontsize=16)
plt.xlabel("Day of Week")
plt.ylabel("Revenue")
plt.show()





