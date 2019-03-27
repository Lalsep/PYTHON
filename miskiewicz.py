#zad 16
n = int(input("odaj liczbe calkowia n = "))
if n%2 == 0:
    print("liczba n = ", n , " jest parzysta")
else:
    print("liczba n = ", n , " jest nieparzysta")

#zad 17

for i in range (1,101):
    if i%2 ==0 and i%7 == 0:
        print(i)
