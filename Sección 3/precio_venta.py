"""
Calcular el Precio de Venta

Enunciado: Dado el valor de venta de un producto, se debe calcular el
Impuesto General a las Ventas (IGV) que es del 18%, y a partir de eso,
determinar el precio de venta final.

Mejora: En esta práctica, vamos a crear un programa en Python que permita
al usuario ingresar el valor de venta del producto. Luego, el sistema
realizará los cálculos necesarios para hallar el IGV y el precio de venta
final.
"""

# Solicitar al usuario que ingrese el valor de venta
valor_venta = float(input('Ingrese el valor de venta del producto:'))

# Calcular el IGV (18% del valor de venta)
igv = valor_venta * 0.18

# Calcular el precio de venta final
precio_venta_final = valor_venta + igv

# Mostrar los resultados al usuario
print('El IGV es: ', igv)
print('El precio de venta final es: ', precio_venta_final)