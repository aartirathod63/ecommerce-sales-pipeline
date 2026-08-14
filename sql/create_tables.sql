CREATE DATABASE IF NOT EXISTS ecommerce_sales_pipeline;

USE ecommerce_sales_pipeline;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100),
    signup_date DATE,
    PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2),
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_date DATE,
    quantity INT,
    price DECIMAL(10,2),
    PRIMARY KEY (order_id),

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_orders_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE INDEX idx_orders_customer
    ON orders(customer_id);

CREATE INDEX idx_orders_product
    ON orders(product_id);

CREATE INDEX idx_orders_date
    ON orders(order_date);
