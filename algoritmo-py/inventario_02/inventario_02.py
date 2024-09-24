# Inventario
# Depreciação e exclusão
inventario = []
resposta = "S"

# Cadastro de equipamento
while resposta == "S":
    equipamentos = [input("Equipamento: "),
                    float(input("Valor: ")),
                    int(input("Número Serial: ")),
                    input("Departamento: ")]
    inventario.append(equipamentos)

    resposta = input("\nDigite \"S\" para continuar: ").upper()

# Exibe lista de equipamento
for elemento in inventario:
    print("Nome...........:", elemento[0])
    print("Valor..........:", elemento[1])
    print("Serial.........:", elemento[2])
    print("Departamento...:", elemento[3])
    print("---" * 10)

# Buscar equipamento
busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..........:", elemento[1])
        print("Serial.........:", elemento[2])

# Calculo de depreciacao de equipamento
depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

# Exclusão de equipamento
serial = int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# Exibe lista de equipamento com item excluido
for elemento in inventario:
    print("Nome...........:", elemento[0])
    print("Valor..........:", elemento[1])
    print("Serial.........:", elemento[2])
    print("Departamento...:", elemento[3])
    print("---" * 10)

# Exibe o equipamento mais caro e mais barato bem como o total
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))