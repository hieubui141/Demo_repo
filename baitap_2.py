# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OMgX7gOhLKWGPbexImV28_mCSbxVfTRI

Bài tập 2
"""

x= float(input('nhập giá trị của x ='))
y=float(input('nhập giá trị của y='))
z=float(input('nhập giá trị của z='))
import math
F = (x+y+z)/(x**2+y**2+1) - abs(x-z*math.cos(y))
print(f'giá trị của biểu thức F bằng : ',round(F,3))