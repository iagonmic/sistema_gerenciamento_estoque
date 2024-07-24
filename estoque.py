from linkedlist import LinkedList
from produto import Product

class Stock:

    def __init__(self):
        self.stock = LinkedList()
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

    #
    # Get product if exists, else return None
    #
    def get_product(self, id):

        ## Get all existent products in stock
        all_products = self.stock.get_all()

        ## Find existent product in stock by ID
        for product in all_products:
            if id == product.id:
                return product
            
        return None
    
    def add_product():  # TODO
        pass

    def remove_product():  # TODO
        pass

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

    def get_product_by_name(): # TODO
        pass

    def get_product_by_category(): # TODO
        pass

    def get_all_products(): # TODO
        pass

    #
    # Order by quantity if stock is not empty
    #
    def order_by_quantity(self):

        if self.stock.is_empty():
            return None

        ## Get all existent produts in stock
        all_products = self.stock.get_all()

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