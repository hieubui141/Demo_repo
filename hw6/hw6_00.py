# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ACkaLXmYGO5JIVy7dCPm62of1IPQlIxx

Bài 00. Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
"""

origin_list = [2, 4, 7 ,'python', 'coding', 2021, 12, 3.14, 'Xyz']
import random
new_list= random.sample(origin_list,5)
print(new_list)