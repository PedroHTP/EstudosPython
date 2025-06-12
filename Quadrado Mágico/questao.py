N = int(input())
Quadrado = [[] * N] * N
Magic = True
SomaX = [0] * N
SomaDe = 0
SomaDd = 0
 
for Y in range(N):
    Quadrado[Y] = list(map(int, input().split()))
    

# esquerda - direita
for Y in range(N-1):
    if sum(Quadrado[Y]) != sum(Quadrado[Y+1]):
        Magic = False
        break

# cima - baixo
for X in range(N):
    for Y in range(N):
        SomaX[X] += Quadrado[Y][X]

for X in range(N-1):
    if SomaX[X] != SomaX[X+1]:
        Magic = False
        break

Y = 0
# diagonal - esq a dir
for X in range(0, N):
    SomaDe += Quadrado[Y][X]
    Y += 1

Y = 0
# diagonal - dir a esq
for X in range(N-1, -1, -1):
    SomaDd += Quadrado[Y][X]
    Y += 1

if Magic and SomaX[0] == sum(Quadrado[0]) and SomaX[0] == SomaDd and SomaDd == SomaDe:
    print(SomaX[0])
else:
    print(-1)