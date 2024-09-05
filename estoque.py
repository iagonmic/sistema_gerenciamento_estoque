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
        self.load_categories()
        self.load_products()

    def load_categories(self):
        father = self.product_category

        alimenticios = Category('Alimentícios', father)
        nao_alimenticios = Category('Não Alimentícios', father)

        FinalCategory('Carnes', alimenticios)
        FinalCategory('Frutas', alimenticios)
        FinalCategory('Grãos', alimenticios)
        FinalCategory('Laticínios', alimenticios)

        FinalCategory('Higiene', nao_alimenticios)
        FinalCategory('Limpeza', nao_alimenticios)
        FinalCategory('Beleza', nao_alimenticios)

    def load_products(self):
        self.add_product("Arroz", "Grãos", 10, 45)
        self.add_product("Feijão", "Grãos", 8, 37)
        self.add_product("Macarrão", "Grãos", 5, 22)
        self.add_product("Açúcar", "Grãos", 3, 15)
        self.add_product("Café", "Grãos", 7, 60)
        self.add_product("Óleo de Soja", "Grãos", 9, 50)
        self.add_product("Leite", "Laticínios", 4, 12)
        self.add_product("Queijo", "Laticínios", 3, 80)
        self.add_product("Iogurte", "Laticínios", 4, 18)
        self.add_product("Manteiga", "Laticínios", 7, 40)
        self.add_product("Presunto", "Carnes", 6, 75)
        self.add_product("Bacon", "Carnes", 3, 65)
        self.add_product("Carne Moída", "Carnes", 5, 90)
        self.add_product("Frango", "Carnes", 6, 85)
        self.add_product("Banana", "Frutas", 8, 10)

        self.add_product("Sabão em Pó", "Limpeza", 6, 35)
        self.add_product("Detergente", "Limpeza", 10, 8)
        self.add_product("Desinfetante", "Limpeza", 7, 25)
        self.add_product("Água Sanitária", "Limpeza", 8, 30)
        self.add_product("Amaciante", "Limpeza", 2, 55)
        self.add_product("Papel Higiênico", "Higiene", 9, 12)
        self.add_product("Shampoo", "Higiene", 4, 45)
        self.add_product("Condicionador", "Higiene", 3, 50)
        self.add_product("Creme Dental", "Higiene", 8, 18)
        self.add_product("Sabonete", "Higiene", 10, 5)
        self.add_product("Escova de Dentes", "Higiene", 7, 14)
        self.add_product("Lâmina de Barbear", "Beleza", 4, 20)
        self.add_product("Esmalte", "Beleza", 5, 9)
        self.add_product("Maquiagem", "Beleza", 6, 80)
        self.add_product("Perfume", "Beleza", 3, 100)

    # Gerando ID novo a cada criação
    def generate_id(self):
        self.current_id += 1

        return self.current_id
    
    def get_product(self, id, category=None): # Busca em profundidade (DFS)
        if category == None:
            category = self.product_category

        if category.can_insert_items():
            for product in category.elements:
                if product.id == id:
                    return product
                
            return None
        
        for subcategory in category.subcategories:
            product = self.get_product(id, subcategory)
            if product != None:
                return product
        
        return None
    
    def get_category(self, name):
        return self.product_category.get_category(name, self.product_category)

    def add_product(self, name, category_name, quantity, price):

        category = self.get_category(category_name)
        if category == None:
            print("Categoria não encontrada.")
            return
        
        if not category.can_insert_items():
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

    # Get product if exists by name
    def get_product_by_name(self, name):
        all_products = self.get_all_products()
        transformed_name = name.strip().lower()

        for product in all_products:
            if transformed_name == product.name.strip().lower():
                return product
        
        return None
    
    # Get list of products if exists by category
    def get_products_by_category(self, category_name):
        
        transformed_category_name = category_name.strip().lower()
        category = self.get_category(transformed_category_name)

        products = []

        # First case: category is a final category
        if category.can_insert_items():
            for element in category.elements:
                products.append(element)
            
            return products

        # Second case: category is not a final category
        product_categories = category.get_all_final_categories()

        for product_category in product_categories:
            for element in product_category.elements:
                products.append(element)

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
    
    def is_empty(self):
        return not self.get_all_products()

    #
    # Order by quantity from highest to lowest if stock is not empty
    #
    def order_by_quantity(self):

        if self.is_empty():
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
    
    def get_products_by_price(self, product_name):
        products = []

        found_product = self.get_product_by_name(product_name)
        if found_product is None:
            print("Não foi encontrado um produto com este nome.")
            return products

        price = found_product.price

        difference = 5
        for product in self.get_all_products():
            price_difference = abs(product.price - price)
            if price_difference <= difference:
                products.append(product)
        
        return products
    
    def register_sale(self, product_id, amount):
        product = self.get_product(product_id)

        if product == None:
            print("O produto não foi encontrado.")
            return
            
        if product.quantity < amount:
            print(f"Você não possui a quantia necessária de {product.name} para vender.")
            return
        
        product.sale(amount)
        print(f"Você vendeu {amount} unidades de {product.name}.")