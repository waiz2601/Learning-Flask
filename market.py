from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')  # Render home.html instead of base.html

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = [
        {"id": 1, "name": "Wireless Mouse", "barcode": "123456789012", "phone_number": "9876543210", "price": 599.99},
        {"id": 2, "name": "Bluetooth Speaker", "barcode": "234567890123", "phone_number": "8765432109", "price": 1299.50},
        {"id": 3, "name": "USB Flash Drive", "barcode": "345678901234", "phone_number": "7654321098", "price": 499.00},
        {"id": 4, "name": "Gaming Keyboard", "barcode": "456789012345", "phone_number": "6543210987", "price": 2499.75}
    ]
    return render_template('market.html', item_name=items)

@app.route('/product/<int:item_id>')
def product_info(item_id):
    return f"<h1>More details about Product ID: {item_id}</h1>"

@app.route('/purchase/<int:item_id>')
def purchase(item_id):
    return f"<h1>Purchase Page for Product ID: {item_id}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
