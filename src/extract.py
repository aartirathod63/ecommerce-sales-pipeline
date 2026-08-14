import pandas as pd


def extract_data():
    customers = pd.read_csv("data/customers.csv")
    orders = pd.read_csv("data/orders.csv")
    products = pd.read_csv("data/products.csv")

    print("Data extraction completed.")
    print(f"Customers: {len(customers)} rows")
    print(f"Orders: {len(orders)} rows")
    print(f"Products: {len(products)} rows")

    return customers, orders, products


if __name__ == "__main__":
    extract_data()
