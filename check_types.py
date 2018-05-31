import fractions

def check_types():
    print(5/6)
    print(5//6)
    print("Ege"
          "Gey")
    print('''Sha
             La
             La''')
    print( type(1.0))
    print(type(2/3))
    print(isinstance(1, int))

    a = fractions.Fraction(15, 10)
    b = fractions.Fraction(7, 4)

    print("Fractions")
    print(a)
    print(b)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

check_types()