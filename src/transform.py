import pandas as pd


def transform_data(customers, orders, products):

    # Remove duplicate records
    customers = customers.drop_duplicates()
    orders = orders.drop_duplicates()
    products = products.drop_duplicates()

    # Clean column names
    customers.columns = customers.columns.str.strip().str.lower()
    orders.columns = orders.columns.str.strip().str.lower()
    products.columns = products.columns.str.strip().str.lower()

    # Clean string columns
    for df in [customers, orders, products]:
        for column in df.select_dtypes(include="object").columns:
            df[column] = df[column].str.strip()

    # Convert dates
    customers["signup_date"] = pd.to_datetime(
        customers["signup_date"],
        errors="coerce"
    )

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    # Convert numeric columns
    customers["customer_id"] = pd.to_numeric(
        customers["customer_id"],
        errors="coerce"
    )

    orders["order_id"] = pd.to_numeric(
        orders["order_id"],
        errors="coerce"
    )

    orders["customer_id"] = pd.to_numeric(
        orders["customer_id"],
        errors="coerce"
    )

    orders["quantity"] = pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    )

    orders["price"] = pd.to_numeric(
        orders["price"],
        errors="coerce"
    )

    products["product_id"] = pd.to_numeric(
        products["product_id"],
        errors="coerce"
    )

    products["price"] = pd.to_numeric(
        products["price"],
        errors="coerce"
    )

    # Convert order product IDs such as P101 → 101
    # This keeps the raw CSV unchanged.
    orders["product_id"] = (
        orders["product_id"]
        .astype(str)
        .str.replace("P", "", regex=False)
    )

    orders["product_id"] = pd.to_numeric(
        orders["product_id"],
        errors="coerce"
    )

    # Remove records with invalid required fields
    customers = customers.dropna(
        subset=["customer_id", "signup_date"]
    )

    orders = orders.dropna(
        subset=[
            "order_id",
            "customer_id",
            "product_id",
            "order_date",
            "quantity",
            "price"
        ]
    )

    products = products.dropna(
        subset=["product_id", "price"]
    )

    print("Data transformation completed.")
    print(f"Customers: {len(customers)} rows")
    print(f"Orders: {len(orders)} rows")
    print(f"Products: {len(products)} rows")

    return customers, orders, products


if __name__ == "__main__":
    print("Transform module loaded successfully.")
