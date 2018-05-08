from jank import *

import time

v, t = T.vt(lambda x: x**4, 1024)
print(v)
print(t)

T(time.sleep, 0.314)

T('x=0\nfor i in range(1000): x += i*i')

print(T.cpu('x=0\nfor i in range(1000): x += i*i'))

f1 = lambda x: x+1
f2 = lambda x: x*2

print((F(f1, f2)/64)@[3,4]) # 7
print(F(f2, f1)(3)) # 8

