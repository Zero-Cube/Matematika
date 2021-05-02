a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))
c = int(input("Zadaj c: "))

A = [a]
B = [b]
C = [c]

print("a = ",A)
print("b = ",B)
print("c = ",C)
print("____________")

#VZORCE
# x = ax^2 + bx + c
# f1 = y = ax^2 + bx + c
# Xv = -b / 2*a
# Yv = (Xv) * a^2 + b * (Xv) + c     ### Za x dosadime ==> Xv
dva_ = 2 * a
dva_a = a ** 2
f1 = f'{a ** 2} - {b} + {c}'
Xv = (-b) / dva_
xvdva = Xv * dva_a
bxv = Xv * b
print(f'f1 = y =  {a}ax² + {b}x + {c}')
print(f'f1 = y =  {a**2}ax² + {b}x + {c}')
print("________________________")
def XV():
    print("Xv = -b / 2 * a")
    print(f"Xv = (-{-b}) / 2 * {a}")
    print(f"Xv = (-{-b}) / {2 * a} ")
    print(f'Xv = {Xv}')
    print("________________________")
def YX():
    print(f'Yv = (Xv) * a² - (Xv) * b + c')
    print(f"Yv = ({Xv} * {a}²) - ({Xv} * {b}) + {c}")
    print(f"Yv= ({xvdva}) - ({-b * Xv}) + ({+c})")
    print("Yv = ", xvdva - -bxv + c)

XV(),YX()
print("=============================")
xv = -b / 2 * a
yv = xvdva - -bxv + c
V = [xv, yv]
print("V = ", V)
