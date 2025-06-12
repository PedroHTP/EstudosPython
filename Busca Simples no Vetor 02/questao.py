valor = list(map(int, input().split()))
X = int(input())


if X in valor:
    print(valor.count(X))
    posicao = []
    for i in range(len(valor)):
        if valor[i] == X:
            posicao.append(i)
    print(" ".join(map(str, posicao)))
else:
    print('Mia x')