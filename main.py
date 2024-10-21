from store import Store
from estoque import Stock
import streamlit as stl
import plotly.graph_objs as go
import networkx as nx
import pandas as pd

def show_products(products):
    # Converte os objetos Product para uma lista de dicionários
    product_dicts = [product.to_dict() for product in stl.session_state.stock.get_all_products()]
    
    # Cria o DataFrame
    df = pd.DataFrame(product_dicts).sort_values("ID")
    
    # Exibe o DataFrame no Streamlit
    stl.dataframe(df, hide_index=True, height=400, width= 1200)

def show_products_by_category(products, category):
    # Converte os objetos Product para uma lista de dicionários
    product_dicts = [product.to_dict() for product in products]
    
    # Cria o DataFrame
    df = pd.DataFrame(product_dicts).sort_values("ID")

    df = df.query(f"Categoria=='{category}'")
    
    # Exibe o DataFrame no Streamlit
    stl.dataframe(df, hide_index=True, height=400, width= 1200)

def create_edge(products):
    edge = []

    for i in range(len(products) - 1):
        current_name = products[i].name
        next_name = products[i + 1].name
        distance = stl.session_state.store.get_node_distance(products[i], products[i+1])

        tuple_edge = (current_name, next_name, distance)

        edge.append(tuple_edge)

    return edge

def order_list(initial_list, product_name):
    product_index = initial_list.index(product_name)

    first_item = initial_list[product_index]
    change_item = initial_list[0]

    initial_list[0] = first_item
    initial_list[product_index] = change_item

    return initial_list

def get_graph(arestas):
    graph = nx.Graph()
    
    for first_product, last_product, distance in arestas:
        graph.add_edge(first_product, last_product, weight=distance)

    return graph

def plot_grafo(graph, edge_color, node_color, bg_color, font_size, layout_type, text_color, edge_width, node_size, box_color, box_size, node_text_color, fig_width, fig_height):
    # Determinar o layout com base na escolha do usuário
    if layout_type == "spring":
        pos = nx.spring_layout(graph)
    elif layout_type == "circular":
        pos = nx.circular_layout(graph)
    elif layout_type == "random":
        pos = nx.random_layout(graph)
    elif layout_type == "shell":
        pos = nx.shell_layout(graph)
    else:
        pos = nx.kamada_kawai_layout(graph)  # Padrão se o layout não for reconhecido

    # Criar listas para as coordenadas das arestas
    edge_x = []
    edge_y = []
    edge_text = []  # Lista para armazenar os textos das distâncias
    edges = list(graph.edges(data=True))  # Obter as arestas como uma lista

    for edge in edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])  # None para criar uma quebra na linha
        edge_y.extend([y0, y1, None])
        edge_text.append(f"{edge[2]['weight']}")  # Armazena a distância da aresta

    # Criação das arestas
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=edge_width, color=edge_color),
        hoverinfo='none',
        mode='lines'
    )

    # Criação dos nós
    node_x = [pos[node][0] for node in graph.nodes()]
    node_y = [pos[node][1] for node in graph.nodes()]
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        marker=dict(size=node_size, color=node_color, line=dict(width=2)),
        text=[node for node in graph.nodes()],
        textposition="middle center",  # Centraliza o texto dentro do nó
        textfont=dict(size=font_size, color=node_text_color),  # Cor do texto do nó configurável
        hoverinfo='text'
    )

    # Criar a figura
    fig = go.Figure(data=[edge_trace, node_trace])

    # Adicionar textos das distâncias com caixa de fundo
    for i, text in enumerate(edge_text):
        # Posicionar o texto no meio da aresta
        x0, y0 = pos[edges[i][0]]
        x1, y1 = pos[edges[i][1]]
        x_text = (x0 + x1) / 2
        y_text = (y0 + y1) / 2
        
        fig.add_annotation(
            x=x_text,
            y=y_text,
            text=text,
            showarrow=False,
            font=dict(size=font_size, color=text_color),  # Cor do texto da distância configurável
            bgcolor=box_color,  # Cor da caixa de fundo configurável
            bordercolor="black",  # Cor da borda da caixa (não será visível com borderwidth=0)
            borderwidth=0,  # Sem borda
            borderpad=4,  # Preenchimento da borda
            xref="x",  # Referência do eixo X
            yref="y",  # Referência do eixo Y
            width=box_size[0],  # Largura da caixa
            height=box_size[1],  # Altura da caixa
        )

    fig.update_layout(
        width=fig_width,  # Definindo a largura
        height=fig_height,  # Definindo a altura
        showlegend=False,
        hovermode='closest',
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor=bg_color
    )

    return fig

def home():
    stl.title(":package: Bem-vindo(a) ao Sistema de Gerenciamento de Estoque!")
    stl.subheader('Use o menu ao lado para navegar para outras páginas.')
    stl.image('img/vegeta-careca.png')

def add_product():
    stl.header("Adicionar Produto")

    # Campos para adicionar um produto com chaves únicas
    nome = stl.text_input("Nome do Produto", key="nome_produto")
    categoria = stl.selectbox("Categoria", stl.session_state.categories, key="categoria_produto")
    quantidade = stl.number_input("Quantidade", min_value=1, step=1, key="quantidade_produto")
    preco = stl.number_input("Preço", min_value=0.0, step=0.50, key="preco_produto")

    # Botão para adicionar o produto
    if stl.button("Adicionar Produto"):
        if nome and categoria and quantidade > 0 and preco >= 0:
            stl.session_state.stock.add_product(nome, categoria, quantidade, preco)
            show_products()

        else:
            stl.error("Por favor, preencha todos os campos corretamente.")


def remove_product():
    stl.header("Remover Produto")

    id = stl.text_input("ID do Produto", key="ID_produto")

    if stl.button("Remover Produto"):
        stl.session_state.stock.remove_product(int(id))
        show_products()


def update_product():
    stl.title("Atualizar Produto")

    stl.header("Seleção do Produto")

    selected_product = stl.selectbox(
        "Escolha o produto que deseja atualizar",
        options=stl.session_state.stock.get_all_products()
    )

    # Verifica se um produto foi selecionado
    if selected_product:
        product = stl.session_state.stock.get_product_by_name(str(selected_product))

        options_update = ["Atualizar Nome", "Atualizar Categoria", "Atualizar Quantidade", "Atualizar Preço"]
        menu_update = stl.selectbox("Escolha o que deseja alterar", options=options_update)

        # Para garantir que os valores persistam ao trocar de campos
        if 'selected_option' not in stl.session_state:
            stl.session_state.selected_option = None

        # Atualiza o estado da opção selecionada
        stl.session_state.selected_option = menu_update

        # Atualiza Nome
        if stl.session_state.selected_option == "Atualizar Nome":
            new_name = stl.text_input("Nome do Produto", key="nome_produto")
            if stl.button("Salvar Nome"):
                stl.session_state.stock.update_product(product.id, "1", new_name)
                stl.success(f"Nome do produto atualizado para {new_name}")

        # Atualiza Categoria
        elif stl.session_state.selected_option == "Atualizar Categoria":
            new_category = stl.text_input("Categoria do Produto", key="categoria_produto")
            if stl.button("Salvar Categoria"):
                stl.session_state.stock.update_product(product.id, "2", new_category)
                stl.success(f"Categoria do produto atualizada para {new_category}")

        # Atualiza Quantidade
        elif stl.session_state.selected_option == "Atualizar Quantidade":
            new_quantity = stl.number_input("Quantidade do Produto", min_value=1, step=1, key="quantidade_produto")
            if stl.button("Salvar Quantidade"):
                stl.session_state.stock.update_product(product.id, "3", new_quantity)
                stl.success(f"Quantidade do produto atualizada para {new_quantity}")

        # Atualiza Preço
        elif stl.session_state.selected_option == "Atualizar Preço":
            new_price = stl.number_input("Preço do Produto", min_value=1.0, step=0.01, key="preco_produto")
            if stl.button("Salvar Preço"):
                stl.session_state.stock.update_product(product.id, "4", new_price)
                stl.success(f"Preço do produto atualizado para {new_price}")



def show_route():
    stl.title("Calcular Rota")

    stl.header("Seleção de Produtos")

    selected_products = stl.multiselect(
        "Escolha os produtos que deseja adicionar à lista",
        options=stl.session_state.stock.get_all_products()
    )

    # Botão para salvar a seleção
    if stl.button("Salvar seleção"):
        stl.session_state.saved_products = []

        # Adiciona os produtos selecionados à lista de salvos
        stl.session_state.saved_products.extend(selected_products)
        # Remove duplicatas
        stl.session_state.saved_products = list(set(stl.session_state.saved_products))
        stl.success(f"Produtos salvos: {', '.join(selected_products)}")

    # Exibe os produtos salvos
    if 'saved_products' in stl.session_state and stl.session_state.saved_products:
        stl.write("Lista de produtos salvos:")
        stl.write(stl.session_state.saved_products)

        # Select box para escolher o primeiro produto
        first_product = stl.selectbox('Selecione o primeiro produto da lista:', stl.session_state.saved_products)

        # Botão para atualizar o gráfico com a nova seleção
        if stl.button("Atualizar Gráfico"):
            # Chama a função order_list e atualiza a lista de produtos
            ordered_product_list = order_list(stl.session_state.saved_products, str(first_product))  # Organiza a lista

            # Atualiza o gráfico com a lista ordenada
            product_list = [stl.session_state.stock.get_product_by_name(product) for product in ordered_product_list]

            # Calcule o Dijkstra
            _, dijkstra = stl.session_state.store.calculate_dijkstra(product_list)
            edge = create_edge(dijkstra)

            # Atualiza o gráfico
            graph(edge, ordered_product_list)

            # Exibe a lista ordenada
            stl.write(f"Lista de produtos ordenada com {first_product} como o primeiro produto.")

    else:
        stl.write("Nenhum produto salvo ainda.")

def show_products_page():

    actions = ["Listar todos Produtos", "Listar por Categoria"]

    action_selectbox = stl.selectbox("Escolha o Método de busca", options=actions)

    products = stl.session_state.stock.get_all_products()

    if action_selectbox == "Listar todos Produtos":
        show_products(products)

    if action_selectbox == "Listar por Categoria":
        category = stl.selectbox("Escolha a categoria", options=stl.session_state.categories)

        # Atualiza automaticamente ao selecionar a categoria
        if category:
            show_products_by_category(products, category)

def graph(edge, lista):

    # Opções de personalização definidas diretamente no código
    edge_color = "#FFD700"  # Cor das arestas
    node_color = "#36A2EB"  # Cor dos nós
    text_color = "#F4E04D"  # Cor do texto da distância
    node_text_color = "#FFFFFF"  # Cor do texto dentro dos nós
    bg_color = "#0e1117"    # Cor do fundo
    font_size = 15        # Tamanho da fonte
    edge_width = 4        # Grossura das arestas
    node_size = 60       # Tamanho dos nós
    layout_type = "circular"  # Tipo de layout
    box_color = "#0e1117"  # Cor da caixa de fundo para as distâncias
    box_size = (10, 20)  # Tamanho da caixa de fundo (largura, altura)

    graph = get_graph(edge)

    # Plotar o grafo com as configurações
    fig = plot_grafo(graph, edge_color, node_color, bg_color, font_size, layout_type, text_color, edge_width, node_size, box_color, box_size, node_text_color,  1080, 600)

    first_product = lista[0]

    stl.title(f"Grafo da melhor rota para {first_product}:")
    stl.plotly_chart(fig)

def main():
    if 'stock' not in stl.session_state:
        stl.session_state['stock'] = Stock()
        stl.session_state['store'] = Store(stl.session_state['stock'])
        stl.session_state['categories'] = [key.name for key in stl.session_state.stock.sections_by_category.keys()]
    
    stl.set_page_config('Sistema de Gerenciamento de Estoque', ':package:')

    pages = [
        "Home",
        "Adicionar Produto",
        "Remover Produto",
        "Listar Produtos",
        "Atualizar Produtos",
        "Calcular Rota"
    ]
    
    menu = stl.sidebar.selectbox("Escolha uma opção", pages)

    if menu == "Home":
        home()

    elif menu == "Adicionar Produto":
        add_product()

    elif menu == "Remover Produto":
        remove_product()

    elif menu == "Listar Produtos":
        show_products_page()

    elif menu == "Atualizar Produtos":
        update_product()

    elif menu == "Calcular Rota":
        graph()

if __name__ == "__main__":
    main()