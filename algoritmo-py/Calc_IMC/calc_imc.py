# Utilizando os conceitos de variáveis,
# operadores e controle de fluxo,
# crie um algoritmo que calcule o Índice de Massa Corporal (IMC) de uma pessoa.

# entrada de dados
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("DIgite sua altura (em metros): "))


# Função para calcular o IMC
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) baseado no peso e altura.
    Parâmetros:
    peso (float): O peso da pessoa em quilogramas.
    altura (float): A altura da pessoa em metros.
    Retorna:
    float: O valor do IMC, calculado como peso
    dividido pela altura ao quadrado.
    """
    imc = peso / altura ** 2
    return imc


imc = calcular_imc(peso, altura)

# Exibir resultado
print(f'O seu peso é {peso}kg, sua altura é {altura}m de altura, e o seu IMC é {imc:.2f}')