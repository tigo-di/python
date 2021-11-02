
def inputNumber(message):
  number = int(input(message))
  return number


def mod(multipleNumber, referenceNumber):
  response = False
  if (multipleNumber % referenceNumber == 0):
    response = True
  return response

def main():
  #  Entrada de dois números
  multipleNumber = inputNumber('Digite o número que se deseja sabe se é múltiplo de outro: \n')
  referenceNumber = inputNumber('Digite o número do qual se deseja verificar se o primeiro número é múltiplo: \n')

  #  O primeiro número é múltiplo do segundo se módulo do primeiro número pelo segundo for igual a zero
  isMultiple = mod(multipleNumber, referenceNumber)

  print(f'\n{isMultiple}')

