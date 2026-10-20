# ===== Exercise_2.py =====
# Exercise 2: Advanced Data Manipulation and Analysis
#
# What you learn here:
#   - A list of dictionaries (looping and reading keys)
#   - Adding up totals in a dictionary (if key in dict ... else ...)
#   - Adding a new key to each dictionary
#   - List comprehension with a condition, sorting with key=
#   - Counting with a dictionary, max()
#
# Instructions:
#   In this exercise, you will analyze data from a hypothetical online retail
#   company to gain insights into sales trends and customer behavior. The data
#   is represented as a list of dictionaries, where each dictionary contains
#   information about a single purchase.
#
# Data: sales_data (see the list below), each purchase has customer_id,
#   product, price, quantity and date.
#
# Tasks:
#   1. Total Sales Calculation:
#      Calculate the total sales for each product category (i.e., the total
#      revenue generated from each type of product). Use a loop to iterate
#      through the data and a dictionary to store the total sales for each
#      product.
#   2. Customer Spending Profile:
#      Determine the total amount spent by each customer. Use a dictionary to
#      keep the total spent per customer.
#   3. Sales Data Enhancement:
#      Add a new key "total_price" to each transaction (price * quantity),
#      so the data holds this new information.
#   4. High-Value Transactions:
#      - Using list comprehension, create a list of all transactions where
#        the total price is greater than $500.
#      - Sort this list by the total price in descending order.
#   5. Customer Loyalty Identification:
#      - Identify any customer who has made more than one purchase,
#        suggesting potential loyalty.
#      - Use a dictionary to count purchases per customer, then use a loop or
#        comprehension to identify customers meeting the loyalty criterion.
#
# Bonus: Insights and Analysis:
#   - Calculate the average transaction value for each product category.
#   - Identify the most popular product based on the quantity sold.
#   - Provide insights into how these analyses could inform the company's
#     marketing strategies.

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# 1. Total Sales Calculation
total_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    total_price = transaction["price"] * transaction["quantity"]
    if product in total_sales:
        total_sales[product] += total_price
    else:
        total_sales[product] = total_price

# 2. Customer Spending Profile
customer_spending = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    total_price = transaction["price"] * transaction["quantity"]
    if customer_id in customer_spending:
        customer_spending[customer_id] += total_price
    else:
        customer_spending[customer_id] = total_price

# 3. Sales Data Enhancement
for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

# 4. High-Value Transactions
high_value_transactions = [transaction for transaction in sales_data if transaction["total_price"] > 500]
high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)

# 5. Customer Loyalty Identification (more than one purchase)
purchase_counts = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    if customer_id in purchase_counts:
        purchase_counts[customer_id] += 1
    else:
        purchase_counts[customer_id] = 1
loyal_customers = [customer_id for customer_id, count in purchase_counts.items() if count > 1]

print("Total Sales:", total_sales)
print("Customer Spending:", customer_spending)
print("First Two Sales Data Entries:", sales_data[:2])
print("High-Value Transactions:", high_value_transactions)
print("Loyal Customers:", loyal_customers)

# Bonus: Insights and Analysis

# Average transaction value for each product category
average_transaction_value = {}
for product in total_sales.keys():
    total_quantity = sum(transaction["quantity"] for transaction in sales_data if transaction["product"] == product)
    average_transaction_value[product] = total_sales[product] / total_quantity

# Most popular product based on the quantity sold
product_quantities = {product: sum(transaction["quantity"] for transaction in sales_data if transaction["product"] == product) for product in set(transaction["product"] for transaction in sales_data)}
most_popular_product = max(product_quantities, key=product_quantities.get)

"""
Insights:
1. Products with higher average transaction values might indicate premium pricing or higher-end products. Marketing could highlight the quality and features of these products to attract customers willing to pay more.

2. The most popular product, based on quantity sold, shows consumer preference and demand. Marketing could promote it more, bundle it with other products, or upsell customers to higher-value related items.

3. Knowing both the average transaction value and the most popular products helps with inventory management, targeted advertising, and promotions for specific product categories.
"""

print("Average Transaction Value:", average_transaction_value)
print("Most Popular Product:", most_popular_product)
