# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oEAmLXVK2ORj6V8PFBe0xkvl-Uk05M6-

Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
"""

my_string = input(' nhập một câu từ bàn phím ')
a = my_string.split()
x = ""
for i in a : 
    if len(i)> len(x) :
      x = i
print(x)