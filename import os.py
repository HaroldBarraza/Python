import math
A = (205 * 60 / 100 * 2 + (15 * 25.4)) * 25.4 / 2 / 1000
C = math.pi * (A ** 2) * (205 * (60/100))
R = C / 1000
B = round(R,2)
print(B)
radio = (205 * 60 / 100 * 2 + 381) * 25.4 / 2 / 1000
print(radio)