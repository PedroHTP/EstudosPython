N = int(input())
Campo = []
Bombas = []

for x in range(0, N):
    Campo.insert(x, int(input()))
    Bombas.insert(x, 0)

# 0 1 1 0 1
for i in range(0, N):
    if Campo[i] > 0:
        Bombas[i] += 1

        if i > 0:
            Bombas[i-1] += 1

        if i < N-1:
            Bombas[i+1] += 1

for B in Bombas:
    print(B)