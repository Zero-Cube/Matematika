
x1 = int(input("Zadaj X:"))
y1 = int(input("Zadaj Y:"))
x2 = int(input("Zadaj X:"))
y2 = int(input("Zadaj Y:"))

Q = [x1, y1]
P = [x2, y2]
q = 1

print("Q =", Q)
print("P =", P)
print("____________")

# Y = kx + q
Y1: y1 = x1 + q
Y2: y2 = x2 + q
Y_vysledok = y1 - y2
kx = Y1-Y2
X = Y_vysledok/kx
na = X * x1
q_ = kx * x1

print(f'{y1} = {x1}kx + q')
print(f'{y2} = {x2}kx + q')
if Y_vysledok == 0 :                                           #Y je väčšie ako 0
    print("============")
    print(f'{Y_vysledok}y = {kx}kx')
    print("____________")
    print("kx =", kx)
    print("============")
    print(f'{y1} = ({kx}) * {x1} + q')
    print(f'{y1} = {kx * x1}q /({y1})')
    print("============")
    print(f'q = {y1 // q_:.1f}')

if Y_vysledok <= -1:
    print("============")
    print(f'{Y_vysledok} = {kx}kx')
    print(f'{Y_vysledok} = {kx}kx / {Y_vysledok}')
    print("____________")
    print(f'kx = {Y_vysledok / kx}')
    print("============")
    print(f'{y1} = {X} * {x1} + q')
    print(f'{y1} = {X * x1:.1f}q /({y1})')
    print("============")
    print(f'q = {y1/na :.1f}')

if Y_vysledok >= -1:
    print("============")
    print(f'{Y_vysledok} = {kx}kx')
    print(f'{Y_vysledok} = {kx}kx / {Y_vysledok}')
    print("____________")
    print(f'kx = {Y_vysledok / kx:.2f}')
    print("============")
    print(f'{y1} = {X:.2f} * {x1} + q')
    print(f'{y1} = {X * x1:.1f}q /({y1})')
    print("============")
    print(f'q = {y1/na :.1f}')