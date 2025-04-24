class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self):
        id = input("Item ID: ")
        name = input("Name: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))
        self.items[id] = {"name": name, "stock": stock, "price": price}

    def update_item(self):
        id = input("Item ID: ")
        if id in self.items:
            stock = int(input("New stock: "))
            price = float(input("New price: "))
            self.items[id].update({"stock": stock, "price": price})
        else:
            print("Item not found.")

    def check_item(self):
        id = input("Item ID: ")
        print(self.items.get(id, "Item not found."))

def main():
    inv = Inventory()
    while True:
        print("\n1.Add 2.Update 3.Check 4.Exit")
        ch = input("Choice: ")
        if ch == "1": inv.add_item()
        elif ch == "2": inv.update_item()
        elif ch == "3": inv.check_item()
        elif ch == "4": break
        else: print("Invalid!")

if __name__ == "__main__":
    main()
