number= input("Inserte numero a probar:")
listanumber = list(number)
a = 1


'''Conseguir la multiplicacion de los digitos'''
for number in listanumber:
    a *= int(number)
print(f"La multiplicacion de los digitos del numero es: {a} \n\n")


'''Reordenar de manera inversa los digitos'''
b = list(reversed(listanumber))
print(f"El reverso del numero insertado es: {b} \n\n")