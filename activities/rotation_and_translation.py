"""
Activitat 1 – Moviments al pla

Implementa les funcions de transformació geomètrica.

Conceptes matemàtics:
- translació
- gir
"""

import math

def translacio(x, y, dx, dy):
    """
    Translació d'un punt del pla.

    Matemàticament:
        (x, y) -> (x + dx, y + dy)

    Retorna les noves coordenades.
    """

    # TODO alumnes
    new_x = x + dx
    new_y = y + dy

    return new_x, new_y


def gir(x, y, angle):
    """
    Gir d'un punt respecte l'origen.

    angle en graus.

    Fórmula matemàtica:

        x' = x cosθ − y sinθ
        y' = x sinθ + y cosθ
    """


    rad = math.radians(angle)

    # TODO alumnes
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)

    return new_x, new_y
