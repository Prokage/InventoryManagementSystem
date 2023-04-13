# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:03:37 2023

@author: Mayk Al-Ghrawi
"""

from flask import Flask, render_template, request, redirect, url_for, g
from database import create_connection, create_table
from inventory import add_product, get_all_products, update_product, delete_product, search_product_by_name


app = Flask(__name__)

def get_conn():
    if "conn" not in g:
        g.conn = create_connection()
        create_table(g.conn)  # create 'products' table if it doesn't exist.
    return g.conn

@app.teardown_appcontext
def close_conn(error):
    if "conn" in g:
        g.conn.close()


@app.route('/')
def index():
    products = get_all_products(get_conn())
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    add_product(get_conn(), name, description, price, quantity)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    update_product(get_conn(), id, name, description, price, quantity)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_product(get_conn(), id)
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('query', '')
    products = search_product_by_name(get_conn(), query)
    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)

