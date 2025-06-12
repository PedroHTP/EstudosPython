N = int(input())
X = list(map(int, input().split()))
IndiceMaior = X.index(max(X))

soma = 0
for i in range(N):
    if i < IndiceMaior:
        soma += X[i]
print(soma)

soma = 0
for i in range(N):
    if i > IndiceMaior:
        soma += X[i]
print(soma)