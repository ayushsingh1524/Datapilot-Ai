SCHEMA_DOCUMENTS = [
    """
Table: orders

Purpose:
Stores customer order and sales information.

Columns:
order_id: Unique identifier for each order.
customer_id: Unique identifier for the customer.
product: Name of the purchased product.
category: Product category.
price: Price of one unit in Indian Rupees.
quantity: Number of units purchased.
order_date: Date when the order was placed.
region: Customer's geographical region.
payment_method: Payment method used for the order.
total_amount: Total value of the order.
""",

    """
Revenue Business Rules

Revenue should normally be calculated using total_amount.

Revenue by product should use:
GROUP BY product

Revenue by region should use:
GROUP BY region

Daily revenue should use:
GROUP BY order_date
""",

    """
Order Analytics Rules

Total orders should be calculated using:
COUNT(order_id)

Average order value should be calculated using:
AVG(total_amount)

The total_amount column is calculated as:
price multiplied by quantity.
""",
]