ala = [2, 7, 1, 0, "kotek", 2]
print(ala)
x = ala[4]
print (x)
print(" to jest czwarty element listy ala : ", x)
for e in ala:
	print (e)
print ("to jest ilosc elementow listy ala ", len(ala))
print ("to jest poza petla")
ala.pop()
for e in ala:
	print (e)
