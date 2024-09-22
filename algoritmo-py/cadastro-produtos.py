# Criar um programa de cadastro de produtos
# receber nome produto e o preço
# função para exibir produtos cadastrados

produtos = {}


def cadastro():
    while True:
        nome = input("Nome do Produto: ")
        if nome != "":
            preco = float(input("Preço do Produto: "))
            produtos[nome] = preco
            print(f'Nome: {nome}, Preço: {preco}')
            print("Cadastrado com sucesso")
            print("---" * 20)
        else:
            print("Preencha o campo com o nome do produto.")
        break


def exibirProdutos():
    print("produtos cadastrados:")
    for nome, preco in produtos.items():
        print(f'Nome: {nome}, Preço: {preco}')


print("[1] Cadastrar Produto. [2] exibir produtos. [3] Sair.")

while True:
    try:
        option = int(input('Numero da opção: '))
        if option == 1:
            print("Cadastrar produto")
            cadastro()
        elif option == 2:
            if produtos != {}:
                exibirProdutos()
                print("---" * 20)
            else:
                print("Não há produtos cadastrados.")
                print("---" * 20)
        elif option == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida, tente novamente")
    except ValueError:
        print("Opção inválida, insira somente numeros!")
print("---" * 20)

