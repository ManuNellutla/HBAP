class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def add_discount(self, discount):
        self.price = self.price * (1-discount)

class Pant:
    def __init__(self, pant_color, pant_size, pant_style, pant_price):
        self.color = pant_color
        self.size = pant_size
        self.style = pant_style
        self.price = pant_price

    def change_price(self, new_price):
        self.price = new_price

    def add_discount(self, discount):
        self.price = self.price * (1-discount)
