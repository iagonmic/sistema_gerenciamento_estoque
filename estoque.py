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
