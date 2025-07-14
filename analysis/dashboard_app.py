
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
orders = pd.read_csv('../data/olist_orders_dataset.csv')
payments = pd.read_csv('../data/olist_order_payments_dataset.csv')
reviews = pd.read_csv('../data/olist_order_reviews_dataset.csv')

st.title("Olist E-commerce Dashboard")

# Order Status Distribution
st.subheader("Order Status Distribution")
order_counts = orders['order_status'].value_counts()
fig1, ax1 = plt.subplots()
order_counts.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Payment Method Distribution
st.subheader("Payment Methods Distribution")
pay_counts = payments['payment_type'].value_counts()
fig2, ax2 = plt.subplots()
pay_counts.plot(kind='bar', color='orange', ax=ax2)
st.pyplot(fig2)

# Review Sentiment (if exists)
st.subheader("Review Sentiment Distribution")
if 'sentiment' in reviews.columns:
    fig3, ax3 = plt.subplots()
    reviews['sentiment'].hist(bins=20, ax=ax3)
    ax3.set_title("Sentiment Polarity")
    st.pyplot(fig3)
else:
    st.info("Run sentiment analysis to generate 'sentiment' column.")
