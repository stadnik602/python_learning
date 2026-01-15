class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items

order = Order("Tom Holland", ["beer", "chicken strips", "nuts", "toilet paper"])
items_list = ""

for item in order.items:
    items_list += item + ", "

print("Order for", order.customer_name + ":", items_list.rstrip(", ") + ".")
# print("Order for", order.customer_name + ":", items_list[:-2] + ".")

