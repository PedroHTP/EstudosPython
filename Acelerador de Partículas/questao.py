dist = int(input())
com = 0

while True:
    if dist == 6 + com:
        saida = 1
        break
    if dist == 7 + com:
        saida = 2
        break
    if dist == 8 + com:
        saida = 3
        break
    com += 8

print(saida)