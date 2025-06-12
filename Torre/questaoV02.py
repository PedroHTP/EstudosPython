N = int(input())
Posicao = [[0 for _ in range(N)] for _ in range(N) ] 
PesoY = [0 for _ in range(N)]
PesoX = [0 for _ in range(N)] 

for Y in range(N):
    Posicao[Y] = list(map(int, input().split()))

for Y in range(N):
    PesoY[Y] = sum(Posicao[Y])

for X in range(N):
    for Y in range(N):
        PesoX[X] += Posicao[Y][X]

Pesomax = 0
for Y in range(N):
    for X in range(N):
        if (PesoX[X] + PesoY[Y]) - 2 * Posicao[Y][X] > Pesomax:
            Pesomax = (PesoX[X] + PesoY[Y]) - 2 * Posicao[Y][X]

print(Pesomax)