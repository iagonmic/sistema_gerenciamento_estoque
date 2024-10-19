from store import Store
from estoque import Stock
import streamlit as stl
import plotly.graph_objs as go
import numpy as np

def mensage(products):
        print("-" * 89)
        print(f"|{'ID':<5}|{'Nome':<20}|{'Categoria':<20}|{'Quantidade':<12}|{'Preço':<12}||{'Vendas':<12}|")
        print("-" * 89)
        for product in products:
            print(f"|{product.id:<5}|{product.name:<20}|{product.category.name:<20}|{product.quantity:<12}|{product.price:<12}||{product.sales:<12}|")
        print("-" * 89)

def plot_grafo(grafo, bg_color, font_size):
    # Extraindo nós únicos
    nodes = list(set([item for edge in grafo for item in edge[:2]]))
    
    # Gerar posições circulares para os nós
    theta = np.linspace(0, 2 * np.pi, len(nodes), endpoint=False)  # Ângulos para o layout circular
    radius = 1  # Definindo um raio
    node_pos = {node: (radius * np.cos(angle), radius * np.sin(angle)) for node, angle in zip(nodes, theta)}
    
    # Criar as coordenadas das arestas e pesos (distâncias)
    edge_x = []
    edge_y = []
    edge_text = []
    for edge in grafo:
        x0, y0 = node_pos[edge[0]]
        x1, y1 = node_pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
        # Calculando a posição média e ajustando o texto para ficar um pouco acima da linha
        x_text = (x0 + x1) / 2
        y_text = (y0 + y1) / 2
        offset = 0.1  # Ajuste vertical (acima da linha)
        y_text += offset
        edge_text.append((x_text, y_text, edge[2]))  # Posição do texto (distância)

    # Plotar as arestas (linhas entre os nós)
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    # Criar a figura
    fig = go.Figure(data=[edge_trace])

    # Adicionar anotações para distâncias com deslocamento horizontal
    for (x_text, y_text, distance) in edge_text:
        fig.add_annotation(
            x=x_text,
            y=y_text,
            text=str(distance),  
            showarrow=False,
            arrowhead=2,
            ax=15,  # Ajuste horizontal (para a direita)
            ay=-10,  # Ajuste vertical
            font=dict(color='yellow', size=font_size)  # Cor e tamanho do texto
        )

    # Plotar os nós e os nomes dentro das bolas
    node_x = [node_pos[node][0] for node in nodes]
    node_y = [node_pos[node][1] for node in nodes]
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        marker=dict(size=50, color='white', line=dict(width=2)),
        text=[node for node in nodes],  # Nomes dos nós dentro das bolas
        textposition="middle center",  # Centralizar o texto dentro das bolas
        textfont=dict(size=14, color='black'),  # Texto branco dentro da bola
        hoverinfo='text'
    )

    # Adicionar nós ao gráfico
    fig.add_trace(node_trace)

    # Ajustar os eixos para evitar deformação no layout circular
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        plot_bgcolor=bg_color,  # Cor de fundo configurada pelo usuário
        paper_bgcolor=bg_color,  # Cor de fundo do papel configurada pelo usuário
        margin=dict(b=20, l=5, r=5, t=40),
        xaxis_range=[-1.5, 1.5],
        yaxis_range=[-1.5, 1.5],
        height=600, width=600
    )

    return fig

def main():
    # Definir a interface do Streamlit
    stl.title("Visualizador de Grafos com Distâncias")

    # Lista de arestas com distâncias (exemplo)
    grafo = [ ('arroz', 'feijão', 5), ('Leite', 'café', 4), ('café', 'feijão', 1)]

    bg_color = "#363636"

    font_size = 25

    # Plotar o grafo
    fig = plot_grafo(grafo, bg_color, font_size)

    # Exibir o gráfico no Streamlit
    stl.plotly_chart(fig)

if __name__ == "__main__":
    main()
    
    
