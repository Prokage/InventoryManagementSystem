# -*- coding: utf-8 -*-
"""
@author: Mayk Al-Ghrawi
"""

import sqlite3

def create_connection():
    conn = sqlite3.connect('inventory.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL
                      );''')
    conn.commit()

if __name__ == "__main__":
    connection = create_connection()
    create_table(connection)
    connection.close()
