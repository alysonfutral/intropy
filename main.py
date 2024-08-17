#function are packages of code that allow you to run that code, without having to copy-paste it, or type it all out manually.
# ***referred to as calling a function


def cube_volume(length, width, height):
  return length * width * height


volumeOfCube = cube_volume(5, 5, 5)
print(volumeOfCube)

print()  #space
import math  #import math


def hypotnuse(length, width):
  return math.sqrt(length**2 + width**2)  #return using exponent


hy = hypotnuse(3, 4)  #find the hypotnuse of a right triangle
print(hy)

print()  #space


def theBigCode():
  print("this prints the function")
  print("theBigCode")


theBigCode()  #prints the function theBigCode()
theBigCode()

print()

#find the area of the square


def areaOfSquare(length, width):
  return length * width


area = areaOfSquare(5, 5)
print(area)

print()


def area(length, width):
  return length * width


a = area(5, 4)
print("The area is")
print(a)
