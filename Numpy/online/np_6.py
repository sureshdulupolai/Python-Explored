# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

a = np.pi
print(a)

b = np.sin(a / 2)
print(b) # 90 degrees

c = np.sin(a / 6) # 30 degreees
d = np.cos(a / 2)
np.tan(a / 2)
np.tan(0)


# Using Matplotlib with Numpy
x = np.arange(1, 11)
y = np.arange(10, 110, 10)

# plt.figure(figsize=(6, 6))
# plt.plot(x, y, 'r--')
# plt.show()


#
x_sin = np.arange(0, 2*a, 0.1)
y_sin = np.sin(x_sin)
print(y_sin)

# plt.figure(figsize=(6, 6))
# plt.plot(x_sin, y_sin)
# plt.title('Sin Curve')
# plt.show()


#
x_cos = np.arange(0, 2*a, 0.1)
y_cos = np.cos(x_cos)

# plt.figure(figsize=(6, 6))
# plt.plot(x_cos, y_cos)
# plt.title('Cos Curve')
# plt.show()


#
x_tan = np.arange(0, 2*a, 0.1)
y_tan = np.tan(x_tan)
# plt.figure(figsize=(6, 6))
# plt.plot(x_tan, y_tan)
# plt.title('Tan Curve')
# plt.show()


# 
plt.figure(figsize=(6, 6))
plt.subplot(2, 2, 1)
plt.plot(x_sin, y_sin, 'r-')
plt.title('Sin Curve')

plt.subplot(2, 2, 2)
plt.plot(x_cos, y_cos, 'b-')
plt.title('Cos Curve')

plt.subplot(2, 2, 3)
plt.plot(x_tan, y_tan, 'g-')
plt.title('Tan Curve')

plt.show()