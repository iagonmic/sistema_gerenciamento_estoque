class Category:

    def __init__(self, name, father=None):
        self.name = name
        self.father = father
        self.subcategories = []

        if father != None:
            father.add_subcategory(self)
    
    def add_subcategory(self, category):
        self.subcategories.append(category)

    def get_category_by_father(self, name, father):

        for category in father.subcategories:
            if category.name.strip().lower() == name:
                return category

            if not isinstance(category, FinalCategory):
                found = self.get_category_by_father(name, category)
                if found != None:
                    return found

        return None
    
    def get_category(self, name, default_father):
        transformed_name = name.strip().lower()

        if transformed_name == default_father.name.strip().lower():
            return default_father

        return self.get_category_by_father(transformed_name, default_father)
    
    def get_all_final_categories(self):
        final_categories = []

        self.__found_final_category__(self, final_categories)

        return final_categories
    
    def __found_final_category__(self, father, array):

        for category in father.subcategories:
            if isinstance(category, FinalCategory):
                array.append(category)
                continue
            
            self.__found_final_category__(category, array)
    
    def can_insert_items(self):
        return False

    def __str__(self):
        return f"Category:[name={self.name}]"

class FinalCategory(Category):

    def __init__(self, name, father=None):
        super().__init__(name, father)
        self.elements = []

    def add_subcategory(self):
        pass

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)
    
    def get_elements(self):
        return self.elements

    def can_insert_items(self):
        return True

    def __str__(self):
        return f'Produtos de {self.name}: {self.elements}'
    
    def __repr__(self) -> str:
        return self.name
    


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