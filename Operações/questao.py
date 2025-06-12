O = str(input())
N = list(map(float, input().split()))

if O == 'M':
    print(f"{(N[0] * N[1]):.2f}")
else:
    print(f"{(N[0] / N[1]):.2f}")