T1 = int(input())
T2 = int(input())
T3 = int(input())

A = [T1, T2, T3]
B = [T1, T2, T3]
B.sort()

for i in range(0, len(A)):
    if A[i] == B[0]:
        T1 = i + 1
    if A[i] == B[1]:
        T2 = i + 1
    if A[i] == B[2]:
        T3 = i + 1
        
print(T1)
print(T2)
print(T3)