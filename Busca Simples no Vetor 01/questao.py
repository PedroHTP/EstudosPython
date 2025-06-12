X = list(map(int, input().split()))
N = int(input())
N = X.count(N)
if N > 0:
    print('SIM')
else:
    print('NAO')