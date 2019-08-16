n = 234

# Loop 1 - finishes
print("Start Loop1")
i = 0
while i <= n:
    i += 1
    print(n)
print("End Loop1")

# Loop2 - finishes
print("Start Loop2")
i = 1
while True:
    i *= 2
    n += 1
    if i > n:
        break
    print(n)
print("End Loop2")

# Loop 3 - "Collatz conjectuse" unknown to anyone
print("Start Loop3")
while n != 1:
    if n % 2 == 0: #n is even
        n /= 2
    else:
        n = 3 * n + 1
        print(n)
print("End Loop3")
