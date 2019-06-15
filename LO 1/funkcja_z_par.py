#a teraz funkcja z parametrem
def moja_funkcja(x):
	return 2*x
x = 2
a = moja_funkcja(x)
print (a)
#a to zmienna, która zwraca wynik działania funkcji z parametrem
x = int (input("Podaj dowolną liczbe  "))
print ('podałeś x  =  ', x)
print('a teraz zastosujemy funkcję z argumentem x  ')
a = moja_funkcja(x)
print (a)

# a teraz kalkulator BMi

def bmi (wzrost, waga):
	return waga/(wzrost**2)

imie = input("podaj swoje imię imię     ")
print ("witaj, " + imie + "  !")
wzrost = float(input("podaj swoj wzrost w m  "+imie+"  !"))
waga = float(input(" ile ważysz w kg, "+imie+"  ?"))
bm = bmi(wzrost, waga)
print (imie+"  !, twoj wskaźnik bmi wynosi bmi =  ", bm)
if(bm<18.5):
	if(bm<16):
		print('jestes chudzielcem')
	else:
		print('masz niedowage')
if (bm<25 and bm>=18.5):
	print('twoja waga jest w normie')
if(bm>=25):
	if(bm>30):
		print('jestes grubasem, musisz koniecznie schudnąc dla twojego zdrowia')
	else:
		print('masz nadwage, musisz przejsc na diete')
print ('dziekuje za rozmowe')


