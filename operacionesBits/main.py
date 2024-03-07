# Imprimir en binario el numero ingresado
# Checar valor de bit n (ingresado)
# Utilizando instrucciones logica poner en 0 el bit dado

number = int(input("Ingrese un numero: "))
bits = format(number,'b')
print(bits)
bit = int(input("Ingrese el bit n: "))
changed = number & (1 << bit)
print(format(number - changed,'b'))

# 15
# 1111
# Bit 1
# 1111 & 0010 = 0010
# 1111 - 0010 = 1101