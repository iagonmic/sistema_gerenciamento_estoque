class Category:

    def __init__(self, name, father=None):
        self.name = name
        self.father = father
        self.subcategories = []

        if father != None:
            father.add_subcategory(self)
    
    def add_subcategory(self, category):
        self.subcategories.append(category)

    def __str__(self):
        return f"Category:[name={self.name}]"

class ProductCategory(Category):

    def __init__(self, name, father=None):
        super().__init__(name, father)
        self.products = []

    def add_subcategory(self):
        pass

    def __str__(self):
        return f'Produtos de {self.name}: {self.products}'


def find_product(category, name): # Busca em profundidade (DFS)
    if isinstance(category, ProductCategory):
        for product in category.products:
            if product == name:
                return product
            
        return None
    
    for subcategory in category.subcategories:
        product = find_product(subcategory, name)
        if product != None:
            return product
    
    return None


"""
TESTE:
produtos = Category("produtos")

alimenticio = ProductCategory("alimenticios", father=produtos)
alimenticio.products.append('uva')
alimenticio.products.append('pera')

nao_alimenticio = ProductCategory("não alimenticios", father=produtos)
nao_alimenticio.products.append('cadeira')
nao_alimenticio.products.append('pano de chao')

product = find_product(produtos, 'uva')
print(product)
"""