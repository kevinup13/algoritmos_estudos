# Sistema de Cadastro de Produtos
Este é um simples programa de cadastro de produtos que permite ao usuário registrar produtos com nome e preço e exibir os produtos cadastrados. O sistema é desenvolvido em Python e possui um menu interativo que facilita o uso.

# Funcionalidades
Cadastrar produtos com entrada de dados como "Nome" e "Preço".
Exibe a lista de produtos cadastrados com seus respectivos preços.

# Requisitos
Python 3.x: Certifique-se de ter o Python instalado para executar o programa. Você pode verificar se o Python está instalado usando o comando:
bash
Copiar código
python --version

# Como usar
Clone ou baixe este repositório.
Execute o script Python com o comando:

bash
Copiar código
```python cadastro_produtos.py```
O menu exibirá as seguintes opções:
[1] Cadastrar Produto: Permite que você insira o nome e o preço do produto.
[2] Exibir Produtos: Exibe todos os produtos cadastrados e seus respectivos preços.
[3] Sair: Encerra o programa.

# Exemplo de Uso
bash
Copiar código
[1] Cadastrar Produto. [2] exibir produtos. [3] Sair.
Numero da opção: 1
Nome do Produto: Teclado
Preço do Produto: 100.00
Nome: Teclado, Preço: 100.0
Cadastrado com sucesso
------------------------------------------------------------
[1] Cadastrar Produto. [2] exibir produtos. [3] Sair.
Numero da opção: 2
produtos cadastrados:
Nome: Teclado, Preço: 100.0
------------------------------------------------------------
# Tratamento de Erros
Validação de entrada: O programa verifica se as opções do menu são válidas (apenas números).
Campo de nome vazio: Se o nome do produto estiver em branco, o programa solicitará que o usuário preencha corretamente.
Melhorias Futuras
Implementar a possibilidade de remover e editar produtos cadastrados.
Salvar os produtos em um arquivo para persistência de dados.
Melhorar a interface do usuário com uma interface gráfica (GUI).
