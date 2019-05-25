# n = 10
# n+=1
# print ("zmienna n wynosi ", n)
# # zadanie pk5
# j=1
# while j < 7:
# 	print("kolejna petla")
# 	j+=1
# 	if j == 3:
# 		break
# # zadanie 6
# n = 0
# lst = [1]
# while n < 9:
# 	m = lst[n]/2
# 	lst.append(m)
# 	n+=1
# print (lst)
# # zadanie 19
# for n in range (1,20):
# 	if n%3 == 0 and n%5 != 0:
# 		print("bum", end=", ")
# 	if n%3 != 0 and n%5 == 0:
# 		print ("bęc", end=", ")
# 	if n%3 ==0 and n%5 == 0:
# 		print ("bingo", end= ", ")
# # zadanie 8
# lt = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
# tot1 = 0
# j=0
# while j < len(lt):
# 	tot1 += lt[j]
# 	if lt[j]>0:
# 		break
# 	j+=1
# print(tot1)
# zadanie 9
lst = [-9,-7,-5,-4,-3,-2,-1,3,4,5,6,9,10]
suma = 0
j = len(lst)-1
while (lst[j] > 0) and (j>=0):
	suma += lst[j]
	j-=1
print(suma)
# zadanie 10
suma = 0
j = 0
while True:
	suma += lst[j]
	j += 1
	if lst[j] > 0:
		break
print (suma)
# zadanie 18
j =0
while j<10:
	if j%3 ==0:
		print(2**j, end=", ")
	j += 1