import mysql.connector, os
from mysql.connector import Error

class Database:
    def __init__(self, host="localhost", user="root", database="online_store"):
        self.host = host
        self.user = user
        self.database = database
        self.password = os.environ.get("SQL_PASSWORD")
        self.connection = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("✅ Connected to MySQL database")
            return self
        except Error as e:
            print(f"❌ Connection error: {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✅ Connection closed")

    # region Product CRUD operations

    def insert_product(self, department_id, name, price):
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO products (department_id, name, price) VALUES (%s, %s, %s)"
                cursor.execute(query, (department_id, name, price))
                self.connection.commit()
                print("Success! The product was added!!!")
        except Error as e:
            print(f"ERROR! Could not insert product!!!\nError: {e}")

    def get_all_products(self):
        products = []
        try:
            with self.connection.cursor(dictionary = True) as cursor: #<--- Setting dictionary = True will add the results into a dictionary instead of a tuple
                query = "SELECT * FROM products"
                cursor.execute(query)
                products = cursor.fetchall()
        except Error as e:
            print(f"ERROR! Could not get all users!\nError: {e}")
        
        return products
    # endregion
