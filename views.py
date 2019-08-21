from flask import Blueprint
from flask import render_template


products_app = Blueprint('products_app', __name__)


@products_app.route('/', endpoint='products')
def products_page():
    return render_template('products.html')


@products_app.route('/<int:product_id>', endpoint='product')
def product_page(product_id):
    return render_template('product.html', product_id=product_id)
