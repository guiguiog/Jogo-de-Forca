palavra = "sushi"
letras_usuario = []
chances = 4
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print('_', end=" ")
        
    print(f"você tem {chances} tentativas")
    tentativa = input("Escolha uma letra para adivinhar")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"parabéns, você ganhou, a palavra era: {palavra}")
else:
    print(f"você perdeu, a palavra era: {palavra}")
