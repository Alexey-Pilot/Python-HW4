m, n = int(input("Введите размер первого множества: ")), int(input("Введите размер второго множества: "))
print("Введите элементы первого множества: ")
nl = set([int(input()) for _ in range(n)])
print("Введите элементы второго множества: ")
ml = set([int(input()) for _ in range(m)])

total = nl.union(ml)
for i in total:
    if i in nl and i in ml:
        print(i, end=' ')