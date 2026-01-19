H, P, F, D = map(int, input().split())

while True:
    if F == P:
        print('N')
        break
    if F == H:
        print('S')
        break

    F += D

    if F == 16:
        F = 0

    if F == -1:
        F = 15