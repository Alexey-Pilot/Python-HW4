n = int(input("Введите колличество кустов: "))
x = [int(input(f"Введите урожайность куста № {i + 1}: ")) for i in range(n)]
prodMax = 0
for i in range(len(x)):
    prod = x[i] + x[i - 1] + x[i - 2]
    if prod > prodMax:
        prodMax = prod

print(f"Максимум ягод за один сбор: {prodMax}")