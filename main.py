from estoque import Stock

def main():
    stock = Stock()

    while True:
        action = input(
            "Digite 1 - para adicionar, remover ou atualizar produtos,\n"
            "Digite 2 - para buscar produto, por categoria, por quantidade,\n"
            "Digite 3 - para listar os produtos,\n"
            "Digite Q - para sair."
            ).upper()

        print("-" * 60)

        if action == "1":
            while True:
                subaction = input(
                    "Digite 1 - para adicionar um produto,\n"
                    "Digite 2 - para remover um produto,\n"
                    "Digite 3 - para atualizar um produto,\n"
                    "Digite Q - para sair."
                    ).upper()
                
                print("-" * 60)
            
                if subaction == "1":    
                    name = input("Digite o nome do produto: ")
                    category = input("Digite a categoria do produto: ")
                    quantity = int(input("Digite a quantidade do produto: "))
                    price = float(input("Digite o preço do produto: "))
                    stock.add_product(name, category, quantity, price)
                    print("-" * 60)

                elif subaction == "2":
                    id = int(input("Digite o ID do produto a ser removido: "))
                    stock.remove_product(id)
                    print("-" * 60)

                elif subaction == "3":    # TODO
                    stock.update_product()
                    pass

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        if action == "2":
            while True:
                subaction = input(
                    "Digite 1 - para buscar um produto,\n"
                    "Digite 2 - para buscar por categoria,\n"
                    "Digite Q - para sair."
                    ).upper()
                
                print("-" * 60)
                
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

                subaction = input("Digite 1 - para listar produtos,\n"
                            "Digite 2 - para listar produtos por quantidade,\n"
                            "Digite Q - para sair."
                            ).upper()
                
                print("-" * 60)

                if subaction == "1":
                    products = stock.get_all_products()
                    if not products:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos")
                        print("-" * 60)
                        for product in products:
                            print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 60)
        
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
    
    
