numero_secreto = 42
palpite = int(input("Adivinhe o número secreto: "))

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")
