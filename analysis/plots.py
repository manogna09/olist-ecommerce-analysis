
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/olist_orders_dataset.csv', parse_dates=['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = df.groupby('month').size()

# Plot monthly order count
monthly_sales.plot(kind='bar', figsize=(12, 6), title='Monthly Order Volume')
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
