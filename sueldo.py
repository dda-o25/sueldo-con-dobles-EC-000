"""
El propósito de este código es dado un número de horas y de tarifa por hora, calcular el sueldo de x persona
asi como tambien las horas extras calculadas despues de la hora numero 48 son cobradas al doble
"""

# Entradas
horas_trabajadas = float(input())
tarifa_hora = float(input())

# Proceso
if horas_trabajadas > 48:
    horas_normales = 48
    horas_extra = horas_trabajadas - 48
    pago_extra = horas_extra * tarifa_hora * 2
    sueldo_total = (horas_normales * tarifa_hora) + pago_extra
else:
    horas_extra = 0
    pago_extra = 0
    sueldo_total = horas_trabajadas * tarifa_hora

# Salidas
print(int(horas_extra))
print(int(pago_extra))
print(int(sueldo_total))
