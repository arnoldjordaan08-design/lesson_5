#Question 1
def greet():
  print("Hello, World!")

greet()

#Question 2
def personalized_greet(name):
  print(f"Hello, {name}!")

personalized_greet("Connor")

#Question 3
def square(num):
  return num ** 2

result = square(5)
print(result)

#Question 4
def rectangle_area(length, width):
  return length * width

area = rectangle_area(4, 5)
print(area)
 #Question 5
def apply_operation(func, num1):
  return func(num1) 

def double(num2):
  return num2 * 2

print(apply_operation(double, 7))
print(apply_operation(square, 3))
