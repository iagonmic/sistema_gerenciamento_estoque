# Introdução

Este guia orienta a implementação do Sistema de Gerenciamento de Estoque, abordando desenvolvimento, documentação e controle de versão.

# Estrutura do Projeto

1. Classe `Produto`
2. Classe `Estoque` (utilizando lista encadeada)
3. Classe `LinkedList`
4. Funções de gerenciamento (adicionar, remover, atualizar, listar)

# Implementação

Todas as funcionalidades abaixo serão implementadas em `main.py` visando alcançar o número mínimo de linhas pedidas pela professora.

## Funcionalidades

### Classe Produto (hertz)

### Classe Estoque (hertz)

### Classe LinkedList (hertz)

### Funções Principais

1. `adicionar_produto()` (cauã)
2. `remover_produto()` (cauã)
3. `atualizar_produto()` (hertz)
4. `listar_produtos()` (iago)
5. `buscar_produto()` (iago)
6. `buscar_por_categoria(categoria)` (hertz) --> Busca mais complexa e específica.
7. `ordenar_por_quantidade()` (iago) --> Ordena a lista de produtos por quantidade (do maior para o menor).
8. `get_action(string)` (cauã)
9. `main()`(cauã)

### Ciclo while True

Implementar while True na função main(), com opções a serem escolhidas abordando cada uma das funções implementadas, e uma opção para quebrar o ciclo, como o número "0" por exemplo.

Lembrar-se de incluir:

```python
if __name__ == '__main__':
    main()
```

## Responsabilidade de implementação do projeto pelos membros

A responsabilidade de cada um ainda foi definida através de uma chamada via discord.

# Boas Práticas

## Comentários no Código

Usar comentários para explicar a lógica complexa e docstrings para funções e classes.

Exemplo:

```python
def buscar_produto(self, id):
    """
    Busca um produto no estoque pelo ID.

    Args:
        id (int): O ID do produto a ser buscado.

    Returns:
        Produto: O produto encontrado ou None se não existir.
    """
    # Implementação da busca
```

## Tratamento de Erros

Usar blocos try/except para lidar com possíveis erros:

```python
try:
    produto = estoque.buscar_produto(id)
    if produto:
        print(f"Produto encontrado: {produto.nome}")
    else:
        print("Produto não encontrado.")
except Exception:
    print(f"Erro ao buscar produto.")
```

# Controle de Versão com GitHub

## Configuração Inicial

Clone o repositório localmente:
   ```
   git clone https://github.com/iagonmic/sistema_gerenciamento_estoque.git
   ```

## Fluxo de Trabalho

1. Criar uma branch para cada nova feature:
   ```
   git checkout -b feature/adicionar-produto
   ```

2. Fazer commits frequentes com mensagens descritivas:
   ```
   git commit -m "Implementa função de adicionar produto"
   ```

3. Fazer um push para o GitHub:
   ```
   git push origin feature/adicionar-produto
   ```

4. Abrir um Pull Request para revisão do código

## Documentação de Erros

1. Usar as Issues do GitHub para rastrear erros
2. Ao encontrar um bug:
   - Criar uma nova Issue descrevendo o problema
   - Adicionar labels relevantes (ex: "bug", "high-priority")
   - Atribuir a um membro da equipe, ou você mesmo caso seja o responsável

3. Ao resolver um bug:
   - Referenciar o número da Issue no commit:
     ```
     git commit -m "Corrige erro na atualização de quantidade (#42)"
     ```
   - Fechar a Issue através do Pull Request ou manualmente
  

# Apresentação

## Estrutura da apresentação

A apresentação será feita de acordo com a seguinte ordem:

1. Introdução
2. Objetivos do Projeto
3. Estruturas Utilizadas
4. Demonstração das Classes Produto e Estoque
5. Funções Principais
6. Demonstração do Código Rodando na IDE
7. Mostrar os desafios enfrentados
8. Soluções adotadas pelo projeto
9. Conclusão e Perguntas

## Falas dos membros

Atenção: As seguintes falas servem de guia para o que será falado. Fique a vontade para incrementar mais coisas de acordo com o seu entendimento do projeto.

### Iago Flávio

(A ser definido)

### Hertz Rafael

(A ser definido)

### Cauã Wendel

(A ser definido)

## Ordem das falas

A ordem das falas ainda será definida de acordo com a implementação do projeto por parte de cada um.

# Conclusão

Seguindo estas diretrizes, será desenvolvido um Sistema de Gerenciamento de Estoque com funções básicas bem documentado. Lembrar-se de comunicar regularmente, fazer commits frequentes e manter a documentação atualizada.