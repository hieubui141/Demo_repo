# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wNLeAxQsTPDJjZgTD8hpFDsexPoY8BGS

Bài 03. Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử. Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
"""

my_dict = {1 : [1, 2, 3, 4, 5, 6], 2: [-1, -2, -3, -4, -5, -6], 3: [3, 5, 7, 9, 11, 13], 4 : [10, 20, 30, 40, 50, 60]}
key_list = my_dict.keys()
for i in key_list : 
  print('phần tử thứ 5 của value thứ' ,i, ' là : ', my_dict[i][4])