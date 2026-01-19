n, m = map(int, input().split())
anot = list(map(int, input().split()))
soma = -1

def min_max(x):
    x = m - x
    return x
    
for i in range(n-1):
    if anot[i] > anot[i+1]:
        if min_max(anot[i]) < anot[i+1]:
            anot[i] = min_max(anot[i])
        if anot[i] <= min_max(anot[i+1]):
            anot[i+1] = min_max(anot[i+1])

for i in range(n):
    if min_max(anot[i]) <= anot[i]:
        if (i != 0):
            if i < n-1:
                if (anot[i-1] <= min_max(anot[i])) and (min_max(anot[i]) <= anot[i+1]):
                    anot[i] = min_max(anot[i])
            else:
                if (anot[i-1] <= min_max(anot[i])):
                    anot[i] = min_max(anot[i])
        else:
            anot[i] = min_max(anot[i])

if n == 1:
    if min_max(anot[0]) < anot[0]:
        anot[0] = min_max(anot[0])

if anot == sorted(anot):
    soma = sum(anot)

print(soma)