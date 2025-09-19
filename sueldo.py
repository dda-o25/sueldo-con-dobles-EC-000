"""
El propósito de este código es dado un número de horas y de tarifa por hora, calcular el sueldo de x persona
asi como tambien las horas extras calculadas despues de la hora numero 48 son cobradas al doble
"""


# Entradas
horas_trabajadas = int(input())
tarifa_hora = int(input())

# Proceso
if horas_trabajadas > 48:
    horas_normales = 48
    horas_extra = horas_trabajadas - 48
    sueldo = (horas_normales * tarifa_hora) + (horas_extra * tarifa_hora * 2)
else:
    sueldo = horas_trabajadas * tarifa_hora

# Salidas
print(sueldo)
