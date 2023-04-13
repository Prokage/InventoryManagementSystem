# -*- coding: utf-8 -*-
"""
@author: Mayk Al-Ghrawi
"""

def add_product(conn, name, description, price, quantity):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES (?, ?, ?, ?)", (name, description, price, quantity))
    conn.commit()

def get_all_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def update_product(conn, id, name, description, price, quantity):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, description=?, price=?, quantity=? WHERE id=?", (name, description, price, quantity, id))
    conn.commit()

def delete_product(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()

def search_product_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()
