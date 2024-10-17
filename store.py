from produto import Product
from estoque import Stock       

class Node:
    def __init__(self, product:Product):
        self.value = product
        self.neighbors = {}

class Store:
    def __init__(self, stock:Stock):
        self.sections = [len(self.sections) + 1 for final_category in stock.product_category.get_all_final_categories()]
        self.nodes = {Node(product) for product in stock.get_all_products} # set com um node de cada produto

        # tem que ver como vai fazer para adicionar o peso de cada produto
        
    def add_section(self):
        self.sections.append(len(self.sections) + 1)

    def add_node(self, node:Node):
        self.nodes.add(node)

        for node in self.nodes:
            pass
            
            # node.neighbors.update{} <- passar o peso da aresta para cada node da loja
        