N = int(input())
X = list(map(float, input().split()))

for i in range(N):
    X[i] = X[i] ** (1/2)
    print(f"{X[i]:.4f}")