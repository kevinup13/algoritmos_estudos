from funcoes import soma

numeros = []
while True:
    entrada = input("Digite um numero (ou 'sair' para encerrar).")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um numero válido!")

    finally:
        continue

print(f'A soma dos numeros {numeros} é:')
print(soma(numeros))