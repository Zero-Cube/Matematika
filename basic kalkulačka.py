

cislo1 = float(input("Zadaj čislo: "))
znamienko = input("Zadaj znamienko: ")
cislo2 = float(input("Zadaj čislo: "))
if znamienko == "+":
    print(float(cislo1 + cislo2))
elif znamienko == "-":
    print(float(cislo1-cislo2))
elif znamienko == "*":
    print(float(cislo1*cislo2))
elif znamienko == "/":
    print(float(cislo1/cislo2))
else:
    print("ERROR 404")
