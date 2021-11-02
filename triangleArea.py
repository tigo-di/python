# triangle area = (base * height)/2

def inputNumber(message):
  number = int(input(message))
  return number

def getTriangleArea(base, height):
  return (base * height)/2

def main():
  base = inputNumber('Enter base value: ')
  
  height = inputNumber('Enter height value: ')
  
  triangleArea = int(getTriangleArea(base, height))
  
  message = f'The triangle area is {triangleArea}'

  print(message)