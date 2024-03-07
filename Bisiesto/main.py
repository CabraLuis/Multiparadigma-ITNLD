year = int(input("Ingrese año: "))

flag = False
if year % 4 == 0:
    flag = True
    if year % 100 == 0:
        flag = False
        if year % 400 == 0:
            flag = True

if flag: 
    print("Bisiesto") 
else: 
    print("No bisiesto")

# Si es divisible /4 y no /100 es bisiesto
# Si es divisible /4, /100, y /400 es bisiesto