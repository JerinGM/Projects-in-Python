a = int(input("first number\n"))
b = int(input("second number\n"))
n = int(input("the value of n\n"))
s = 0
i = 0
print(f"{a} {b}", end=' ')
while i <= n:
    s = a + b
    print(s, end=' ')
    a = b
    b = s
    i += 1
