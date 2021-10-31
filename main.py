


message = """Choose a tiny Python code to execute: 

0 - exit this program
1 - Variables - Scope of variables
2 - Formatting output
3 - Fibonacci = 1, 1, 2, 3, 5, 8... 

"""

import formatting
import fibonacci
import scopeVariables


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

  print("\n\n\n----#----\n\n") 


print('Bye bye')