#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
b = 2
c = "hello there"
print (a)
print (b)
print (c)


# In[2]:


number = 6
while number > 0:
    number -= 3
    print(number,end=' ')


# In[3]:


x = 0
while x<4:
    x=x+1
print ('x is ',x)


# In[4]:


x = 1
x *= x + 1
print (x)


# In[5]:


x = round(3.52)
print(x)


# In[6]:


x=7
if x%2 == 0:
    print("Liczba x jest parzysta")
else:
    print('Liczba x jest nieparzyta')


# In[7]:


count = 0
while count < 10:
    print("Welcome to Python")
    count += 1


# In[8]:


f = 2
g = 1
print ('f=',f,'  g=',g)
temp = f
f = g
g = temp
print('f=',f,'  g=',g)


# In[9]:


d = 2
b = 1
print (a)
print (b)
print (c)


# In[10]:


b = "ahhhhhhhhh"
print (a)
print (b)
print (c)


# In[11]:


print ("Hello world!")


# In[12]:


a = int(input("podaj liczbę całkowitą a:  "))
#print(a)
b = float(input("podaj wartość rzeczywistą b:  "))
#print (b)
#Poniżej zastosujemy konkatenację
print ("liczba a =  ",a)
print ("liczba b = ",b)


# In[13]:


a = 1
b = 2
c = 3
print(a,end=' ')
print (b,end=' ')
print (c,end=' ')
print (" koniec linii")


# In[14]:


#sposób zamiany zmiennych, czyli data swapping
a = 10
b = 20
print ("a= ",a, "b =  ",b)
#dokonujemy zamiany
c = a
a = b
b = c
print ("a= ",a, "b =  ",b)


# In[15]:


print ('dzień dobry klasa I LO')
print (3)


# In[16]:


#Obliczanie sumy zmiennych
print ("obliczanie sumy trzech zmiennych")
a = int(input("Podaj zmienną a= "))
b = int(input("Podaj zmienną b= "))
c = int(input("Podaj zmienną c= "))
suma = a + b + c
print ("suma trzech zmiennych a,b,c wynosi",suma)


# In[17]:


if a < b:
    print(a,"<",b)
else:
    if a == b:
        print ("a rowna sie b")


# In[18]:


x = int(input("Podaj wartość x  :"))
y = int(input("Podaj wartość y  :"))
z = int(input("Podaj wartość z  :"))
if x < y:
    print("x jest mniejsze od y")
else:
    print("x nie jest mniejsze od y")    
#tu kończy się działanie warunku
print("++++++++++++++++++++++++")
print("to jest drukowane poza warunkiem")
print("z = ",z)


# In[19]:


print(a+b)


# In[20]:


#Rozwiązanie równania liniowego
print("Znajdujemy punkty przecięcia równania prostej y=ax+b z osią OY oraz OX")
print (" ==================")
a = float(input("Podaj współczynnik a : "))
b = float(input("Podaj współczynnik b : "))
x0 = -b/a
print("przecięcie z osią OX prostej y=",a,"x+",b,"ma miejsce w punkcie Xo= ",x0)
print("przecięcie z osią OY prostej y=",a,"x+",b,"ma miejsce w punkcie Xo=0 dla współrzędnej Yo= ",b)
print ("Koniec obliczeń")


# In[21]:


#Rozwiązanie równania kwadratowego
print("Rozwiązujemy równanie kwadratowe y=ax^2+bx+c")
a = float(input("Podaj współczynnik a :"))
b = float(input("Podaj współczynnik b  :"))
c = float(input("Podaj współczynnik c :"))
print("Równanie kwadratowe postaci y=",a,"*x^2+",b,"*x +",c)
#obliczamy delte
delta = b**2-4*a*c
if delta < 0:
    print("Równianie nie ma rozwiązań rzeczywistych, delta < 0")
else:
    if delta == 0:
        print("Równanie ma jedno rozwiązanie Xo= ",-b/2/a)
    else:
        print("Równanie ma dwa rozwiązania")
        x1 = (-b-delta**0.5)/(2*a)
        x2 = (-b+delta**0.5)/(2*a)
        print("================")
        print("Pierwiastki są następujące X1 = ",x1," , X2 = ",x2)
print ("============")
if a > 0:
    print ("Parabola skierowana jest do góry")
else:
    if a < 0:
        print("Parabola skierowana jest do dołu")
if a == 0:
    print("a = 0, to nie jest równanie kwardratowe")
print("Koniec obliczeń")


# In[22]:


print(4%3)


# In[23]:


for x in range(0,3):
    print ("jestesmy w petli po raz ",x)


# In[24]:


n = int(input("podaj liczbę n = "))
print ("liczymy silnię liczby n = ",n)
silnia = 1
for i in range(1,n+1):
    m = i+1
    silnia = silnia*i
    for j in range(1,m):
        print(j,"*",end='')
    print('')
print ("silnia wynosi ",silnia)


# In[25]:


count = 0
while (count < 9):
    print ("the count is: ", count)
    count += 1


# In[26]:


print ("wypisz liczby parzyste podzielne przez 3 z zakresu 1-100")
for i in range(1,100):
    if((i%2 == 0) & (i%3 == 0) & (i%7 == 0)):
        print (i)
print ("goodbye")


# In[27]:


print (10%3)


# In[28]:


x = 1
x = x + 2.5
print (x)


# In[29]:


def function1():
    print("to jest funkcja")


# In[30]:


a = function1()
print (a)


# In[31]:


lst = ["pies", "kot", "żaba"]
print(lst)


# In[32]:


lst.pop()
print(lst)


# In[33]:


lst = [1, 2, 3, 4]
lst.append(5)
print(lst)
print('==========')
print('lista jako element listy')
lst.append([11, 33])
print(lst)


# In[34]:


lst.pop()
print(lst)


# In[35]:


lst = [1, 2, 3, 4]
print(lst)
lst.append(['jeden', 'dwa', 'trzy'])
print(lst)


# In[36]:


#listy
lst = ['mama', 'tata', 'bobas', ]
#print(lst[2])
for e in lst:
    print(e)


# In[37]:


lst =  list(range(1,11))
print (lst)


# In[38]:


x = int(input('podaj x :'))
if x%2 == 0:
    print('Liczba x jest parzysta')
else:
    print('liczba x jest nieparzysta')


# In[39]:


total = 0
for i in range(1,11):
    total +=i
print(total)


# In[40]:


lst = [1,2,3,4,5]
#x = len(lst)
#print (x)
print(len(lst))
#print.lengh(lst()) błędny zapis


# In[41]:


for i in range(5):
    print('Dzień dobry!')


# In[42]:


lst = [8, 3, 2, 0, -2, -4, -5]
total = 0
for i in range(len(lst)):
    if lst[i] < 0:
        total += lst[i]
print (total)


# In[43]:


lstn = ['Jacek', 'Ania', 'Zosia']
lsts = ['Kowalski', 'Nowak', 'Kwiatkowska']
for i in range(len(lstn)):
    print(lstn[i],' ',lsts[i])
    


# In[44]:


x=int(3.999)
print(x)


# In[45]:


lst = list(range(0,10))
print(lst)


# In[ ]:




