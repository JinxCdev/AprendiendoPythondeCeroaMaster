"""
    Crea un programa en Python que simule un sistema de descuentos en un
    restaurante según el monto de consumo. El programa debe seguir las
    siguientes instrucciones:

    - Solicita al usuario que ingrese el monto de consumo en el restaurante.
    - Aplica descuentos según las siguientes reglas:
    - Si el monto de consumo es mayor a $50 pero igual o menor a $100, aplica un descuento del 10%.
    - Si el monto de consumo es mayor a $100 pero igual o menor a $200, aplica un descuento del 20%.
    - Si el monto de consumo es mayor a $200, aplica un descuento del 30%.
    - Si el monto de consumo es igual o menor a $50, no aplica ningún descuento.

    Muestra al usuario un resumen de la cuenta con el monto de consumo, el
    descuento aplicado y el monto final con descuento.
"""

consumo = float(input("Ingrese el monto de consumo en el restaurante: $"))

if consumo > 50 and consumo <= 100:
    descuento = 0.1
elif consumo > 100 and consumo <= 200:
    descuento = 0.2
elif consumo > 200:
    descuento = 0.3
else:
    descuento = 0.0

monto_descuento = consumo * descuento
total = consumo - monto_descuento

print('\nResumen de la cuenta')
print('Monto de consumo:', consumo)
print('Descuento aplicado:', descuento * 100, "%")
print('Monto final con descuento:', total)