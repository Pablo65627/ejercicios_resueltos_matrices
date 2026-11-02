# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


def esMatrizCuadrada(matriz):
    numeroFilas = len(matriz)

    for fila in matriz:
        if len(fila) != numeroFilas:
            return False

    return True


def esAntisimetrica(matriz):

    if not esMatrizCuadrada(matriz):
        return False

    numeroFilas = len(matriz)

    for i in range(numeroFilas):
        for j in range(numeroFilas):
            if matriz[i][j] != -matriz[j][i]:
                return False

    return True


if __name__ == '__main__':

    assert esAntisimetrica([[0, 1, 2],
                            [-1, 0, 3],
                            [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True

    assert esAntisimetrica([[0, 1, 2],
                            [-1, 0, -2],
                            [2, 2, 3]]) is False

    assert esAntisimetrica([[1, 2, 5],
                            [0, 1, -9],
                            [0, 0, 1]]) is False

    assert esAntisimetrica([[1, 2, 5],
                            [-2, 1, -9],
                            [-5, 0, 1]]) is False

    matriz5 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz5) is False

    matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz6) is False

    matriz7 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz7) is False

    assert esMatrizCuadrada([[1, 0, 0, 0],
                             [0, 1, 1, 0],
                             [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0, 0, 0, 0, 0, 0]]) is False

    assert esMatrizCuadrada([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    print("All tests passed")