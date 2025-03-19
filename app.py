<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rain",
    database="cloth_store"
)
cursor = db.cursor()

@app.route('/')
def home():
    return "Welcome to the Cloth Store Management System!"

# Route to add a customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    cursor.execute("INSERT INTO Customer (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    db.commit()
    return jsonify({"message": "Customer added successfully!"})

# Route to add an order
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    cursor.execute("INSERT INTO Orders (customer_id, employee_id) VALUES (%s, %s)", 
                   (data['customer_id'], data['employee_id']))
    db.commit()
    return jsonify({"message": "Order placed successfully!"})

# Route to get products
@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()
    return jsonify(products)

# Route to add a product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category_id = request.form['category_id']

        cursor.execute("INSERT INTO Product (name, price, category_id) VALUES (%s, %s, %s)", 
                       (name, price, category_id))
        db.commit()
        return redirect(url_for('get_products'))  # ✅ Fixed error here

    return render_template("add_product.html")  # ✅ Fixed error here

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rain",
    database="cloth_store"
)
cursor = db.cursor()

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    cursor.execute("INSERT INTO Customer (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    db.commit()
    return jsonify({"message": "Customer added successfully!"})

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    cursor.execute("INSERT INTO Orders (customer_id, employee_id) VALUES (%s, %s)", (data['customer_id'], data['employee_id']))
    db.commit()
    return jsonify({"message": "Order placed successfully!"})

@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 080fd517e4cc18cac75956d53d07939d82c20a39
