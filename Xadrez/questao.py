Linhas = int(input())
Colunas = int(input())
Tabuleiro = [[False for _ in range(Colunas)] for _ in range(Linhas)]
Tabuleiro[0][0] = True

for Y in range(Linhas):
    if Y > 0:
        Tabuleiro[Y][0] = not Tabuleiro[Y-1][0]
    for X in range(1, Colunas):
        Tabuleiro[Y][X] = not Tabuleiro[Y][X-1]


if Tabuleiro[Linhas-1][Colunas-1] == True:
    print(1)
else:
    print(0)