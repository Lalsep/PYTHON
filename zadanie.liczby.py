#Liczby z zakresu <1918;1939> podzielna przez 3 i przez 2
print("Liczby liczby z zakresu od 1918 do 1939 podzielne przez 3 i przez 2 jednocześnie \n")
for i in range(1918,1940):
    if i%3 == 0 and i%2 == 0:
        print("rok ", i, ". - ")
print("koniec listy")

