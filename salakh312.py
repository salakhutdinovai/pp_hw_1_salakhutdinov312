from  random import randint
x = randint(-100,100)
y = randint(-100,100)
print(x,y)
if x > 0 and y > 0:
    print(1)
if x < 0 and y > 0:
    print(2)
if x < 0 and y < 0:
    print(3)
if x > 0 and y < 0:
    print(4)
if x == 0 and y != 0:
    print('x')
if y == 0 and x != 0:
    print('y')


