# -*- coding: utf-8 -*-
"""Untitled58.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EH36GCZGAiC-f-0AXajS2V8mVebKBfbc

Bài 02. Xem code đã có trong file btvn_02_pet.py (file trong link đính kèm).
    Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Hãy tạo ra class Pet để chứa các đối tượng của class Dog, class Pet này độc lập với class Dog (hay Pet ko kế thừa từ Dog)
        - Sau đó, tạo 4 đối tượng kiểu Dog và gán thành thuộc tính của 1 đối tượng kiểu Pet
            name        age
            Tom          6
            Jerry        9
            Butt         3
            Wine         1
        - Code đoạn chương trình để in ra được như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.
"""

class Dog:
  species = 'mammal'

  def __init__(self, name, age):
    self.name = name
    self.age = age
class Pet : 
  def __init__(self, petname, petage): 
    self.pet_name = petname
    self.pet_age = petage
  def description(self):
    return f'{self.pet_name} is {self.pet_age} years old'

    
dog1 = Pet('Tom', 6)
dog2 = Pet('Jerry', 9)
dog3 = Pet('Butt', 3)
dog4 = Pet('Wine', 1)
print(dog1.description(),'.' , dog2.description(), '.', dog3.description(),'.', dog4.description(), 'And theyre all mammals, of course.')