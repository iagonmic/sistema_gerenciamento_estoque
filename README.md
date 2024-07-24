# Introdução

Este guia orienta a implementação do Sistema de Gerenciamento de Estoque, abordando desenvolvimento, documentação e controle de versão.

# Estrutura do Projeto

1. Classe `Produto`
2. Classe `Estoque` (utilizando lista encadeada)
3. Funções de gerenciamento (adicionar, remover, atualizar, listar)
4. Demonstração da função de listas encadeadas no projeto com demonstrações de código.

# Implementação

Todas as funcionalidades abaixo serão implementadas em `main.py` visando alcançar o número mínimo de linhas pedidas pela professora.

## Classe Produto

## Classe Estoque

## Funções Principais

1. `adicionar_produto()`
2. `remover_produto()`
3. `atualizar_produto()`
4. `listar_produtos()`
5. `buscar_produto()`
6. `main()`

## Ciclo while True

Implementar while True na função main(), com opções a serem escolhidas abordando cada uma das funções implementadas, e uma opção para quebrar o ciclo, como o número "0" por exemplo.

Lembrar-se de incluir:

```python
if __name__ == '__main__':
    main()
```

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
   git clone (link_do_repositório) --> O link ainda será enviado no grupo do whatsapp do projeto pois o repositório ainda não foi implementado.
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

# Conclusão

Seguindo estas diretrizes, será desenvolvido um Sistema de Gerenciamento de Estoque com funçõe básicas bem documentado. Lembrar-se de comunicar regularmente, fazer commits frequentes e manter a documentação atualizada.