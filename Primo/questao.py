def eh_primo (N):
    for x in range(2, N, 1):
        if N % x == 0:
            return False
        elif x == N-1:
            return True

N = int(input())

if eh_primo(N):
    print("S")
else:
    print("N")