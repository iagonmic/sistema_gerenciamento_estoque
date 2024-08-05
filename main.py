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

                elif subaction == "3":
                    product_id = int(input("Digite o id do produto a ser atualizado: "))
                    stock.update_product(product_id)
                    # TODO

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        elif action == "2":
            while True:
                subaction = input(
                    "Digite 1 - para buscar um produto,\n"
                    "Digite 2 - para buscar por categoria,\n"
                    "Digite Q - para sair."
                    ).upper()
                
                print("-" * 60)
                
                if subaction == "1": # TODO
                    product_name = input("Digite o nome do produto a ser encontrado: ")
                    product = stock.get_product_by_name(product_name)
                    if product:
                        print("-" * 60)
                        print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 60)
                    else:
                        print("Nenhum produto encontrado.")

                elif subaction == "2": # TODO
                    product_category = input("Digite a categoria do produto a ser encontrado: ")
                    products = stock.get_products_by_category(product_category)
                    if not products:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos")
                        print("-" * 60)
                        for product in products:
                            print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 60)

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        elif action == "3":
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
                    ordered_list = stock.order_by_quantity()   
                    if not products:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos ordenados por quantidade")
                        print("-" * 60)
                        for product in ordered_list:
                            print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 60)
                    pass

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        elif action == "Q":
            break

        else:
            print("Ação inválida.")

if __name__ == "__main__":
    main()
    
    
