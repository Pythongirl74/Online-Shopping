class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class ProductManager:
    def __init__(self):
        self.products = []

    def load_products_from_file(self, filename):
        print("Loading product data from file...")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    product = Product(int(data[0]), data[1], float(data[2]), data[3])
                    self.products.append(product)
        except FileNotFoundError:
            print("Error: File not found.")
            return
        print(f"Successfully loaded {len(self.products)} products.")


    def insert_product(self, id, name, price, category):
        product = Product(id, name, price, category)
        self.products.append(product)
        print(f"Product '{name}' with ID {id} inserted successfully.")

    def update_product(self, id, name=None, price=None, category=None):
        for product in self.products:
            if product.id == id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if category:
                    product.category = category
                print(f"Product with ID {id} updated successfully.")
                return
        print(f"Error: Product with ID {id} not found.")

    def delete_product(self, id):
        initial_length = len(self.products)
        self.products = [product for product in self.products if product.id != id]
        if len(self.products) < initial_length:
            print(f"Product with ID {id} deleted successfully.")
        else:
            print(f"Error: Product with ID {id} not found.")

    def search_product_by_id(self, id):
         print(f"Searching for product with ID: {id}")
         for product in self.products:
            if product.id == id:
                print(f"Product found: {product.name} (ID: {product.id}, Price: {product.price}, Category: {product.category})")
                return product
         print("Product not found.")
         return None  

    def search_product_by_name(self, name):
        result = []
        for product in self.products:
            if name.lower() in product.name.lower():
                result.append(product)
        return result

    def bubble_sort_by_price(self):
        n = len(self.products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.products[j].price > self.products[j + 1].price:
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]
        print("Products sorted by price:")
        for product in self.products:
            print(f"{product.name} - Price: {product.price}")

#LOADING PRODUCTS FROM FILE:
manager = ProductManager()
manager.load_products_from_file('product_data.txt')

# INSERTING A NEW PRODUCT:
manager.insert_product(101, 'Bubbles', 29.99, "Children's Toys")

# UPDATING A PRODUCT:
manager.update_product(101, name='Updated Product', price=39.99)

# DELETING A PRODUCT:
manager.delete_product(101)

# SEARCHING FOR A PRODUCT BY ID:
result = manager.search_product_by_id(101)
if result:
    print("Product found:", result.name)
else:
    print("Product not found")

#BUBBLE SORT BY PRICE:
manager.bubble_sort_by_price()
for product in manager.products:
    print(product.name, product.price)
