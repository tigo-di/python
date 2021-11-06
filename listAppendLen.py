# ENTRADA DE DADOS EM UMA LISTA
# (APPEND) E TAMANHO DA LISTA (LEN)
# Faremos um programa que solicita ao
# usuário a quantidade de elementos da
# lista, insere essa quantidade de elementos
# na lista e mostra os elementos
# armazenados nela.


def setNumberOfitems():
  number = int(input('Enter the number of items list: '))
  return number

def enterItems(numberOfItems):
  tempList = []
  counter = 0
  while counter<numberOfItems:
    item = input(f'Enter item #{counter+1}: ')
    tempList.append(item)
    counter = counter + 1
  return tempList

def printList(theList):
  print('\n')
  lengthList = len(theList)
  print(f'len: {lengthList}')
  print('\n')
  for i in range(lengthList):
    print(theList[i])

def main():
  numberOfItems = setNumberOfitems()
  aList = enterItems(numberOfItems)
  printList(aList)