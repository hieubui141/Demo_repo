# -*- coding: utf-8 -*-
"""Untitled54.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YKGT2rSfgj2ytZlzEILf9HZ9MHlyZm60

Bài 00. Mô phỏng lại trò chơi sau: 
- Người chơi tung 2 con xúc xắc 6 mặt, các mặt có số chấm là: 1, 2, 3, 4, 5, 6
- Quan sát kết quả, tính tổng các mặt hướng lên sau khi 2 con xúc xắc đứng yên
- Lần đầu tiên,
    - Nếu tổng là 7 hoặc 11 => Người chơi THẮNG
    - Nếu tổng là 2, 3 hoặc 12 => Người chơi THUA
    - Nếu tổng là 4, 5, 6, 8, 9 hoặc 10 => Đây sẽ là ĐIỂM của người chơi, và sang vòng tiếp theo
- Để giành được THẮNG, người chơi tiếp tục tung 2 con xúc xắc cho đến khi ra được tổng = ĐIỂM trong lần đầu tiên; 
nếu tung ra được tổng = 7 => Người chơi THUA
Epsilon Bit
•
7 thg 10
"""

import random 
def dice_roll1():
  diceroll1 = random.randrange(1,7)
  return diceroll1
def dice_roll2():
  diceroll2 = random.randrange(1,7)
  return diceroll2
a = dice_roll1() + dice_roll2()
if a == 7 or a == 11:
 
  print('Thắng',dice_roll1(),dice_roll2(), 'tong a ', a)

elif a ==2 or a == 3 or a == 12 :
  
  print('thua',dice_roll1(),dice_roll2(), 'tong a', a)
else :
  b = dice_roll1() + dice_roll2()
  if b == a :
    print('chuc mung ban thang',b)
  elif b == 7 :
    print('thua roi',dice_roll1(),dice_roll2(),'tong b', b)
  else : 
    print('thua roi ban oi',dice_roll1(),dice_roll2(),'tong b', b)

import random 
def dice_roll1():
  diceroll1 = random.randrange(1,7)
  return diceroll1
def dice_roll2():
  diceroll2 = random.randrange(1,7)
  return diceroll2
a = dice_roll1() + dice_roll2()
if a == 7 or a == 11:
 
  print('Thắng', 'tong a ', a)

elif a ==2 or a == 3 or a == 12 :
  
  print('thua',dice_roll1(),dice_roll2(), 'tong a', a)
else :
  print(a)
  def dice_roll3():
    diceroll3 = random.randrange(1,7)
    return diceroll3

  def dice_roll4():
    diceroll4 = random.randrange(1,7)
    return diceroll4

  b = dice_roll3() + dice_roll4()
  if b == a :
    print(' chuc mung ban da thang',b)
  elif b == 7 :
    print('hen gap lai lan sau',b)
  else :
    print(' sr thu lai sau ', b)