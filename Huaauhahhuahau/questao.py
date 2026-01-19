# A entrada é composta por uma linha, contendo uma sequência de no máximo 50 caracteres, formada apenas por letras minúsculas sem acentuação. As vogais são as letras ‘a’,‘e’,‘i’,‘o’,‘u’. A sequência contém pelo menos uma vogal.

ris = str(input())
vogais = ["a","e", "i","o","u"]
x = 'N'
sequencia1 = []
sequencia2 = []

for i in range(len(ris)):
    if ris[i] in vogais:
        sequencia1.append(ris[i])
    if ris[len(ris) - 1 - i] in vogais:
        sequencia2.append(ris[len(ris)-1-i])

if sequencia1 == sequencia2:
    x = 'S'

print(x)