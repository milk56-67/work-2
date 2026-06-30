import math

r = float(input("ป้อนรัศมี: "))
h = float(input("ป้อนความสูง: "))

area = 2 * math.pi * r * (r + h)

print("พื้นที่ผิวทรงกระบอก =", area)