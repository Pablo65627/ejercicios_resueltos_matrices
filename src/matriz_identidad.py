# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)


def esMatrizIdentidad(matrix):
    if len(matrix)<2:
         return False 
    for row in range(len(matrix)):
            if len(matrix[row]) != len(matrix):
                return False
            else:
                for item in range(len(matrix)):
                    if (row == item and matrix[row][item] != 1) or (row != item and matrix[row][item] != 0):
                        return False
    return True


if __name__ == '__main__':
    # Casos Test:

    matrix1 = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix1) is True

    matrix2 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 0]]

    assert esMatrizIdentidad(matrix2) is False

    matrix8 = [[1, 0, 1],
               [0, 1, 0],
               [0, 0, 0]]

    assert esMatrizIdentidad(matrix8) is False

    matrix3 = [[2, 0, 0],
               [0, 2, 0],
               [0, 0, 2]]

    assert esMatrizIdentidad(matrix3) is False

    matrix6 = [[1, 0, 0, 0],
               [0, 1, 0, 2],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix6) is False

    matrix7 = [[1, -1, 1],
               [0, 1, 0],
               [0, 0, 1]]

    assert esMatrizIdentidad(matrix7) is False


    # casos test que no satisfacen la precondicion de que la matrix sea cuadrada:

    matrix4 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix4) is False

    matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esMatrizIdentidad(matrix5) is False

    matrix9 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esMatrizIdentidad(matrix9) is False
