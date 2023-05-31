palavra= "PYTHON"
chances = 6
letras_corretas = []
letras_erradas = []

print ("-"*35)
print ("    BEM VINDO AO JOGO DA FORCA  ")
print ("-"*35)

print("Sua dica é: linguagem de programação")

while True:
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\nChances restantes: ", chances)
    print("Letras erradas: ", letras_erradas)

    if len(letras_corretas) == len(set(palavra)):
        print("Parabéns! Você venceu!")
        break

    if chances == 0:
        print("Você perdeu! A palavra secreta era", palavra)
        break

    tentativa = input("Digite uma letra: ").upper()

    if tentativa in palavra:
        letras_corretas.append(tentativa)
    else:
        letras_erradas.append(tentativa)
        chances -= 1

    print("\n")