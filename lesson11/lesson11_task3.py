from prettytable import PrettyTable


class Product:

    def __init__(self, l_type, l_name, l_price):
        self.type = l_type
        self.name = l_name
        self.price = l_price


class ProductStore:
    products = []
    income = 0

    def __init__(self):
        pass

    @staticmethod
    def check(prod_name, list_local):
        if prod_name not in list_local:
            print("There is no such product")

    def add(self, product, q):
        product.price = round(product.price * 1.3, 2)
        product.quantity = q
        self.products.append(product)

    def set_discount(self, identifier, percent, identifier_type="name"):
        if identifier_type == "name":
            for i in self.products:
                if i.name == f"{identifier}":
                    i.price *= 1 - percent / 100
        elif identifier_type == "type":
            for i in self.products:
                if i.type == f"{identifier}":
                    i.price *= 1 - percent / 100

    def sell_product(self, product_name, amount):
        for i in self.products:
            if i.name == product_name:
                if i.quantity >= amount:
                    i.quantity -= amount
                    self.income += i.price * amount
                else:
                    print("There is no such quantity of goods in stock")

    def get_income(self):
        print(self.income)

    def get_all_products(self):
        x = PrettyTable(["Type", "Name", "Price", "Quantity"])
        for i in self.products:
            x.add_row([i.type, i.name, i.price, i.quantity])
        print(x)

    def get_product_info(self, product_name):
        for i in self.products:
            if product_name == i.name:
                print((i.name, i.quantity))


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)


s.get_all_products()

