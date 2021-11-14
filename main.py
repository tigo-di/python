


message = """Choose a tiny Python code to execute: 

0 - exit this program
1 - Variables - Scope of variables
2 - Formatting Strings
3 - Fibonacci = 1, 1, 2, 3, 5, 8... 
4 - Multiple Of a Number
5 - Triangle Area
6 - Number of Dividers of a Positive Integer
7 - List - append and len
8 - List - general
9 - List - Name book

"""

import formatting
import fibonacci
import scopeVariables
import multipleOfANumber
import triangleArea
import numberOfDividersOfAPositiveInteger
import listAppendLen
import listGeneral
import listNameBook



while True:
  print(message)
  code = int(input('Enter the option number: '))
  
  print("\n")

  if (code == 0):
    break;
  elif (code == 1):
    scopeVariables.main()
  elif (code == 2):
    formatting.main()
  elif (code == 3):
    fibonacci.main()
  elif (code == 4):
    multipleOfANumber.main()
  elif (code == 5):
    triangleArea.main()
  elif (code == 6):
    numberOfDividersOfAPositiveInteger.main()
  elif (code == 7):
    listAppendLen.main()
  elif (code == 8):
    listGeneral.main()
  elif (code == 9):
    listNameBook.main()


  print("\n\n\n----#----\n\n") 


print('Bye bye')