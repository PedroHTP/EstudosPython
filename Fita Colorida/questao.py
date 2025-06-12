fim = int(input())
Fita = list(map(int, input().split()))
dist = [10**9] * fim

for i in range(fim):
    if Fita[i] == 0:
        dist[i] = 0

for i in range(1, fim):
    dist[i] = min(dist[i], dist[i-1] + 1)

for i in range(fim-2, -1, -1):
    dist[i] = min(dist[i], dist[i+1] + 1)

for i in range(fim):
    if dist[i] > 9:
        dist[i] = 9

print(" ".join(map(str, dist)))  