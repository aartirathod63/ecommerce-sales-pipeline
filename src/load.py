import pandas as pd
import mysql.connector


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": “Aarti@123”,
    "database": "ecommerce_sales_pipeline"
}


def load_data(customers, products, orders):

    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Load customers
    customer_query = """
        INSERT INTO customers
        (customer_id, customer_name, city, state, signup_date)
        VALUES (%s, %s, %s, %s, %s)
    """

    customer_data = [
        tuple(row)
        for row in customers[
            [
                "customer_id",
                "customer_name",
                "city",
                "state",
                "signup_date"
            ]
        ].itertuples(index=False, name=None)
    ]

    cursor.executemany(customer_query, customer_data)

    # Load products
    product_query = """
        INSERT INTO products
        (product_id, product_name, category, price)
        VALUES (%s, %s, %s, %s)
    """

    product_data = [
        tuple(row)
        for row in products[
            [
                "product_id",
                "product_name",
                "category",
                "price"
            ]
        ].itertuples(index=False, name=None)
    ]

    cursor.executemany(product_query, product_data)

    # Load orders
    order_query = """
        INSERT INTO orders
        (order_id, customer_id, product_id, order_date, quantity, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    order_data = [
        tuple(row)
        for row in orders[
            [
                "order_id",
                "customer_id",
                "product_id",
                "order_date",
                "quantity",
                "price"
            ]
        ].itertuples(index=False, name=None)
    ]

    cursor.executemany(order_query, order_data)

    connection.commit()

    print(f"Loaded {len(customers)} customers")
    print(f"Loaded {len(products)} products")
    print(f"Loaded {len(orders)} orders")

    cursor.close()
    connection.close()

    print("Data loading completed successfully.")


if __name__ == "__main__":
    print("Load module loaded successfully.")
