import random

r = random.randint(1, 100)
while True:
    num = input('1到100請猜一個數字？ ')
    num = int(num)
    if num == r:
        print('你答對了！')
        break
    elif num > r:
        print('答錯了，猜的數字太大了！')
    elif num < r:
        print('答錯了，猜的數字太小了！')    