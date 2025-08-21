from database import Database

with Database() as db:
    products = db.get_all_products()
    print(products)