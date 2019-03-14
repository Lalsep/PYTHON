#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = [3,4,5,8]
print(a)


# In[70]:


print (a)


# In[71]:


for e in a:
    print(e,end=', ')
print('\n')
print('Koniec listy')


# In[3]:


for e in a:
    print(e)
print('\n')
print('Koniec listy')


# In[4]:


a.append(9)


# In[5]:


a.append('lista jest długa')


# In[6]:


print(a)


# In[7]:


a.pop()


# In[75]:


print(a)


# In[76]:


for e in a:
    print(e,end=', ')


# In[77]:


a.append(['pies', 'żaba', 'bocian'])


# In[78]:


print(a)


# In[79]:


b = ['Jacek', 'jest', 'pies', 'baby', 'lubi', 'na']
print(b[3])


# In[80]:


print(b[0],b[4],b[3])


# In[81]:


print(b[0],b[1],b[2],b[5],b[3])


# In[82]:


#definicje
def silnia(n):
    if n <= 1: #początek silni zaczynan sie od jedynki
        return 1
    else:
        return n * silnia(n-1)


# In[54]:


n = int(input('Podaj liczbę całkowitą dodatnią n<20:  '))
a = silnia(n)
print(a)


# In[ ]:




