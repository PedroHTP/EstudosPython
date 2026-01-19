N = int(input())
camisasJ = list(map(int, input().split()))
camP = int(input())
camM = int(input())
camPJ = camisasJ.count(1)
camMJ = camisasJ.count(2)

if camP == camPJ and camM == camMJ:
    print('S')
else:
    print('N')
