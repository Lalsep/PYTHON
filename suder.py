#suder zad 17
for x in range(1,101):
    if x%7 == 0:
        if x%2 == 0:
            print(x)

#drugi sposob
print("liczyby te same liczy drugiem sposobem")
print("\n")
for x in range(1,101):
    if (x%7 == 0) and (x % 2 == 0):
        print(x)

