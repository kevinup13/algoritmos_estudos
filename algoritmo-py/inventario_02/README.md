# Inventário de Equipamentos
Este é um programa em Python que permite cadastrar, depreciar, excluir e visualizar equipamentos de um inventário. Ele armazena os dados dos equipamentos (nome, valor, número serial e departamento) e realiza diversas operações sobre eles, como busca, depreciação e exclusão.

## Funcionalidades
O programa oferece as seguintes funcionalidades:

1. Cadastro de Equipamentos: Permite inserir nome, valor, número serial e departamento dos equipamentos.
2. Exibição do Inventário: Lista todos os equipamentos cadastrados com seus respectivos detalhes.
3. Busca de Equipamentos: Localiza e exibe informações de um equipamento específico pelo nome.
4. Depreciação de Equipamentos: Aplica uma depreciação de 10% ao valor de um equipamento específico.
5. Exclusão de Equipamentos: Remove um equipamento do inventário pelo seu número serial.
6. Resumo do Inventário: Exibe o valor do equipamento mais caro, o mais barato e o valor total dos equipamentos.

## Como Utilizar
Siga os passos abaixo para utilizar o programa:

1. Cadastro de Equipamentos
O programa irá solicitar os seguintes dados para cada equipamento:
- Nome
- Valor
- Número Serial
- Departamento
- Para continuar adicionando equipamentos, digite "S" quando solicitado.

2. Exibição de Equipamentos
Após o cadastro, o programa exibirá todos os equipamentos com os seguintes detalhes:
- Nome
- Valor
- Número Serial
- Departamento

3. Busca de Equipamentos
O programa solicitará o nome de um equipamento para busca e, se encontrado, mostrará:
- Valor
- Número Serial

4. Depreciação de Equipamentos
Para depreciar o valor de um equipamento, insira o nome do equipamento. O valor será reduzido em 10%.

5. Exclusão de Equipamentos
Para excluir um equipamento, insira o número serial correspondente. O equipamento será removido do inventário.

6. Resumo do Inventário
O programa exibe:
- O equipamento mais caro
- O equipamento mais barato
- O valor total dos equipamentos restantes

## Requisitos
Python 3.x instalado

## Como Executar
1 - Baixe ou clone este repositório.
2 - Execute o script inventario.py no seu terminal ou ambiente Python.

# Contribuições
Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões para melhorias, fique à vontade para abrir uma issue ou fazer um pull request.