import math
import os
from datetime import datetime
file = open("volumes.txt","a+")
date = datetime.now()
day = date.weekday()
d = float(input("enter the width of the tire in mm: "))
Z = float(input("enter the aspect ratio of the tire: "))
D = float(input("Enter the diameter of the wheel in inches: "))
A = (d * Z / 100 * 2 + (D * 25.4)) * 25.4 / 2 / 1000
C = math.pi * (A**2) * (d*(Z/100))
R = C / 1000
P = round(R,2)
print(f"The approximate volume of the wheel is {P} liters")

M_0 = "Michelin" 
Y_0 = "YoKohama"
V_0 = "Vikran" 
T_0 = "Toyo"
M = 50.00  
Y = 40.85
V = 60.20 
T = 69.85
M_1 = 60.00  
Y_1 = 58.50 
V_1 = 78.20 
T_1 = 78.85
M_2 = 70.00  
Y_2 = 60.50 
V_2 = 85.20 
T_2 = 86.85
M_3 = 90.00  
Y_3 = 80.50 
V_3 = 95.20 
T_3 = 99.85
if R>=0 and R <= 20:
    print(f"For your tire volume we find these prices")
    print(f"    Brand      Price ")
    print(f"1. Michelin -  ${M}  \n\
2. YoKohama -  ${Y} \n\
3. Vikran   -  ${V} \n\
4. Toyo     -  ${T} \n")
    while True:
        a = float(input("Que marca desea comprar? "))
        if a == 1:
         print(F"The purchase of a brand new tire was made {M_0} for ${M}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${M}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break

        elif a == 2:
         print(F"The purchase of a brand new tire was made {V_0} for ${Y}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${Y}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 3:
         print(F"The purchase of a brand new tire was made {V_0} for ${V}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${V}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 4:
         print(F"The purchase of a brand new tire was made {T_0} for ${T}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${T}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        else:
         print(f"That is not a valid option")
elif R>= 21 and R <=30:
      print(f"For your tire volume we find these prices")
      print(f"    Brand      Price ")
      print(f"1. Michelin -  ${M_1}  \n\
2. YoKohama -  ${Y_1} \n\
3. Vikran   -  ${V_1} \n\
4. Toyo     -  ${T_1} \n\
5. Salir\n")
      while True:
        a = float(input("Que marca desea comprar? "))
        if a == 1:
         print(f"The purchase of a brand new tire was made {M_0} for ${M_1}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${M_1}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 2:
         print(f"The purchase of a brand new tire was made {V_0} for ${Y_1}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${Y_1}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 3:
         print(f"The purchase of a brand new tire was made {V_0} for ${V_1}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${V_1}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()   
         break
        elif a == 4:
         print(f"The purchase of a brand new tire was made {T_0} for ${T_1}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${T_1}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        else:
         print(f"That is not a valid option")
elif R>= 31 and R <=40:
      print(f"For your tire volume we find these prices")
      print(f"    Brand      Price ")
      print(f"1. Michelin -  ${M_2}  \n\
2. YoKohama -  ${Y_2} \n\
3. Vikran   -  ${V_2} \n\
4. Toyo     -  ${T_2} \n\
5. Salir\n")
      while True:
        a = float(input("Que marca desea comprar? "))
        if a == 1:
         print(f"The purchase of a brand new tire was made {M_0} for ${M_2}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${M_2}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 2:
         print(f"The purchase of a brand new tire was made {V_0} for ${Y_2}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${Y_2}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 3:
         print(f"The purchase of a brand new tire was made {V_0} for ${V_2}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${V_2}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 4:
         print(f"The purchase of a brand new tire was made {T_0} for ${T_2}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${T_2}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         break
        else:
         print(f"That is not a valid option")
elif R >= 41:
      print(f"For your tire volume we find these prices")
      print(f"    Brand      Price ")
      print(f"1. Michelin -  ${M_3}  \n\
2. YoKohama -  ${Y_3} \n\
3. Vikran   -  ${V_3} \n\
4. Toyo     -  ${T_3} \n\
5. Salir\n")
      while True:
        a = float(input("Que marca desea comprar? "))
        if a == 1:
         print(f"The purchase of a brand new tire was made {M_0} for ${M_3}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${M_3}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 2:
         print(f"The purchase of a brand new tire was made {V_0} for ${Y_3}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${Y_3}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 3:
         print(f"The purchase of a brand new tire was made {V_0} for ${V_3}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${V_3}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        elif a == 4:
         print(f"The purchase of a brand new tire was made {T_0} for ${T_3}")
         tel = input("Enter your cell phone number please ")
         print("thank you for your purchase")
         file.write(f"{date:%Y-%m-%d}, {d}, {Z}, {D}, {P}\n")
         file.write(f"a tire was purchased for ${T_3}\n")
         file.write(f"the contact number is {tel}\n")
         print(file)
         file.close()
         file = open("volumes.txt", "r+")
         c = file.read()
         print(c)
         file.close()
         file = open("volumes.txt", "r+")
         c =file.read()
         print(c)
         file.close()
         break
        else:
         print(f"That is not a valid option")
