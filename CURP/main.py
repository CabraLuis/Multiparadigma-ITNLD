apellidoPaterno = input("Ingrese el apellido paterno: ")
apellidoMaterno = input("Ingrese el apellido materno: ")
primerNombre = input("Ingrese el primer nombre: ")

apellidoPaternoCortado = apellidoPaterno[:2]

CURP = apellidoPaternoCortado + apellidoMaterno[0] + primerNombre[0]

print(CURP.upper())