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
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(int(data[0]), data[1], float(data[2]), data[3])
                self.products.append(product)

    def insert_product(self, id, name, price, category):
        product = Product(id, name, price, category)
        self.products.append(product)

    def update_product(self, id, name=None, price=None, category=None):
        for product in self.products:
            if product.id == id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if category:
                    product.category = category
                break

    def delete_product(self, id):
        self.products = [product for product in self.products if product.id != id]

    def search_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
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

# Example usage:
manager = ProductManager()
manager.load_products_from_file('product_data.txt')

# Insert a new product
manager.insert_product(101, 'New Product', 29.99, 'New Category')

# Update an existing product
manager.update_product(101, name='Updated Product', price=39.99)

# Delete a product
manager.delete_product(101)

# Search for a product
result = manager.search_product_by_id(100)
if result:
    print("Product found:", result.name)
else:
    print("Product not found")

# Bubble sort products by price
manager.bubble_sort_by_price()
for product in manager.products:
    print(product.name, product.price)
