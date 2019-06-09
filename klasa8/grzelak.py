import math
#zapytaj o wartości a,b i c
a=float(input("proszę podać watość a: "))
print (c)
b=float(input("proszę podać watość b: "))

print (c)
c=float(input("proszę podać watość c: "))
print (c)
#oblicz delte oraz ilosc odpowiedzi
delta = (b**2)-(4*a*b)
#oblicz k
k=(-b)/2/a
#oblicz x1 i x2
x1=(-b-delta**0.5)/(2*a)
x2 = (-b + delta**0.5)/(2*a)
if delta <0:
	print ("rownanie nie posiada rozwiazan rzeczywistych")
	if delta > 0:
		print ("rownanie ma jedno rozwiazanie, ", k)
#wypisac kierunek paraboli
if a>0:
	print ("prabola funkjic skierowana jest w gore")
if a < 0:
	print("prabola funkjic skierowana jest w dol")
if a==0:
	print ("rownainie nie jest rownainiem kwardratowym")
	print("prosze skontrolawac wartosci a, b, c")