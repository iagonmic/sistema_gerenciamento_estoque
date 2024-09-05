from estoque import Stock

def mensage(products):
        print("-" * 89)
        print(f"|{'ID':<5}|{'Nome':<20}|{'Categoria':<20}|{'Quantidade':<12}|{'Preço':<12}||{'Vendas':<12}|")
        print("-" * 89)
        for product in products:
            print(f"|{product.id:<5}|{product.name:<20}|{product.category.name:<20}|{product.quantity:<12}|{product.price:<12}||{product.sales:<12}|")
        print("-" * 89)

def main():
    stock = Stock()

    while True:
        action = input(
            "Digite 1 - para adicionar, remover ou atualizar produtos,\n"
            "Digite 2 - para buscar produto, por categoria, por quantidade,\n"
            "Digite 3 - para listar os produtos,\n"
            "Digite 4 - para vender um produto, \n"
            "Digite Q - para sair."
            ).upper()

        print("-" * 75)

        if action == "1":
            while True:
                subaction = input(
                    "Digite 1 - para adicionar um produto,\n"
                    "Digite 2 - para remover um produto,\n"
                    "Digite 3 - para atualizar um produto,\n"
                    "Digite Q - para sair."
                    ).upper()
                
                print("-" * 75)
            
                if subaction == "1":    
                    name = input("Digite o nome do produto: ")
                    category = input("Digite a categoria do produto: ")
                    quantity = int(input("Digite a quantidade do produto: "))
                    price = float(input("Digite o preço do produto: "))
                    stock.add_product(name, category, quantity, price)
                    print("-" * 75)

                elif subaction == "2":
                    id = int(input("Digite o ID do produto a ser removido: "))
                    stock.remove_product(id)
                    print("-" * 75)

                elif subaction == "3":
                    product_id = int(input("Digite o id do produto a ser atualizado: "))
                    stock.update_product(product_id)

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
                
                print("-" * 75)
                
                if subaction == "1":
                    product_name = input("Digite o nome do produto a ser encontrado: ")
                    product = stock.get_product_by_name(product_name)
                    if product:
                        print("-" * 75)
                        print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category.name}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 75)
                    else:
                        print("Nenhum produto encontrado.")

                elif subaction == "2":
                    product_category = input("Digite a categoria do produto a ser encontrado: ")
                    products = stock.get_products_by_category(product_category)
                    if not products:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos")
                        print("-" * 75)
                        for product in products:
                            print(f"ID: {product.id}, Nome: {product.name}, Categoria: {product.category}, Quantidade: {product.quantity}, Preço: {product.price}")
                        print("-" * 75)

                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        elif action == "3":
            while True:

                subaction = input("Digite 1 - para listar produtos,\n"
                            "Digite 2 - para listar produtos por quantidade,\n"
                            "Digite 3 - para listar produtos por preço,\n"
                            "Digite Q - para sair."
                            ).upper()
                
                print("-" * 89)

                if subaction == "1":
                    products = stock.get_all_products()
                    if not products:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos")
                        mensage(products)
        
                elif subaction == "2":
                    ordered_list = stock.order_by_quantity()   
                    if not ordered_list:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos ordenados por quantidade")
                        mensage(ordered_list)

                elif subaction == "3":
                    product_name = input("Digite o nome do produto: ")
                    ordered_list = stock.get_products_by_price(product_name)
                       
                    if not ordered_list:
                        print("Nenhum produto encontrado.")
                    else:
                        print("Relatório dos produtos ordenados por preço")
                        mensage(ordered_list)
                
                elif subaction == "Q":
                    break

                else:
                    print("Ação inválida.")

        elif action == "4":
            product_id = int(input("Insira o id do produto a ser vendido: "))
            amount = int(input("Insira a quantidade que você quer vender: "))

            stock.register_sale(product_id, amount)

        elif action == "Q":
            break

        else:
            print("Ação inválida.")

if __name__ == "__main__":
    main()
    
    
