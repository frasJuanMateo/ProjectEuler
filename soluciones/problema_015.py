import math

def solve():
    # Para una cuadrícula de n x n, el número de movimientos hacia la derecha es n
    # y el número de movimientos hacia abajo es n.
    # El total de movimientos es 2n, de los cuales debemos elegir n para ir a la derecha
    # (o n para ir hacia abajo).
    # Esto se calcula con el coeficiente binomial C(2n, n).
    n = 20
    return math.comb(2 * n, n)

if __name__ == "__main__":
    print(solve())
