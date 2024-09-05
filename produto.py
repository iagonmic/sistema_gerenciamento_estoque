class Product:

    def __init__(self, id, name, category, quantity, price):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.sales = 0
    
    def __str__(self) -> str:
        return f'Product:[id={self.id}, name={self.name}, category={self.category.name}, quantity={self.quantity}, price={self.price}, sales={self.sales}]'
    
    def sale(self, amount):
        self.sales += amount
        self.quantity = max(0, self.quantity - amount)

        