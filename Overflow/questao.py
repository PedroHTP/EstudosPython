M = int(input())
S = list(map(str, input().split()))

if S[1] == "*":
    if int(S[0]) * int(S[2]) > M:
        print("OVERFLOW")
    else:
        print('OK')
else:
    if int(S[0]) + int(S[2]) > M:
        print("OVERFLOW")
    else:
        print('OK')