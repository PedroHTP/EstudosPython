Linha = [0 for _ in range(3)]

for Y in range(3):
    for X in range(3):
        Linha[Y] += (int(input()))

for Y in range(3):
    print("Linha " + str(Y) + ": " + str(Linha[Y]))