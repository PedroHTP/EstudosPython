N1 = int(input())
N2 = int(input())
X = []

if  N1 > N2:
    N = N1
    N1 = N2
    N2 = N

for i in range(N1, N2+1):
    X.append(i)
    X.sort()

print(" ".join(map(str, X)))