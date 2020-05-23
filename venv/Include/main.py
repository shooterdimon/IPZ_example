from cmath import*

F1 = lambda p: 195825*p + 17642.205 * (p ** 2) + 2750000000
F2 = lambda p: 8.4 * p ** 2 + 2225 * p + 291666
F2d = lambda p: 13213*(p**2) + 420000 * p + 30600000

p1, p2 = complex(238, 112.687), complex(238, -112.687)

print(f'F1(p): {F1(p1):.3f} and {F1(p2):.3f}')
print(f'F2d(p): {F2d(p1):.3f} and {F2d(p2):.3f}')


F1p1 = polar(F1(p1))
F2dp1 = polar(F2d(p1))
F1p2 = polar(F1(p2))
F2dp2 = polar(F2d(p2))

print(f'F1(p1) = {F1p1[0]:.3f}e^({F1p1[1] * 180 / pi:.3f}) and F2d(p1) = {F2dp1[0]:.3f}e^({F2dp1[1] * 180 / pi:.3f})')
print(f'F1(p2) = {F1p2[0]:.3f}e^({F1p2[1] * 180 / pi:.3f}) and F2d(p2) = {F2dp2[0]:.3f}e^({F2dp2[1] * 180 / pi:.3f})')



print(polar(F1(p1)/F2d(p1)))
print(polar(F1(p2)/F2d(p2)))