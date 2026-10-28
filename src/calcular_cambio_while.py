"""

coding = utf-8


Define un prodecimiento, euros, que toma como entrada un entero positivo en euros
y devuelve el número de monedas de 5 céntimos, de 2 cénts. y de 1 cénts. requeridos
para formar ese valor. El valor retornado debe ser una lista de tres números:
el número de monedas de 5 cénts, de 2 cénts. y de 1 cénts. necesarias.
Tu respuesta debe usar el menor número posible usandp primero cuantas más monedas
de 5 cénts posible, luego de 2 y finalmente de 1 (para sumar el total)
"""

def calcular_cambio(pago):

    tipos_de_mondedas = [5, 2, 1]

    numero_de_monedas = [0, 0, 0]

    moneda_index = 0

    while pago > 0 and moneda_index < len(tipos_de_mondedas):
        numero_de_monedas[moneda_index] = pago // tipos_de_mondedas[moneda_index]
        pago = pago % tipos_de_mondedas[moneda_index]
        moneda_index += 1
    return numero_de_monedas


# print(calcular_cambio(8))
assert calcular_cambio(8) == [1, 1, 1]
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
# print(calcular_cambio(5))
assert calcular_cambio(5) == [1, 0, 0]
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.

assert calcular_cambio(2) == [0, 1, 0]

assert calcular_cambio(1) == [0, 0, 1]

# print(calcular_cambio(29))
assert calcular_cambio(29) == [5, 2, 0]
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.

assert calcular_cambio(235) == [47, 0, 0]

# print(calcular_cambio(0))
assert calcular_cambio(0) == [0, 0, 0]
# >>> [0, 0, 0] # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.

assert calcular_cambio(-1) == [0, 0, 0]
