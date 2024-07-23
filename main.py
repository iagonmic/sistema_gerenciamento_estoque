from estoque import Stock

def main():
    stock = Stock()

    while True:
        action = input("""Digite 1 - para adicionar, remover ou atualizar produtos,
                    Digite 2 - para buscar produto, por categoria, por quantidade,
                    Digite 3 - para listar os produtos,
                    Digite Q - para sair.
                """).upper()

        if action == "1":
            while True:
                subaction = input("""Digite 1 - para adicionar um produto,
                            Digite 2 - para remover um produto,
                            Digite 3 - para atualizar um produto,
                            Digite Q - para sair.
                        """).upper()
            
                if subaction == "1":    # TODO
                    stock.add_product()
                    pass

                if subaction == "2":    # TODO
                    stock.remove_product()
                    pass

                if subaction == "3":    # TODO
                    stock.update_product()
                    pass

                if subaction == "Q":
                    break

                print("Ação inválida.")
                continue

        if action == "2":
            while True:
                subaction = input("""Digite 1 - para buscar um produto,
                            Digite 2 - para buscar por categoria,
                            Digite Q - para sair.
                        """).upper()
                
                if subaction == "1":
                    stock.get_product_by_name() # TODO
                    pass

                if subaction == "2":
                    stock.get_product_by_category() # TODO
                    pass

                if subaction == "Q":
                    break

                print("Ação inválida.")

        if action == "3":
            while True:

                subaction = input("""Digite 1 - para listar produtos,
                            Digite 2 - para listar produtos por quantidade,
                            Digite Q - para sair.
                        """).upper()
                
                if subaction == "1":
                    stock.get_all_products()    # TODO
                    pass

                if subaction == "2":
                    stock.order_by_quantity()   # FIXME
                    pass

                if subaction == "Q":
                    break

                print("Ação inválida.")
                continue

        if action == "Q":
            break

        pass

if __name__ == "__main__":
    main()
    
    
