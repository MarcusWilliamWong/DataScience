'''
Author       : Eureke
Date         : 2022-11-18 01:32:47
LastEditors  : Marcus Wong
LastEditTime : 2022-11-27 05:20:30
Description  : 
'''
import numpy as np
# 1
x = 2*5000*np.tan(2*np.pi*0.2/2)
# print(x)
# 3
b = np.array(-0.2052-0.5638j, dtype=complex)
# print(np.abs(b))
c = np.array(0.6-1.0392j, dtype=complex)
# print(np.abs(c))
# 4

# 5
for i in range(100):
  y = np.random.choice(3, p=[0.4, 0.5, 0.1])
  print(y)

np.random.uniform()