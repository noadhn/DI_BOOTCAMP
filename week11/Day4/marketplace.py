from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('market_homepage.html')


@app.route('/products')
def show_products():
    with open("product_db.json", 'r') as products:
        products = json.load(products)
    return render_template('market_products.html', products=products)


@app.route('/products/<product_id>')
def show_products_details(product_id):
    with open("product_db.json", 'r') as products:
        products = json.load(products)
    for each in products:
        if each['ProductId'] == product_id:
            product = each
            product_id = product['ProductId']
    return render_template('market_products_details.html', product=product, product_id=product_id)


if __name__ == '__main__':
    app.run(debug=True)
