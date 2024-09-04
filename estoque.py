from produto import Product
from tree import Category, ProductCategory, find_product

class Stock:

    def __init__(self):
        self.stock = Category()
        self.current_id = 0
        self.update_actions = [
            { 
                "action": "1",
                "description": "Alterar o nome do produto.", 
                "function": lambda product, new_value: setattr(product, 'name', new_value)
            },
            { 
                "action": "2", 
                "description": "Alterar a categoria do produto.", 
                "function": lambda product, new_value: setattr(product, 'category', new_value)
            },
            { 
                "action": "3", 
                "description": "Alterar a quantidade do produto.", 
                "function": lambda product, new_value: setattr(product, 'quantity', int(new_value))
            },
            { 
                "action": "4", 
                "description": "Alterar o preço do produto.", 
                "function": lambda product, new_value: setattr(product, 'price', float(new_value))
            }
        ]

    # Gerando ID novo a cada criação
    def generate_id(self):
        self.current_id += 1

        return self.current_id

    #
    # Get product if exists, else return None
    #
    def get_product(self, id): 

        ## Get all existent products in stock
        all_products = self.get_all_products()

        ## Find existent product in stock by ID
        for product in all_products:
            if product.id == id:
                return product
            
        return None

    def add_product(self, name, category, quantity, price):
        id = self.generate_id()
        new_product = Product(id, name, category, quantity, price)

        all_products = list(self.get_all_products())

        if not all_products:
            self.stock.add_node(new_product, new_product)
        else:
            for product in all_products:
                self.stock.add_node(new_product, product)

        print(f"Produto {name} adicionado com sucesso.")

    def remove_product(self, id):
        product = self.get_product(id)

        if product is None:
            print("Produto não encontrado.")
            return
        
        self.stock.remove_node(product)
        print(f"Produto '{product.name}' removido com sucesso.")

    def update_product(self, id):
        product = self.get_product(id)

        if product is None:
            return
        
        for action in self.update_actions:
            print(f"{action['action']}: {action['description']}")
        
        action_command = input("Insira o número de qual campo acima você quer alterar: ")
        
        action_object = None
        for action in self.update_actions:
            if action['action'] == action_command:
                action_object = action
        
        if action_object is None:
            print(f"Você inseriu uma ação inválida.")
            self.update_product(id)
            return

        new_value = input("Insira o novo valor para o campo informado: ")
        action_object['function'](product, new_value)

        # --- Graph --- #
        all_products = self.get_all_products()

        for key in all_products:
            nodes = self.stock.get_nodes(key)
            for node in nodes:
                if node == product:
                    action_object['function'][node, new_value]

    # Get product if exists by name
    def get_product_by_name(self, name):
        all_products = self.stock.get_all()
        transformed_name = name.strip().lower()

        for product in all_products:
            if transformed_name == product.name:
                return product
        
        return None
    
    # Get list of products if exists by category
    def get_products_by_category(self, category):
        products = []

        all_products = self.get_all_products()
        transformed_category = category.strip().lower()

        for product in all_products:
            if transformed_category == product.category:
                products.append(product)
        
        return products

    #
    # Get all products from stock
    #
    def get_all_products(self): 
        return self.stock.get_all_nodes()

    #
    # Order by quantity from highest to lowest if stock is not empty
    #
    def order_by_quantity(self):

        if self.stock.is_empty():
            return None

        ## Get all existent produts in stock
        all_products = [element for element in self.get_all_products()]

        ## Initialize ordered list
        ordered_list = []

        ## Search in all of the products list and return
        for i in range(len(all_products)):
            highest = None

            for product in all_products:
                if highest == None or product.quantity >= highest.quantity:
                    highest = product
            
            ordered_list.append(highest)
            all_products.remove(highest)

        return ordered_list
    
    def get_products_by_price(self, origin):
        products = []

        price = origin.price
        difference = 5
        for product in self.get_all_products():
            price_difference = abs(product.price - price)
            if price_difference <= difference:
                products.append(product)

        return products
