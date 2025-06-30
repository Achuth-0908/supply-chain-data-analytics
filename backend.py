import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv() 

def get_connection():
    try:
        connection = cx_Oracle.connect(
            user=os.getenv("ORACLE_USER"),
            password=os.getenv("ORACLE_PASSWORD"),
            dsn=os.getenv("ORACLE_DSN")
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Connection Error:", e)
        return None

def close_connection(connection):
    if connection:
        connection.close()

def insert_supplier(supplier_id, name, address, phone_no, email):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO SUPPLIER (SUPPLIER_ID, NAME, ADDRESS, PHONE_NO, EMAIL)
        VALUES (:1, :2, :3, :4, :5)
    """
    try:
        cursor.execute(query, (supplier_id, name, address, phone_no, email))
        connection.commit()
    except cx_Oracle.DatabaseError as e:
        print("Insert Supplier Error:", e)
    finally:
        cursor.close()
        close_connection(connection)

def get_suppliers():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM SUPPLIER"
    try:
        cursor.execute(query)
        suppliers = cursor.fetchall()
        return suppliers
    except cx_Oracle.DatabaseError as e:
        print("Get Suppliers Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def insert_supplier_product(supplier_id, products_supplied):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO SUPPLIER_PRODUCTS (SUPPLIER_ID, PRODUCTS_SUPPLIED)
        VALUES (:1, :2)
    """
    try:
        cursor.execute(query, (supplier_id, products_supplied))
        connection.commit()
    except cx_Oracle.DatabaseError as e:
        print("Insert Supplier Product Error:", e)
    finally:
        cursor.close()
        close_connection(connection)

def get_supplier_products():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM SUPPLIER_PRODUCTS"
    try:
        cursor.execute(query)
        supplier_products = cursor.fetchall()
        return supplier_products
    except cx_Oracle.DatabaseError as e:
        print("Get Supplier Products Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def insert_manufacturer(manufacturer_id, name, address, phone_no, email):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO MANUFACTURER (MANUFACTURER_ID, NAME, ADDRESS, PHONE_NO, EMAIL)
        VALUES (:1, :2, :3, :4, :5)
    """
    try:
        cursor.execute(query, (manufacturer_id, name, address, phone_no, email))
        connection.commit()
    except cx_Oracle.DatabaseError as e:
        print("Insert Manufacturer Error:", e)
    finally:
        cursor.close()
        close_connection(connection)

def get_manufacturers():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM MANUFACTURER"
    try:
        cursor.execute(query)
        manufacturers = cursor.fetchall()
        return manufacturers
    except cx_Oracle.DatabaseError as e:
        print("Get Manufacturers Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def insert_customer(customer_id, name, address, phone_no, email):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO CUSTOMER (CUSTOMER_ID, NAME, ADDRESS, PHONE_NO, EMAIL)
        VALUES (:1, :2, :3, :4, :5)
    """
    try:
        cursor.execute(query, (customer_id, name, address, phone_no, email))
        connection.commit()
    except cx_Oracle.DatabaseError as e:
        print("Insert Customer Error:", e)
    finally:
        cursor.close()
        close_connection(connection)

def get_customers():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM CUSTOMER"
    try:
        cursor.execute(query)
        customers = cursor.fetchall()
        return customers
    except cx_Oracle.DatabaseError as e:
        print("Get Customers Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

# Additional Analytics SQL Views/Queries

def get_supplier_product_count():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT s.NAME, COUNT(sp.PRODUCTS_SUPPLIED) AS product_count
        FROM SUPPLIER s
        JOIN SUPPLIER_PRODUCTS sp ON s.SUPPLIER_ID = sp.SUPPLIER_ID
        GROUP BY s.NAME
        ORDER BY product_count DESC
    """
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except cx_Oracle.DatabaseError as e:
        print("Supplier Product Count Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def get_top_customers_by_order_volume():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT c.NAME, COUNT(p.PURCHASE_ORDER_ID) AS total_orders
        FROM CUSTOMER c
        JOIN PURCHASE_ORDER p ON c.CUSTOMER_ID = p.CUSTOMER_ID
        GROUP BY c.NAME
        ORDER BY total_orders DESC FETCH FIRST 10 ROWS ONLY
    """
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except cx_Oracle.DatabaseError as e:
        print("Top Customers Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def get_average_product_price_by_category():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT CATEGORY, AVG(PRICE) AS avg_price
        FROM PRODUCT
        GROUP BY CATEGORY
        ORDER BY avg_price DESC
    """
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except cx_Oracle.DatabaseError as e:
        print("Average Product Price Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def get_inventory_status():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT INVENTORY_ID, QUANTITY,
               CASE 
                   WHEN QUANTITY > 100 THEN 'HIGH'
                   WHEN QUANTITY BETWEEN 51 AND 100 THEN 'MEDIUM'
                   ELSE 'LOW'
               END AS STOCK_LEVEL
        FROM INVENTORY
        ORDER BY INVENTORY_ID
    """
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        print("Inventory Status Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def get_shipment_delivery_times():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT SHIPMENT_ID, DISPATCH_DATE, DELIVERY_DATE,
               DELIVERY_DATE - DISPATCH_DATE AS DELIVERY_DURATION
        FROM SHIPMENT
        ORDER BY DELIVERY_DURATION DESC
    """
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        print("Shipment Delivery Times Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)

def get_return_rate_by_status():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT STATUS, COUNT(*) AS return_count
        FROM RETURN_ORDER
        GROUP BY STATUS
        ORDER BY return_count DESC
    """
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        print("Return Rate Error:", e)
        return None
    finally:
        cursor.close()
        close_connection(connection)
