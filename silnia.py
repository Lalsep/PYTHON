#Tu policzymy silnię metodą iteracyjną
n=int(input("podaj liczbę rzeczywistą n= "))
silnia=1
if n==0 or n==1:
    silnia=1
if n==0 or n==1:
    silnia=1
else:
    for i in range(1,n+1):
        silnia*=i
print("silnia podanej liczby ",n,"!=",silnia)
