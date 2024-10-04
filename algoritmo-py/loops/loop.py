# Segundo algoritmo: implementar um loop simples (ex.: contar até 10)
# Criar um algoritmo que use um loop para realizar uma tarefa repetitiva, como contar até 10 ou somar uma série de números.

print("Loop usando (for)")
for i in range(1, 11):
    print(f'Numero: {i}')
    i += 1

print("\nLoop usando (while)")

num = 1
while num <= 10:
    print(num)
    num += 1