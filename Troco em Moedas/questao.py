C = int(input())
tipo = {
    100:0, 
    50:0, 
    25:0, 
    10:0, 
    5:0,
    1:0,
}

for x in tipo.keys():
    if C >= x:
        tipo[x] = C // x
        C = C % x

print(sum(tipo.values()))

for X in tipo.values():
    print(X)