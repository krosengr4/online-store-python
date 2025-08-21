from database import Database
from models import Product, Department

with Database() as db:
    products = db.get_all_products()
    for product in products:
        product.print_data()

    departments = db.get_all_departments()
    for department in departments:
        department.print_data()