from store import Store
from stock import Stock
import streamlit as st
import plotly.graph_objs as go
import networkx as nx
import pandas as pd

def show_products(view=True, filter:dict={}):
    # Converte os objetos Product para uma lista de dicionários
    product_dicts = [product.to_dict() for product in st.session_state.stock.get_all_products()]
    
    # Cria o DataFrame
    df = pd.DataFrame(product_dicts).sort_values("ID")

    # Filtrar pela coluna e valor
    if len(filter) != 0:

        if isinstance(filter[1], str):
            df = df.query(f'{str(filter[0])} == "{filter[1]}"')
        elif isinstance(filter[1], int) or isinstance(filter[1], float):
            df = df.query(f'{str(filter[0])} == {filter[1]}')
        else:
            pass
    
    # Exibe o DataFrame no Streamlit
    if view == True: 
        st.dataframe(df, hide_index=True, height=400, width= 1200)

    return df

def show_products_by_category(category):
    # Converte os objetos Product para uma lista de dicionários
    product_dicts = [product.to_dict() for product in st.session_state.stock.get_all_products()]
    
    # Cria o DataFrame
    df = pd.DataFrame(product_dicts).sort_values("ID")

    df = df.query(f"Categoria=='{category}'")
    
    # Exibe o DataFrame no Streamlit
    st.dataframe(df, hide_index=True, height=400, width= 1200)

def create_edge(products):
    edge = []

    for i in range(len(products) - 1):
        current_name = products[i].name
        next_name = products[i + 1].name
        distance = st.session_state.store.get_node_distance(products[i], products[i+1])

        tuple_edge = (current_name, next_name, distance)

        edge.append(tuple_edge)

    return edge

def order_list(initial_list, product):

    print(id(product))

    for elemento in initial_list:   
        print(id(elemento), '--', elemento, ';')

    product_index = initial_list.index(product)

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
    st.title(":package: Bem-vindo(a) ao Sistema de Gerenciamento de Estoque")
    st.subheader('Use o menu ao lado para navegar para outras páginas :flag-br:')
    st.image('vegeta-careca.png')

def add_product():
    st.title("Adicionar Produto")

    st.header("Digite as informações do produto que você quer adicionar:")

    # Campos para adicionar um produto com chaves únicas
    nome = st.text_input("Nome do Produto", key="nome_produto", placeholder="Digite o nome do produto")
    categoria = st.selectbox("Categoria", st.session_state.categories, key="categoria_produto")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key="quantidade_produto")
    preco = st.number_input("Preço", min_value=0.0, step=0.50, key="preco_produto")

    # Botão para adicionar o produto
    if st.button("Adicionar Produto"):
        if nome and categoria and quantidade > 0 and preco >= 0:
            st.session_state.stock.add_product(nome, categoria, quantidade, preco)
            show_products()

        else:
            st.error("Por favor, preencha todos os campos corretamente.")


def remove_product():
    st.title("Remover Produto")

    st.header("Escolha o produto a ser removido:")

    product = st.selectbox('Escolha o produto', options=st.session_state.stock.get_all_products(), placeholder="Escolha uma opção", index=None)

    try: id = int(id)
    except: pass

    if st.button("Remover Produto") and product is not '':
        st.session_state.stock.remove_product(product.id)
        st.rerun()

    show_products()


def update_product():
    st.title("Atualizar Produto")

    st.header("Digite as informações do produto que deseja atualizar:")

    selected_product = st.selectbox(
        "Escolha o produto que quer alterar",
        options=st.session_state.stock.get_all_products(),
        placeholder='Escolha uma opção',
        index=None
    )

    # Verifica se um produto foi selecionado
    if selected_product:
        product = st.session_state.stock.get_product(selected_product.id)

        options_update = ["Nome", "Categoria", "Quantidade", "Preço"]
        menu_update = st.selectbox("Escolha o que deseja alterar", options=options_update, placeholder='Escolha uma opção', index=None)

        # Para garantir que os valores persistam ao trocar de campos
        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = None

        # Atualiza o estado da opção selecionada
        st.session_state.selected_option = menu_update

        new_value = st.text_input(f'{menu_update} do Produto')

        try: int(new_value)
        except: pass

        if st.button(f'Salvar {menu_update}'):
            st.session_state.stock.update_product(product.id, menu_update, new_value)
            st.success(f"{menu_update} do produto {selected_product.name} atualizado para {new_value}")
            show_products()

def remove_duplicates(new_list):
    temp_list = []

    for item in new_list:
        if item not in temp_list:
            temp_list.append(item)
    
    return temp_list

def show_route():
    st.title("Calcular Rota")

    st.header("Seleção de Produtos")

    selected_products = st.multiselect(
        "Escolha os produtos que deseja adicionar à lista",
        options=st.session_state.stock.get_all_products(),
        placeholder='Escolha uma opção'
    )

    if 'saved_products' not in st.session_state:
        st.session_state.saved_products = []

    # Botão para salvar a seleção
    if st.button("Salvar seleção"):
        # Adiciona os produtos selecionados à lista de salvos
        st.session_state.saved_products = remove_duplicates(selected_products)

        # Exibe os produtos salvos
    if len(st.session_state.saved_products) != 0:
        st.write("Lista de produtos salvos:")
        st.write(st.session_state.saved_products)

        # Select box para escolher o primeiro produto
        first_product = st.selectbox('Selecione o primeiro produto da lista:', st.session_state.saved_products)

        # Botão para atualizar o gráfico com a nova seleção
        if st.button("Atualizar Grafo"):
            # Chama a função order_list e atualiza a lista de produtos
            ordered_product_list = order_list(st.session_state.saved_products, first_product)  # Organiza a lista

            # Atualiza o gráfico com a lista ordenada
            product_list = [st.session_state.stock.get_product_by_name(product.name) for product in ordered_product_list]

            # Calcule o Dijkstra
            _, dijkstra = st.session_state.store.calculate_dijkstra(product_list)
            edge = create_edge(dijkstra)

            # Atualiza o gráfico
            graph(edge, ordered_product_list)

            # Exibe a lista ordenada
            st.write(f"Lista de produtos ordenada com {first_product} como o primeiro produto.")

    else:
        st.write("Nenhum produto salvo ainda.")

def show_products_page():
    filter = {}

    st.title("Listar Produtos")

    st.header('Esses são os produtos do estoque atual:')

    option = st.selectbox('Escolha o método de busca', options=['Listar Produtos', 'Filtrar Seleção'])
    
    if option == 'Filtrar Seleção':
        filter_option = st.selectbox(
            'Escolha o filtro:',
            options=show_products(view=False).columns
        )
        
        filter_value = st.selectbox(
            'Escolha ou digite o valor que você quer filtrar:',
            options=show_products(view=False)[str(filter_option)].unique(),
            placeholder='Escolha uma opção',
            index=None
        )
        
        filter = (filter_option,filter_value)

    show_products(filter=filter)

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

    st.title(f"Grafo da melhor rota para {first_product}:")
    st.plotly_chart(fig)

def main():
    if 'stock' not in st.session_state:
        st.session_state['stock'] = Stock()
        st.session_state['store'] = Store(st.session_state['stock'])
        st.session_state['categories'] = [key.name for key in st.session_state.stock.sections_by_category.keys()]
    
    st.set_page_config('Sistema de Gerenciamento de Estoque', ':package:')

    pages = [
        "Home",
        "Adicionar Produto",
        "Remover Produto",
        "Listar Produtos",
        "Atualizar Produtos",
        "Calcular Rota"
    ]
    
    with st.sidebar:
        st.image('logo.jpg')
        menu = st.selectbox("Escolha uma opção", pages)

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
        show_route()

if __name__ == "__main__":
    main()