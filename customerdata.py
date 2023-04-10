import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQL database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=<server_name>;DATABASE=<database_name>;UID=<username>;PWD=<password>')

# Load the customer sales data from the SQL view into a Pandas dataframe
query = "SELECT * FROM customer_sales_data"
df = pd.read_sql(query, conn)

# Aggregate and filter the data to identify key business insights
grouped_data = df.groupby(['customer_name', 'product_name'])['sales_amount'].sum().reset_index()
filtered_data = grouped_data[grouped_data['sales_amount'] > 10000]

# Visualize the data using a bar chart
plt.bar(filtered_data['product_name'], filtered_data['sales_amount'])
plt.xlabel('Product')
plt.ylabel('Sales Amount')
plt.title('Top Selling Products')
plt.show()
