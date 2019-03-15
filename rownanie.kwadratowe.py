#liczymy pierwiastki rowania kwadratowego
import math
print('podaj wspolczynniki rownania kwadratowego \n')
a = float(input ('a ='))
b= float(input('b ='))
c = float(input('c ='))
print('liczymy delte \n')
delta = b*b - 4*a*c
if delta < 0:
    print('rownanie nie ma rozwiazan rzeczywistych')
else:
    if delta == 0:
        print ('jedno rozwiazanie x = ' , -b/2/a)
    else:
        print ('dwa rozwiazania  x1 =', (-b - math.sqrt(delta)/2/a), 'x2 = ', 
(-b + math.sqrt(delta)/2/a))
               
