# Inventory and Sales Management System (Python)

## Description
This is a simple **inventory and sales management system written in Python** that runs in the console.  
The program allows a user to:

- Add products to an inventory
- Sell products
- View the sales history
- Calculate total money earned from sales
- View the current inventory

The program uses basic Python concepts such as:
- Lists
- Dictionaries
- Functions
- Loops
- Exception handling
- User input

It is designed as a simple practice project for beginners learning Python.

---

## How the Program Works

The system maintains two main lists:

- `inventory`: Stores all products available in the system.
- `sales_history`: Stores the history of all completed sales.

Each **product** is stored as a dictionary with:

```python
{
 "name": product_name,
 "price": product_price,
 "quantity": product_quantity
}