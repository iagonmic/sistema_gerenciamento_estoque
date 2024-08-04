from estoque import Stock

def main():
    stock = Stock()

    while True:
        action = input("""Digite 1 - para adicionar, remover ou atualizar produtos,
                    Digite 2 - para buscar produto, por categoria, por quantidade,
                    Digite 3 - para listar os produtos,
                    Digite Q - para sair.""").upper()

        if action == "1":
            while True:
                subaction = input("""Digite 1 - para adicionar um produto,
                        Digite 2 - para remover um produto,
                        Digite 3 - para atualizar um produto,
                        Digite Q - para sair.""").upper()
            
                if subaction == "1":    
                    name = input("Digite o nome do produto: ")
                    category = input("Digite a categoria do produto: ")
                    quantity = int(input("Digite a quantidade do produto: "))
                    price = float(input("Digite o preço do produto: "))
                    stock.add_product(name, category, quantity, price)
                    pass

                elif subaction == "2":
                    id = int(input("Digite o ID do produto a ser removido: "))
                    stock.remove_product(id)
                    pass

                elif subaction == "3":    # TODO
                    stock.update_product()
                    pass

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        if action == "2":
            while True:
                subaction = input("""Digite 1 - para buscar um produto,
                            Digite 2 - para buscar por categoria,
                            Digite Q - para sair.""").upper()
                
                if subaction == "1":
                    stock.get_product_by_name() # TODO
                    pass

                elif subaction == "2":
                    stock.get_product_by_category() # TODO
                    pass

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        if action == "3":
            while True:

                subaction = input("""Digite 1 - para listar produtos,
                            Digite 2 - para listar produtos por quantidade,
                            Digite Q - para sair.""").upper()
                
                if subaction == "1":
                    stock.get_all_products()    # TODO
                    pass

                elif subaction == "2":
                    stock.order_by_quantity()   # FIXME
                    pass

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        if action == "Q":
            break

        pass

if __name__ == "__main__":
    main()
    
    
