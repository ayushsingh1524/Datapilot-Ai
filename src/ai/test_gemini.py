from src.ai.sql_generator import generate_sql
from src.ai.sql_validator import validate_sql
from src.database.queries import execute_query


schema = """
orders(
    order_id,
    customer_id,
    product,
    category,
    price,
    quantity,
    order_date,
    region,
    payment_method,
    total_amount
)
"""

question = "What is the total revenue by product?"

# 1. Generate SQL using Gemini
sql = generate_sql(question, schema)

print("\nGenerated SQL:")
print(sql)

# 2. Validate the AI-generated SQL
try:
    sql = validate_sql(sql)
    print("\nSQL validation passed.")

except ValueError as error:
    print(f"\nSQL validation failed: {error}")
    exit(1)

# 3. Execute only validated SQL
results = execute_query(sql)

print("\nQuery Results:")
for row in results:
    print(row)