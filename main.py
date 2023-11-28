def main():
    a = float(input(f"ingrese la primera medida del odometro: "))
    b = float(input(f"ingrese la segunda medida del odometro: "))
    c = float(input(f"ingrese la cantidad de combustible utilizado: "))
    mpg =  miles_per_galon( a, b , c)# resultado de (b-a)/c
    ipk100 = ipk_mpg(mpg)# resultado de 235.215 / mpg
    print(f"{mpg: .2f} millas por galon")
    print(f"{ipk100: .2f} litros por 100 kilmetros")

def miles_per_galon(a, b, c):
    mpg = abs(b - a) / c
    return mpg
def ipk_mpg(mpg):
    ipk100 = 235.215 / mpg
    return ipk100   
main()  