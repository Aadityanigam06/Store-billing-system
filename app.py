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
