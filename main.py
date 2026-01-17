class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        total = 0
        for i in self.items:
            total += i.price
        return total

    def show_order(self):
        for i in self.items:
            print(i.name, "-", i.price)


burger = MenuItem("Burger", 35000)
cola = MenuItem("Cola", 10000)

order = Order()
order.add_item(burger)
order.add_item(cola)

order.show_order()
print("Jami:", order.total_price(), "so‘m")
