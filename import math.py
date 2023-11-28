import math
import os
from datetime import datetime
file = open("volumes.txt","a+")
date = datetime.now()
day = date.weekday()
d = float(input("introdusca el ancho del neumatico en mm: "))
a = float(input("introduzca la relacion de aspecto del neumatico: "))
D = float(input("istrduzca el diametro de la rueda en pulgadas: "))
A = (d * a / 100 * 2 + (D * 25.4)) * 25.4 / 2 / 1000
C = math.pi * (A**2) * (d*(a/100))
R = C / 1000
T = round(R,2)
print(f"El volumen aproximado de la rueda es {T} litros")
file.write(f"el ancho del denumatico es {d} la relacion del neumatico es {a} el diametro del neumatico es {D} el volimen es {T} {date:%Y-%m-%d}\n")
print(file)
file.close()
file = open("volumes.txt", "r+")
c =file.read()
print(c)
file.close()
