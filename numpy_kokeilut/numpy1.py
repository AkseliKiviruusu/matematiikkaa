import numpy as np

#T1

a = 2.493
b = 0.911

print(f'a = {np.degrees(a):.2f} astetta')
print(f'b = {np.degrees(b):.2f} astetta')

c = 137.7
d = 62.3

print(f'\nc = {np.radians(c):.2f} radiaania')
print(f'd = {np.radians(d):.2f} radiaania')

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print()
for i in A:
    print(f'{i} astetta on {np.radians(i):.2f} radiaania')

#T2

kat1 = 1.6
kat2 = 2.3

print(f'\nhypotenuusan pituus: {np.hypot(kat1, kat2):.2f}m')