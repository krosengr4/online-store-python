from database import Database
from models import Product

with Database() as db:
    products = db.get_all_products()
    for product in products:
        product.print_data()