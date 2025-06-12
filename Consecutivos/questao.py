N = int(input())
V = list(map(int, input().split()))
S = []
P = 1

# 14
# 1 1 1 20 20 20 20 3 3 3 3 3 3 3
for i in range(0, N-1):

    if V[i] == V[i+1]:
        P += 1
    else:
        S.append(P)
        P = 1
    
    if i == N-2:
        S.append(P)

S.sort(reverse=True)
print(S[0])