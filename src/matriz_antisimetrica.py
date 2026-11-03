# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


def esAntisimetrica(matriz):
    # Escribe aqui tu codigo
    if len(matriz[0]) != len(matriz):
        return False
    else:
        filas = 0
        while filas < len(matriz):
            columnas = 0
            while columnas < len(matriz[filas]):
                if matriz[filas][columnas] != - matriz[columnas][filas]:
                    return False
                columnas += 1
            filas += 1
    return True

# Casos Test:

if __name__ == '__main__':
    # Test Cases:

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, 3],
                             [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, -2],
                             [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                             [0, 1, -9],
                             [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                             [-2, 1, -9],
                             [-5, 0, 1]]) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:
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

    print("All tests passed")