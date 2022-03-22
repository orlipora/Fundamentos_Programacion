'''
Dados descripción y precio de producto, calcular total general factura.

Consultar si se desea seguir ingresando, caso contrario imprimir el valor total con IVA 10.5 y 21%.
'''
producto = "moto"
precio = 1500
iva = 21
iva_f = 1.21
cantidad = 1
cant_agregada = 0
print()
print("Ha comprado una ",producto,"  precio $ ",precio,"con iva ",iva,"%")
print()

cant_agregada = int(input("Desea agregar mas cantidad , ingrese nº entero :  "))
print()
factura = (cantidad +cant_agregada )* precio * iva_f
print("El Total de su Compra es : ", factura)
print()