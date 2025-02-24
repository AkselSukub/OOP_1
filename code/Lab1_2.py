class Goods:

    def __init__(self, name="", date="", price=0.0, quantity=0, invoice_number=""):
        self.name = name
        self.date = date
        self.price = price
        self.quantity = quantity
        self.invoice_number = invoice_number

    def read(self):
        self.name = input("Введите наименование товара: ")
        self.date = input("Введите дату оформления: ")
        self.price = float(input("Введите цену товара: "))
        self.quantity = int(input("Введите количество товара: "))
        self.invoice_number = input("Введите номер накладной: ")

    def display(self):
        print("Наименование товара:", self.name)
        print("Дата оформления:", self.date)
        print("Цена товара:", self.price)
        print("Количество товара:", self.quantity)
        print("Номер накладной:", self.invoice_number)

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, delta):
        self.quantity += delta

    def calculate_total_cost(self):
        return self.price * self.quantity

if __name__ == "__main__":
    product = Goods()

    product.read()

    product.display()

    new_price = float(input("Введите новую цену товара: "))
    product.change_price(new_price)

    delta = int(input("Введите изменение количества товара: "))
    product.change_quantity(delta)

    total_cost = product.calculate_total_cost()
    print("Стоимость товара:", total_cost)