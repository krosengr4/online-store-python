from database import Database
from product import Product

with Database() as db:
    products = db.get_all_products()
    for product in products:
        product.print_data()