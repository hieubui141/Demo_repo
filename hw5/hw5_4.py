# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-EpaB9_HvHtwJWGnx6Ju8WyrbhPc26uH

Bài 04. Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
"""

s= input('nhap mot chuoi bay ky: ')
for i in range(len(s)):
  if 65<=ord(s[i])<=90:
    print(s[i].lower(),end="")
  elif 97<=ord(s[i])<=142:
    print(s[i].upper(),end="")
  else : 
    print(s[i],end="")