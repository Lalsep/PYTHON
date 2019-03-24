#liczymy pierwiastki rowania kwadratowego
import math
print('podaj wspolczynniki rownania kwadratowego \n')
a = float(input ('a ='))
while(true):
    if(a==0):
        print('a nie moze być zerem, niedozwolone dzilenie przez zero')
        break #koniec kodu tutaj
b= float(input('b ='))
c = float(input('c ='))
print('liczymy delte \n')
delta = b*b - 4*a*c
print ("delta wynosi ", delta)
if delta < 0:
    print('rownanie nie ma rozwiazan rzeczywistych')
else:
    if delta == 0:
        print ('jedno rozwiazanie x = ' , -b/2/a)
    else:
        print ('dwa rozwiazania  x1 =', (-b - math.sqrt(delta)/2/a), 'x2 = ', 
(-b + math.sqrt(delta)/2/a))
if (a > 0 ):
    print("parabola skierowana jest do góry")
else:
    print("parabola skierowana jest do dolu")
               
