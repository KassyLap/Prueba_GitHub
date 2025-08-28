import numpy as np

def sumaFormula(p1, p2):
    max_len = max(len(p1), len(p2))
    p1 = [0] * (max_len - len(p1)) + p1
    p2 = [0] * (max_len - len(p2)) + p2
    return [a + b for a, b in zip(p1, p2)]

def sumaNumpy(p1, p2):
    poly1 = np.poly1d(p1)
    poly2 = np.poly1d(p2)
    return poly1 + poly2

p1 = [2, 4, 6]
p2 = [1, 0, 4]

print("Suma manual:", sumaFormula(p1, p2))

print("Suma con numpy:", sumaNumpy(p1, p2))

print("Hola Mundo")
