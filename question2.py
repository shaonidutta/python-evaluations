# product inventory

class Product:
    def __init__(self,name, price, quatity):
        self.name = name
        self.price = price
        self.quantity = quatity

    def __str__(self):
        return f"Product name: {self.name}, Price: {self.price}, Quatity: {self.quantity}"
    
    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("only merge same Product objects")
        if self.name.lower() != other.name.lower:
            raise TypeError("Cannot merge product with different names")
        total_quantity = self.quantity + other.quantity
        avg_price = (self.price*self.quantity)+ (other.price * other.quantity) / total_quantity
        return Product(self.name, total_quantity, avg_price)
    
    def __it__(self, other):
        return self.price < other.price
    

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for i, existing_product in enumerate(self.products):
            if existing_product.name.lower() == product.name.lower():
                self.products[i] = existing_product + product
                break
            else:
                self.products.append(product)

    def __len__(self):
        return len(self.products)
    
    def __getitem__(self, index):
        return self.products[index]
    
    def search_by_name(self, name):
        return [p for p in self.products if p.name.lower()==name.lower()]
    
if __name__ == "__main__":
    p1 = Product("Laptop", 80000, 8)
    p2 = Product("Laptop", 90000, 10)

    inventory = Inventory()
    inventory.add_product(p1)
    inventory.add_product(p2)

    # sorting
    # for p in sorted(inventory)

    #search
    search_results = inventory.search_by_name("laptop")
    for p in search_results:
        print(p)

    print(f"Total inventory value: {len(inventory)}")