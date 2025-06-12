n = int(input().strip())
fita = list(map(int, input().split()))

# Inicializa distâncias com valor grande (maior que qualquer distância possível)
dist = [10**9] * n

# Primeiro: marcar posições onde há 0 com distância 0
for i in range(n):
    if fita[i] == 0:
        dist[i] = 0

# -1 -1 0 -1 -1 -1 0 -1
# 0
# Passagem da esquerda para a direita
for i in range(1, n):
    dist[i] = min(dist[i], dist[i-1] + 1)

# Passagem da direita para a esquerda
for i in range(n-2, -1, -1):
    dist[i] = min(dist[i], dist[i+1] + 1)

# Aplicar limite de distância (>=9 -> 9)
for i in range(n):
    if dist[i] >= 9:
        dist[i] = 9

print(" ".join(map(str, dist)))