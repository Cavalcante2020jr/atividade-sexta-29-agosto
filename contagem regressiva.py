num = int(input("Digite um número inteiro positivo: "))

print("Contagem regressiva de ímpares:")
for i in range(num, 0, -1):
    if i % 2 != 0:
        print(i)
