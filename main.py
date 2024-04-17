'''
This is a simple program that will print out a message of your choice to the screen.

Simple Constructor Code 
'''


class calc:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    print("I have called the init constructor")

  def add(self, x, y):
    return x + y


numbers = calc(5, 6)
print(numbers.add(5, 6))
