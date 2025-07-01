# 📊 Oracle-Based Supply Chain Data Management & Analytics System

This project implements a complete backend utility system for managing and analyzing a **Supply Chain Database** using **Oracle SQL** and **Python (cx_Oracle)**. It includes data insertion, retrieval, and advanced analytical queries—ideal for data-driven dashboards or enterprise ERP systems.

---

## 📂 Project Overview

The database models a supply chain workflow including:
- Suppliers and the products they offer
- Manufacturers and inventory tracking
- Customers and their purchase behaviors
- Orders, shipments, and returns
- Analytical queries for business insights

Python scripts connect to an Oracle Database to perform CRUD operations and execute analytical SQL queries.

---

## 🧱 Database Schema

The system consists of the following interrelated tables:

### 1. `SUPPLIER`
| Column Name   | Type         | Description                      |
|---------------|--------------|----------------------------------|
| SUPPLIER_ID   | NUMBER (PK)  | Unique ID for each supplier      |
| NAME          | VARCHAR2(50) | Supplier name                    |
| ADDRESS       | VARCHAR2(250)| Supplier address                 |
| PHONE_NO      | NUMBER(10)   | Contact number                   |
| EMAIL         | VARCHAR2(50) | Email ID                         |

---

### 2. `SUPPLIER_PRODUCTS`
| Column Name       | Type          | Description                              |
|-------------------|---------------|------------------------------------------|
| SUPPLIER_ID       | NUMBER (FK)   | Linked to `SUPPLIER`                     |
| PRODUCTS_SUPPLIED | VARCHAR2(100) | List of products the supplier provides   |

---

### 3. `MANUFACTURER`
| Column Name   | Type         | Description                       |
|---------------|--------------|-----------------------------------|
| MANUFACTURER_ID | NUMBER (PK)| Unique manufacturer ID            |
| NAME          | VARCHAR2(50) | Manufacturer name                 |
| ADDRESS       | VARCHAR2(250)| Location/address                  |
| PHONE_NO      | NUMBER(10)   | Contact number                    |
| EMAIL         | VARCHAR2(50) | Email ID                          |

---

### 4. `INVENTORY`
| Column Name   | Type         | Description                       |
|---------------|--------------|-----------------------------------|
| INVENTORY_ID  | NUMBER (PK)  | Unique inventory item ID          |
| QUANTITY      | NUMBER       | Units available                   |
| LAST_UPDATED  | DATE         | Last update timestamp             |

---

### 5. `PRODUCT`
| Column Name     | Type            | Description                          |
|-----------------|-----------------|--------------------------------------|
| PRODUCT_ID      | NUMBER (PK)     | Unique product ID                    |
| MANUFACTURER_ID | NUMBER (FK)     | Links to `MANUFACTURER`              |
| INVENTORY_ID    | NUMBER (FK)     | Links to `INVENTORY`                 |
| NAME            | VARCHAR2(50)    | Product name                         |
| CATEGORY        | VARCHAR2(100)   | Product category                     |
| PRICE           | NUMBER(10,2)    | Price per unit                       |

---

### 6. `CUSTOMER`
| Column Name   | Type          | Description                       |
|---------------|---------------|-----------------------------------|
| CUSTOMER_ID   | NUMBER (PK)   | Unique customer ID                |
| NAME          | VARCHAR2(100) | Customer full name                |
| ADDRESS       | VARCHAR2(100) | Address/location                  |
| PHONE_NO      | NUMBER(10)    | Phone number                      |
| EMAIL         | VARCHAR2(100) | Email ID                          |

---

### 7. `CUSTOMER_ORDERS`
| Column Name    | Type          | Description                    |
|----------------|---------------|--------------------------------|
| CUSTOMER_ID    | NUMBER (PK)   | Links to `CUSTOMER`           |
| ORDERS_PLACED  | VARCHAR2(100) | Description of orders placed  |

---

### 8. `PURCHASE_ORDER`
| Column Name       | Type         | Description                          |
|-------------------|--------------|--------------------------------------|
| PURCHASE_ORDER_ID | NUMBER (PK)  | Unique purchase order ID             |
| CUSTOMER_ID       | NUMBER (FK)  | Links to `CUSTOMER`                  |
| QUANTITY          | NUMBER       | Quantity ordered                     |
| ORDER_DATE        | DATE         | Date of order                        |

---

### 9. `SHIPMENT`
| Column Name     | Type         | Description                          |
|-----------------|--------------|--------------------------------------|
| SHIPMENT_ID     | NUMBER (PK)  | Unique shipment ID                   |
| SHIPPED_ORDER_ID| NUMBER (FK)  | Links to `PURCHASE_ORDER`            |
| DISPATCH_DATE   | DATE         | Date of dispatch                     |
| DELIVERY_DATE   | DATE         | Estimated delivery date              |
| STATUS          | VARCHAR2(100)| Current status of shipment           |

---

### 10. `RETURN_ORDER`
| Column Name   | Type         | Description                          |
|---------------|--------------|--------------------------------------|
| RORDER_ID     | NUMBER (FK)  | Related order                        |
| RETURN_ID     | NUMBER (PK)  | Unique return order ID               |
| RETURN_DATE   | DATE         | Date the item was returned           |
| REASON        | VARCHAR2(100)| Reason for return                    |
| STATUS        | VARCHAR2(100)| Return status                        |

---

### 11. `ORDERS`
| Column Name   | Type           | Description                     |
|---------------|----------------|---------------------------------|
| ORDER_ID      | NUMBER (PK)    | Unique order ID                 |
| ORDER_DATE    | DATE           | Date of order                   |
| EXPECTED_DATE | DATE           | Estimated delivery date         |
| SUPPLIER_ID   | NUMBER (FK)    | Linked to `SUPPLIER`            |
| STATUS        | VARCHAR2(255)  | Status of the order             |

---

## ⚙️ Features

✅ Modular Python functions for:
- Inserting and retrieving data from all major tables  
- Executing advanced SQL-based analytical queries  

✅ Analytical Functions:
- 🧮 Product counts per supplier  
- 📦 Inventory stock classification (Low/Medium/High)  
- 🧾 Top 10 customers by purchase volume  
- 📈 Average product price per category  
- 🚚 Shipment delivery durations  
- 🔄 Return rate summaries grouped by status  

---

## 📊 Analytics Use Cases

- **Supplier Performance**: Analyze which suppliers contribute the most to product distribution  
- **Inventory Management**: Detect low-stock items proactively  
- **Customer Engagement**: Discover your most active customers  
- **Order Trends**: Track order frequencies, delays, and return rates over time  
- **Category Pricing**: Understand pricing trends across different product categories  

---

## 🔐 Security Best Practices

Make sure to use environment variables or a `.env` file to store your database credentials:

## 🚀 How to Run

1. Clone this repository  
2. Install dependencies:  
   ```bash
   pip install cx_Oracle python-dotenv
