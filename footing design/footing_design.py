import math
import os
clear=lambda: os.system('cls')
clear()
b = int(input('Shorter side of the column in mm: '))
D = int(input('Longer side of the column in mm: '))
fck = int(input('Grade of concrete used in N/mm²: '))
fy = int(input('Grade of steel used in N/mm²:'))
SBC = int(input('SBC of soil in kN/mm²:'))
p = int(input('Load on column in kN:'))
wf = 1.1*p
wu = 1.5*wf
# Area of footing
Af = wf/SBC

# Size of footing
L = math.sqrt(Af/(b/D))
B = (b/D)*L
L = int(L)
L = L+1
B = int(B)
B = B+1
# AF PROVOIDED
Af = L*B
# upward soil pressure
P = 1.5*p/Af
# depth of footing for bending moment
D = D/1000
b = b/1000
# Bending moment in x direction
Mx = (P*B*(L-D)*(L-D))/8
# Bending moment in y direction
My = (P*L*(B-b)*(B-b))/8
# Maximum bending moment
if Mx >= My:
    Mmax = Mx
if Mx <My:
    Mmax = My
#  calculation of depth d
d = math.sqrt((Mmax*10**6)/(138*fck))
# for safety purpose, we are adding 15mm in d
d = d+15
# Assuming cover for footing is 50 mm and 20 mm bars are provoided
Doverall = d+60



clear=lambda: os.system('cls')
clear()
print('sorter lenth of footing in m:', B)
print('longer lenth of footing in m:', L)
print('area of footing provoided in m²:', Af)
print('Upward soil Pressure in kN/m²:', P)
print('Maximum bending moment in kN.m:', Mmax )
print('Effective depth provoided in mm:', d)
print('Overall depth provoded in mm:', Doverall)