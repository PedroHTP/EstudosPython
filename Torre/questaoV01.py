N = int(input())
Posicao = [[0] * N for _ in range(N)]
Peso = [[0] * N for _ in range(N)]

for Y in range(N):
    Posicao[Y] = list(map(int, input().split()))

for Y in range(N):
    for X in range(N):
        # cima para baixo
        if Y < N-1:
            for A in range(Y+1, N):
                Peso[Y][X] += Posicao[A][X]
        
        # baixo para cima
        if Y > 0:
            for A in range(Y-1, -1, -1):
                Peso[Y][X] += Posicao[A][X]

        # esquerda para direita
        if X < N-1:
            for L in range(X+1, N):
                Peso[Y][X] += Posicao[Y][L]
        
        # direita para esquerda
        if X > 0:
            for L in range(X-1, -1, -1):
                Peso[Y][X] += Posicao[Y][L]

peso = 0
for Y in range(N):
    for X in range(N):
        if Peso[Y][X] > peso:
            peso = Peso[Y][X]
print(peso)