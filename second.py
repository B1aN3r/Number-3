a = int(input())
b = int(input())
c = int(input())

n1 = (a**2 + b**2)
n2 = (3 * b - 4)
n3 = (4 * c**5 / 6)

a = ((n1 / n2) // n3)
print(a)

b = ((n1 / n2) % n3)
print(b)
