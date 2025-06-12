N = int(input())
X = list(map(int, input().split()))
X.sort()
print(" ".join(map(str, X)))