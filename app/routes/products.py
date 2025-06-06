from flask import render_template, Blueprint, session
import requests

products_bp = Blueprint('products', __name__, template_folder='../templates')


@products_bp.route('/')
def products():
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()

    response = {
        "status": "success",
        "products": products,
        "user": session['actual_user']
    }

    return render_template('index.html', data = response)