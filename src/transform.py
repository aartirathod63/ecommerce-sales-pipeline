import pandas as pd


def transform_data(customers, orders, products):

    # -------------------------
    # 1. Remove duplicate rows
    # -------------------------
    customers = customers.drop_duplicates()
    orders = orders.drop_duplicates()
    products = products.drop_duplicates()

    # -------------------------
    # 2. Handle missing values
    # -------------------------
    customers = customers.dropna()
    orders = orders.dropna()
    products = products.dropna()

    # -------------------------
    # 3. Clean column names
    # -------------------------
    customers.columns = customers.columns.str.strip().str.lower()
    orders.columns = orders.columns.str.strip().str.lower()
    products.columns = products.columns.str.strip().str.lower()

    # -------------------------
    # 4. Remove leading/trailing spaces
    # -------------------------
    for df in [customers, orders, products]:
        for column in df.select_dtypes(include="object").columns:
            df[column] = df[column].str.strip()

    print("Data transformation completed.")

    print(f"Customers after cleaning: {len(customers)} rows")
    print(f"Orders after cleaning: {len(orders)} rows")
    print(f"Products after cleaning: {len(products)} rows")

    return customers, orders, products


if __name__ == "__main__":
    print("Transform module loaded successfully.")
