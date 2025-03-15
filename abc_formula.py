import math

a = float(input("Oppgi koeffisienten a: "))
b = float(input("Oppgi koeffisienten b: "))
c = float(input("Oppgi koeffisienten c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("Likningen har ingen reelle løsninger.")
elif discriminant == 0:
    x = -b / (2*a)
    print("Likningen har én løsning: x =", x)
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Likningen har to løsninger: x1 =", x1, "og x2 =", x2)
