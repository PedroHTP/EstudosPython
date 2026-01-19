import random

def brute(n, m, anot):
    """Resposta correta por força bruta (só para n pequeno)."""
    best = None
    for mask in range(1 << n):
        arr = []
        for i in range(n):
            if (mask >> i) & 1:
                arr.append(m - anot[i])
            else:
                arr.append(anot[i])

        ok = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                ok = False
                break

        if ok:
            s = sum(arr)
            if best is None or s < best:
                best = s

    return -1 if best is None else best


def fast(n, m, anot):
    soma = -1

    def min_max(x):
        x = m - x
        return x
        
    for i in range(n-1):
        if anot[i] > anot[i+1]:
            if min_max(anot[i]) < anot[i+1]:
                anot[i] = min_max(anot[i])
            if anot[i] <= min_max(anot[i+1]):
                anot[i+1] = min_max(anot[i+1])

    for i in range(n):
        if min_max(anot[i]) <= anot[i]:
            if (i != 0):
                if i < n-1:
                    if (anot[i-1] <= min_max(anot[i])) and (min_max(anot[i]) <= anot[i+1]):
                        anot[i] = min_max(anot[i])
                else:
                    if (anot[i-1] <= min_max(anot[i])):
                        anot[i] = min_max(anot[i])
            else:
                anot[i] = min_max(anot[i])

    if n == 1:
        if min_max(anot[0]) < anot[0]:
            anot[0] = min_max(anot[0])

    if anot == sorted(anot):
        soma = sum(anot)

    return soma


def stress(trials=20000, n_max=12, m_max=30):
    for t in range(trials):
        n = random.randint(1, n_max)
        m = random.randint(1, m_max)
        anot = [random.randint(0, m) for _ in range(n)]

        b = brute(n, m, anot)
        f = fast(n, m, anot.copy())  # copy porque seu código pode alterar a lista

        if b != f:
            print("MISMATCH!")
            print("n m:", n, m)
            print("anot:", anot)
            print("brute:", b)
            print("fast :", f)
            return

    print("Sem divergências nesses testes.")


if __name__ == "__main__":
    stress()
