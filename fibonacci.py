def main():
  limit = 8

  numberA = 1
  numberB = 1

  numbers = []
  numbers.append(numberA)
  numbers.append(numberB)


  for counter in range(2, limit + 1):
    currentNumber = numberA + numberB
    numbers.append(currentNumber)
    numberA = numberB
    numberB = currentNumber
    counter = counter + 1

  message = '';

  first = True

  for n in numbers:
    if (first == False):
      message += ", "
    message += f"{n}"
    first = False

  message += "..."

  print(message)