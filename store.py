from produto import Product
from estoque import Stock       

class Node:
    def __init__(self, product:Product):
        self.product = product
        self.neighbors = {}

    def __repr__(self) -> str:
        return str(self.product)

class Store:
    def __init__(self, stock:Stock):
        self.sections = self.update_stock_sections(stock)
        self.nodes = {Node(product) for product in stock.get_all_products()} # set com um node de cada produto

        for node in self.nodes:
            node.neighbors.update({Node(stock_product):self.get_node_distance(node.product, stock_product) for stock_product in stock.get_all_products()})
        
    # Função para organizar as seções da loja em formato de grid com fileiras de 5 de acordo com as categorias disponíveis na classe stock
    def update_stock_sections(self, stock:Stock):
        return_list = []
        temp_list = [section for section in stock.sections_by_category.values()]

        while len(temp_list) > 0:
            append_list = []

            for _ in range(5):
                if len(temp_list) == 0:
                    break

                actual_section = temp_list[0]
                temp_list.remove(actual_section)
                append_list.append(actual_section)

            return_list.append(append_list)

        return return_list
    

    # nesse caso será implementada a distância de Manhattan pois o movimento só é feito em linhas horizontais e verticais no grid do estoque
    # caso fosse possível movimento livre, em diagonais, utilizariamos a distância Euclidiana
    def get_node_distance(self, origin:Product, end:Product):
        origin_row = 0
        origin_column = 0

        end_row = 0
        end_column = 0

        for row in self.sections:
            if origin.section in row:
                origin_column = row.index(origin.section)
                origin_row = self.sections.index(row)

            if end.section in row:
                end_column = row.index(end.section)
                end_row = self.sections.index(row)

        return abs(end_row - origin_row) + abs(end_column + origin_column)