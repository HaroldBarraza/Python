print(f"para el volumen de su llanta econtramos estos precios")
print(f"    Marca      Precio ")
print(f"1. Michelin -  $60.00  \n\
2. YoKohama -  $58.50 \n\
3. Vikran   -  $90.20 \n\
4. Toyo     -  $63.85 \n\
5. Salir\n")
while True:
 a = float(input("Que marca desea comprar? "))
 if a == 1:
        print("se realizo la compra de un neumatico marca Michelin por $60.00")
        print("gracias por su compra")
        break
 elif a == 2:
     print("se realizo la compra de un neumatico marca Vikran por $90.20")
     print("gracias por su compra")
     break
 elif a == 3:
     print("se realizo la compra de un neumatico marca Toyo por $63.50")
     print("gracias por su compra")
     break
 elif a == 4:
     print("se realizo la compra de un neumatico marca Toyo por $63.50")
     print("gracias por su compra")
     break
 else:
        print(f"esa no es una opcion valida")
