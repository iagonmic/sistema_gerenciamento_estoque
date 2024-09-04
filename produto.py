class Product:

    def __init__(self, id, name, category, quantity, price):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def __str__(self) -> str:
        return f'Product:[id={self.id}, name={self.name}, category={self.category.name}, quantity={self.quantity}, price={self.price}]'