from product import Product
from stock import Stock

import random

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

    def get_node(self, product):

        for node in self.nodes:
            if node.product == product:
                return node
            
        return None


    def get_random_product_list(self, max=10):
        all_products = list(self.nodes)
        products = []

        for _ in range(max):
            node_product = None

            while node_product is None:
                node_product = all_products[random.randint(0, len(all_products) - 1)]
                
                for saved_product in products:
                    if saved_product.id == node_product.product.id:
                        continue
                
                products.append(node_product.product)

        return products

    def calculate_dijkstra(self, product_list):
        start = product_list[0]

        possibilities = self.__permutation__(product_list, start, len(product_list))

        shortest_distance = -1
        shortest_possibility = None

        for possibility in possibilities:
            distance = sum([self.get_node_distance(possibility[index], possibility[index + 1])
                            for index in range(len(possibility) - 1)])

            if shortest_distance == -1 or distance < shortest_distance:
                shortest_distance = distance
                shortest_possibility = possibility

        return shortest_distance, shortest_possibility

    def __permutation__(self, lst, start, original_size):

        # If lst is empty then there are no permutations
        if len(lst) == 0:
            return []

        # If there is only one element in lst then, only
        # one permutation is possible
        if len(lst) == 1:
            return [lst]

        # Find the permutations for lst if there are
        # more than 1 characters

        l = [] # empty list that will store current permutation

        # Iterate the input(lst) and calculate the permutation
        for i in range(len(lst)):
            m = lst[i]

            # Extract lst[i] or m from the list. remLst is
            # remaining list
            remLst = lst[:i] + lst[i+1:]

            # Generating all permutations where m is first
            # element
            for p in self.__permutation__(remLst, start, original_size):
                result = [m] + p

                if len(result) == original_size and result[0] != start:
                    continue

                l.append(result)

        return l


stock = Stock()
store = Store(stock)

pr = store.get_random_product_list(3)
store.calculate_dijkstra(pr)