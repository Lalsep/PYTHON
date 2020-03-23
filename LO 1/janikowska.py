#zadanie 16
n = int(input("Podaj liczbe calkowita n= "))
print("podales liczbe  ", n)
if (n%2 == 0):
    print("liczba na jest parzysta")
else:
    print("liczba n jest nieparzysta")

#zadanie 17
def print_factors(x):
    print("the factors of ", x , "are")
    for i in range(7, x+1):
        if x%i == 0:
            print(i)
num = 100
print_factors(num)
