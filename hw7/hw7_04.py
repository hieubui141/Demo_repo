# -*- coding: utf-8 -*-
"""Untitled40.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wcjNh4OHiWZbgRbp-wUyAU1D5SAErg7a

Bài 04: Cho 1 list chứa các tuple không rỗng. Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
"""

my_list = [(1, 3, 5, 7), (-1 , -2, -3), (4, 3, 2, 1), (10, 20, 30, 40)]
print(sorted( my_list, key = lambda x : x[-1]))