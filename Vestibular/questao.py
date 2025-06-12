N = int(input())
G = str(input())
R = str(input())
C = 0

for i in range(0, N):
    if G[i:i+1] == R[i:i+1]:
        C += 1

print(C)