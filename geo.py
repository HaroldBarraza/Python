import math

print("¿Cuál es el nombre de la Veta?")
NV = str(input())
print("'¿Cuáles son las coordenadas UTM de partida?")
print("Norte")
PPN = float(input())
print("Este")
PPE = float(input())
print("¿Cuáles son las coordenadas UTM donde se pretende cortar la veta?")
print("Norte")
PCN = float(input())
print("Este")
PCE = float(input())
print("Ingresa la cota inicial (solo números): ")
CI = float(input())
print("Ingresa la cota de llegada (final): ")
CF = float(input())

# Calculando las diferencias en coordenadas
if PPN > PCN:
    DN = PPN - PCN
else:
    DN = -(PPN - PCN)

if PPE > PCE:
    DE = PPE - PCE
else:
    DE = -(PPE - PCE)

# Determinando el cuadrante
if DN < 0 and DE < 0:
    cuadrante = "tercer cuadrante"
elif DN > 0 and DE > 0:
    cuadrante = "primer cuadrante"
elif DN > 0 and DE < 0:
    cuadrante = "segundo cuadrante"
elif DN < 0 and DE > 0:
    cuadrante = "cuarto cuadrante"

# Calculando el rumbo
x = math.sqrt((+ DN) * 2 + (+ DE) * 2)
coseno_de_beta = (+ DE) / x
resultado_beta = math.acos(coseno_de_beta)
beta = math.degrees(resultado_beta)

if cuadrante == "primer cuadrante":
    rumbo = f"N {90 - beta} E"
elif cuadrante == "segundo cuadrante":
    rumbo = f"N {90 - beta} W"
elif cuadrante == "tercer cuadrante":
    rumbo = f"S {90 - beta} W"
else: 
    rumbo = f"S {90 - beta} E"

# Calculando la distancia verdadera
distancia_verdadera = math.sqrt(x * 2 + (CI - CF) * 2)

# Calculando la inclinación
coseno_alfa = x / distancia_verdadera
inclinacion = math.degrees(math.acos(coseno_alfa))

# Resultados
print(f"El Rumbo del taladro es: {rumbo}")
print(f"La distancia verdadera de la Veta al Taladro es: {distancia_verdadera} m")
print(f"La inclinación del taladro es: {inclinacion}°")