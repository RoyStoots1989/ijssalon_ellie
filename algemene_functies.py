def kwadraat(x):
    return x ** 2
mijn_functie_1 = kwadraat
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

def bereken(a,b):
    return [a+b, a-b, a*b,a//b]
mijn_functie_2 = bereken
print(bereken(12,3))
print(bereken(12,2))
print(bereken(10,5))
print(bereken(100,20))