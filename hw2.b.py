# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdC3SxdfjwBLniTyHbktCrGtuNeFkzXo

S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
"""

x= int(input('nhap gia tri cua x'))
n= int(input('nhap gia tri cua n'))
s_2=0
for i in range(n+1):
  s_2=s_2+((-1)**i)*x**i
print('gia tri cua s_2 la :',s_2)