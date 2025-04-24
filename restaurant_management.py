class Restaurant:
    def __init__(self):
        self.menu = {}
        self.tables = []
        self.orders = {}

    def add_item(self):
        name = input("Item name: ")
        price = float(input("Price: "))
        self.menu[name] = price

    def book_table(self):
        t = input("Table number: ")
        if t not in self.tables:
            self.tables.append(t)
        else:
            print("Already booked.")

    def take_order(self):
        t = input("Table number: ")
        if t not in self.tables:
            print("Not booked!")
            return
        item = input("Item name: ")
        if item not in self.menu:
            print("Not on menu.")
            return
        self.orders.setdefault(t, []).append(item)

    def print_data(self):
        print(f"Menu: {self.menu}\nTables: {self.tables}\nOrders: {self.orders}")

def main():
    r = Restaurant()
    while True:
        print("\n1.Add Item 2.Book Table 3.Take Order 4.Show Data 5.Exit")
        ch = input("Choice: ")
        if ch == "1": r.add_item()
        elif ch == "2": r.book_table()
        elif ch == "3": r.take_order()
        elif ch == "4": r.print_data()
        elif ch == "5": break
        else: print("Invalid!")

if __name__ == "__main__":
    main()
