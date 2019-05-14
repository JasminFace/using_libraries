class Product:
    def __init__(self, name, base_price, tax=0.13):
        self.name = name
        self.price = base_price
        self.tax = tax
    
    def __str__(self):
        return f"Item: {self.name} Price: ${self.price:.2f}"

    def total_price(self):
        taxes = self.price * self.tax
        total = self.price + taxes
        return total