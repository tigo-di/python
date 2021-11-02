# enter positive integer 

def inputNumber():
  
  while True: 
    number = int(input('Enter positive integer: '))
    if (number > 0):
      break

  return number


def getDividers(number):
  numberOfDividers = 0  
  for n in range(1, number + 1):
    if(number % n == 0):
      numberOfDividers = numberOfDividers + 1
  return numberOfDividers 


def main():
  number = inputNumber()
  dividers = getDividers(number)
  message = f'The number of dividers of {number} is {dividers}'
  print(message)
  