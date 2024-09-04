from produto import Product
from tree import Category, FinalCategory

class Stock:

    def __init__(self):
        self.current_id = 0
        self.product_category = Category('Produtos')
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
    
    def get_product(self, id, category=None): # Busca em profundidade (DFS)
        if category == None:
            category = self.product_category

        if isinstance(category, FinalCategory):
            for product in category.elements:
                if product.id == id:
                    return product
                
            return None
        
        for subcategory in category.subcategories:
            product = self.get_product(subcategory, id)
            if product != None:
                return product
        
        return None
    
    def can_insert_items(self, category: Category):
        return isinstance(category, FinalCategory)

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

    def add_product(self, name, category_name, quantity, price):

        category = self.get_category(category_name)
        if category == None:
            print("Categoria não encontrada.")
            return
        
        if not self.can_insert_items(category):
            print("Você não pode inserir elementos nesta categoria.")
            return

        id = self.generate_id()
        new_product = Product(id, name, category, quantity, price)
        category.add_element(new_product)

        print(f"Produto {name} adicionado com sucesso.")

    def remove_product(self, id):
        product = self.get_product(id)

        if product is None:
            print("Produto não encontrado.")
            return
        
        product.category.remove_element(product)

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
        products = []

        for final_category in self.product_category.get_all_final_categories():
            for element in final_category.elements:
                products.append(element)

        return products

    #
    # Order by quantity from highest to lowest if stock is not empty
    #
    def order_by_quantity(self):

        if self.stock.is_empty():
            return None

        ## Get all existent produts in stock
        all_products = self.get_all_products()

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
    
    def sale():
        pass

stock = Stock()

father = stock.product_category

alimenticios = Category("alimentícios", father)
nao_alimenticios = Category("não alimenticios", father)

frutas = FinalCategory("frutas", alimenticios)
verduras = FinalCategory("verduras", alimenticios)

uva = Product(1, 'uva', frutas, 3, 5)
pera = Product(2, 'pera', frutas, 5, 10)

"""
print(id(nao_alimenticios))
print("-" * 60)
found_frutas = stock.get_category('não alimenticios')
print(id(found_frutas))
print('Encontrado:', found_frutas)"""
