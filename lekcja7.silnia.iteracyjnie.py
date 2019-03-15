#liczymy silnie iteracyjnie
silnia=1
n=int(input("Podaj wartosc n : "))
print("liczymy silnie liczby", n, "! =")
for i in range (1,n+1):
    silnia*=i
print("silnia", n , "! = ", silnia)
