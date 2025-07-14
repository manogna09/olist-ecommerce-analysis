
import pandas as pd

# Load datasets
orders = pd.read_csv('../data/olist_orders_dataset.csv', parse_dates=['order_purchase_timestamp'])
items = pd.read_csv('../data/olist_order_items_dataset.csv')
payments = pd.read_csv('../data/olist_order_payments_dataset.csv')
reviews = pd.read_csv('../data/olist_order_reviews_dataset.csv')
products = pd.read_csv('../data/olist_products_dataset.csv')
customers = pd.read_csv('../data/olist_customers_dataset.csv')
translate = pd.read_csv('../data/product_category_name_translation.csv')

# Merge data
df = orders.merge(items, on='order_id') \
           .merge(payments, on='order_id') \
           .merge(reviews[['order_id', 'review_score']], on='order_id') \
           .merge(products, on='product_id') \
           .merge(translate, on='product_category_name', how='left') \
           .merge(customers[['order_id','customer_state']], on='order_id', how='left')

# Feature engineering
df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
df['delivery_time'] = (pd.to_datetime(df['order_delivered_customer_date']) - pd.to_datetime(df['order_purchase_timestamp'])).dt.days

# Basic insights
total_revenue = (df['price'] + df['freight_value']).sum()
avg_order_value = df.groupby('order_id')['price'].sum().mean()
monthly_sales = df.groupby('month')['price'].sum()
top_categories = df.groupby('product_category_name_english')['order_id'].nunique().sort_values(ascending=False).head(10)
least_categories = df.groupby('product_category_name_english')['order_id'].nunique().sort_values().head(10)
avg_review_score = df.groupby('product_category_name_english')['review_score'].mean().sort_values(ascending=False).head(10)
delivery_stats = df['delivery_time'].describe()
payment_methods = df['payment_type'].value_counts()
orders_by_state = df['customer_state'].value_counts()

# Print summaries
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Order Value: ${avg_order_value:.2f}\n")
print("Top Categories:\n", top_categories)
print("\nLeast Ordered Categories:\n", least_categories)
print("\nAverage Review Score by Category:\n", avg_review_score)
print("\nDelivery Time Statistics:\n", delivery_stats)
print("\nPayment Methods:\n", payment_methods)
print("\nOrders by State:\n", orders_by_state)
