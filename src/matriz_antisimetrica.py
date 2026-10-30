# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is esAntisimetrica and False otherwise.
# An nxn square is called esAntisimetrica if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def esMatrizCuadrada(matriz):

    numeroFilas = len(matriz)

    for fila in matriz:

        if len(fila) != numeroFilas:

            return False

    return True

def esAntisimetrica(matriz):

    if not esMatrizCuadrada(matriz):

        return False

    fila = 0

    while fila < len(matriz):

        columna = 0

        while columna < len(matriz[fila]):

            if matriz[fila][columna] != -matriz[columna][fila]:

                return False

            columna += 1

        fila += 1

    return True


# CASOS DE PRUEBA

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, 3],
                       [-2, -3, 0]]))
# Resultado: True

print(esAntisimetrica([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]))
# Resultado: True

print(esAntisimetrica([[0, 1, 2],
                       [-1, 0, -2],
                       [2, 2, 3]]))
# Resultado: False

print(esAntisimetrica([[1, 2, 5],
                       [0, 1, -9],
                       [0, 0, 1]]))
# Resultado: False


# MATRICES QUE NO SON CUADRADAS

matriz4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(esAntisimetrica(matriz4))
# Resultado: False

matriz5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(esAntisimetrica(matriz5))
# Resultado: False