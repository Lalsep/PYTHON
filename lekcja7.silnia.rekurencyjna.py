#silnia liczona rekurencyjnie
#n!=n*(n-1!)
def silnia(n):
    if n==0 or n==1:
        return 1
    else:
        return n*silnia(n-1)
n = int(input("Podaj liczbe calkowita dodatnia n < 20     \n"))
while n<0 or n>20:
    print("Podales licze spoza zakresu")
    break
else:
    a = silnia(n)
    print('silnia liczby', n, '! = ', a)
