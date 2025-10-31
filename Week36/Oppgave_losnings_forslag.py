m: int = int(input("Start på intervallet: "))
n: int = int(input("Slutt på intervallet: "))

width: int = max(len(str(m + n)), len(str(n + n)))

print("|", end="")
for j in range(m, n+1):
    print(str(j).rjust(width), "|", end="")
print()

print("|", end="")
for _ in range(m, n +1):
    print("-" * width, "|", end="")
print()

for i in range(m, n +1):
    print("|", end="")
    for j in range(m, n +1):
        value = i + j
        print(str(value).rjust(width), "|", end="")
    print()
