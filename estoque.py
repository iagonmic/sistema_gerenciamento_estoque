from linkedlist import LinkedList
from produto import Product

class Stock:

    def __init__(self):
        self.stock = LinkedList()

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
            for product in all_products:
                highest = product
                
                if product.quantidade >= highest.quantidade:
                    highest = product
                
            ordered_list.append(highest)
            all_products.remove(highest)

        return ordered_list