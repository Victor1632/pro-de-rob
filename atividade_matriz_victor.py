victor e david
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz completa:")
for linha in matriz:
    for num in linha:
        print(f"[{num:^5}]", end="")
    print()

soma_pares = sum(num for linha in matriz for num in linha if num % 2 == 0)
soma_coluna3 = sum(linha[2] for linha in matriz)
maior_segunda = sorted(matriz[1])[-1]

print(f"\nA) Soma dos pares: {soma_pares}")
print(f"B) Soma da terceira coluna: {soma_coluna3}")
print(f"C) Maior valor da segunda linha: {maior_segunda}")
