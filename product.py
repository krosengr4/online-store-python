class Product:
    def __init__(self, name, price, product_id = None, department_id = None):
        self.product_id = product_id
        self.department_id = department_id
        self.name = name
        self.price = price

    def print_data(self):
        print("\n---PRODUCT---")
        print("Product ID:", self.product_id)
        print("Department ID:", self.department_id)
        print("Name:", self.name)
        print(f"Price: ${self.price:,.2f}")
        print('-------------------------------')
