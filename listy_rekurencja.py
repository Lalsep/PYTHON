#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [2, 3, 4, 5]
print(a)


# In[2]:


for e in a:
    print(e, end=", ")
#print("\n", end='')
print('')
print('koniec listy')


# In[8]:


a.append(6)
print(a)


# In[9]:


a.pop()
print(a)


# In[10]:


a.pop()
print(a)


# In[12]:


a.append(5)
print(a)


# In[14]:


a.pop()


# In[16]:


for e in a:
    print(e,end=', ')
print('')
print('koniec listy')


# In[17]:


a = ['pies', 'żaba', 'bocian']
print(a)


# In[18]:


for e in a:
    print(e, end=', ')
print('')
print('koniec')


# In[19]:


print(a[1])


# In[20]:


print(a[0])


# In[21]:


a.append('kot')
for e in a:
    print(e, end=', ')
print('')
print('koniec')


# In[22]:


a.append('lubi')


# In[23]:


print(a)


# In[24]:


print(a[2], a[4], a[1])


# In[25]:


def drukowanie():
    for e in a:
        print(e, end=', ')
    print('')
    print('koniec')


# In[26]:


drukowanie()


# In[3]:


def suma(x, y):
    return x+y


# In[4]:


d = suma(3,4)


# In[5]:


print(d)


# In[6]:


def sumakw(x,y):
    return x*x + y*y


# In[7]:


f = sumakw(4,5)
print(f)


# In[8]:


#rekurencja
#silnia - factorial
# silnia oznaczana jest przez "!"
# 3! = 1*2*3=6


# In[9]:


#3! = 3*2!
#3! = 3*2*1! =6


# In[10]:


def silnia(n):
    if n <= 1:
        return 1
    else:
        return n*silnia(n-1)


# In[11]:


n = int(input('Podaj liczbę całkowitą dodatnią n<20:   '))
k = silnia(n)
print('szukana liczba ',n,'! =', k)


# In[ ]:





# In[ ]:




