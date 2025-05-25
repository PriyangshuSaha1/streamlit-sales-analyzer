import streamlit as st
import pandas as pd

st.title("📊 Sales & Profit Analyzer")

# Input number of entries
n = st.number_input("How many entries do you want to add?", min_value=1, max_value=20, value=3)

# Collect dynamic input
entries = []
for i in range(n):
    st.subheader(f"Entry {i+1}")
    date = st.date_input(f"Order Date (Entry {i+1})", key=f"date_{i}")
    category = st.selectbox(f"Category (Entry {i+1})", ['Furniture', 'Office Supplies', 'Technology'], key=f"cat_{i}")
    sale = st.number_input(f"Sales Amount (Entry {i+1})", min_value=0.0, key=f"sale_{i}")
    profit = st.number_input(f"Profit Amount (Entry {i+1})", min_value=0.0, key=f"profit_{i}")
    entries.append({'Order Date': date, 'Category': category, 'Sales': sale, 'Profit': profit})

if st.button("Analyze"):
    df = pd.DataFrame(entries)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M')

    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    category_sales = df.groupby('Category')['Sales'].sum()
    monthly_sales = df.groupby('Month')['Sales'].sum()

    st.subheader("📋 Input Data")
    st.dataframe(df)

    st.subheader("📈 Total Sales & Profit")
    st.write(f"**Total Sales:** ${total_sales}")
    st.write(f"**Total Profit:** ${total_profit}")

    st.subheader("📊 Sales by Category")
    st.bar_chart(category_sales)

    st.subheader("🗓️ Monthly Sales")
    st.line_chart(monthly_sales)
