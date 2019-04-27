a = 2
b = 3
print (a)
print (b)
#drukowanie, łaczenie z łańcuchem
print ("=============")
print ("a = ", a)
print ("b = ", b)
print("a = ", a, ", b = ", b)
print("wyswietlamy liczby od 1 .. do .. 10")
for i in range(1,11):
    print (i,end=", ")
print("")
#data swapping
print ("zamieniamy dane zapisane w zmiennych a, b")
print ("przed zamianą")
print("a = ", a)
print ("b = ", b)
print ("zamiana ->")
temp = b
b = a
a = temp
print ("po zamianie")
print("a = ", a)
print ("b = ", b)
