# -*- coding: utf-8 -*-
"""Copy of Copy of Welcome to Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13CCO8N5i4mbwkRX95UzM56Giy5KpXRRN

bài tập 1
"""

age = int(input(" nhập tuổi của bạn : "))
income = float(input(" nhập thu nhập hàng năm của bạn : " ))
print(f'điều kiện để vay ngân hàng của bạn là :', age >=18 and income >= 2500)

"""bài tập 2 """

x= float(input('nhập giá trị của x ='))
y=float(input('nhập giá trị của y='))
z=float(input('nhập giá trị của z='))
import math
F = (x+y+z)/(x**2+y**2+1) - abs(x-z*math.cos(y))
print(f'giá trị của biểu thức F bằng : ',round(F,3))

"""bài tập 3"""

a = float(input('nhập giá trị của a = '))
b= float(input('nhập giá trị trị của b = '))
print(f'phần nguyên của phép chia là : ',a//b)
print(f'phần dư của phép chia là : ',a%b)