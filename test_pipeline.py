from src.extract import extract_data
from src.transform import transform_data


customers, orders, products = extract_data()

customers, orders, products = transform_data(
    customers,
    orders,
    products
)

print("\nPipeline test completed successfully.")
