from store import Store
from estoque import Stock
import streamlit as stl
import plotly.graph_objs as go
import networkx as nx

def get_graph(arestas):
    graph = nx.Graph()
    
    for first_product, last_product, distance in arestas:
        graph.add_edge(first_product, last_product, weight=distance)

    return graph

def plot_grafo(graph, edge_color, node_color, bg_color, font_size, layout_type, text_color, edge_width, node_size, box_color, box_size, node_text_color, width, height):
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
        pos = nx.spring_layout(graph)  # Padrão se o layout não for reconhecido

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
        showlegend=False, hovermode='closest',
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor=bg_color,  # Cor de fundo configurada pelo usuário
        width=1024,  # Largura da figura (definida diretamente no código)
        height=768  # Altura da figura (definida diretamente no código)
    )

    return fig

def main():
    
    # Opções de personalização definidas diretamente no código
    edge_color = "yellow"  # Cor das arestas
    node_color = "white"  # Cor dos nós
    text_color = "yellow"  # Cor do texto da distância
    node_text_color = "black"  # Cor do texto dentro dos nós
    bg_color = "#0e1117"    # Cor do fundo
    font_size = 25        # Tamanho da fonte
    edge_width = 4        # Grossura das arestas
    node_size = 100        # Tamanho dos nós
    layout_type = "circular"  # Tipo de layout
    box_color = "#0e1117"  # Cor da caixa de fundo para as distâncias
    box_size = (20, 20)  # Tamanho da caixa de fundo (largura, altura)

    # Exemplo de lista de arestas
    edge = [
        ('Arroz', 'Feijão', 1), 
        ('Feijão', 'Açúcar', 2), 
        ('Açúcar', 'Macarrão', 1), 
        ('Macarrão', 'Óleo', 3)
    ]
    
    graph = get_graph(edge)

    # Plotar o grafo com as configurações
    fig = plot_grafo(graph, edge_color, node_color, bg_color, font_size, layout_type, text_color, edge_width, node_size, box_color, box_size, node_text_color, 800, 600)  
    stl.plotly_chart(fig)

if __name__ == "__main__":
    main()








