# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oEAmLXVK2ORj6V8PFBe0xkvl-Uk05M6-

Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]. Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
"""

my_list =  ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
a = []
for i in my_list:
   a = (i.split('.',3))[-1]
   print('hậu tố bao gồm : ', a)