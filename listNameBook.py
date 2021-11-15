# Name Book exercise: 
# enter name 
# search name 
# delete name 
# list names in ascending order 
# list name in descendirg order 

nameBook = []

def enterName():
  while True:
    newName = input('Enter a name: ')
    if(len(newName)>0):
      break
  
  message = 'Choose position to save the new name: \n1 - at top of list\n2 - at end of list: \n\nEnter number position: '
  
  position = input(message)

  if(position == '1'):
    nameBook.insert(0,newName)  
  else:
    nameBook.append(newName)

def searchName():
  searchFor = input('Enter a name to search: ')
  negative = ''
  if (not searchFor in nameBook):
      negative = 'not '
  message = searchFor + ' was ' + negative + 'founded'
  print(message)

def replaceName():
  listNames(True)
  choosedName = int(input('Enter the number to replace: '))
  substitute = input('Enter the replecement name: ')
  nameBook[choosedName] = substitute

def deleteName():
  print('Choose a name to delete: ')
  listNames(True)
  choosedName = int(input('Enter the number to delete: '))
 
  nameTarget = nameBook[choosedName]
  del nameBook[choosedName]
  print(f'{nameTarget} was deleted')

def listNames(withouOrder=False):
  if(withouOrder==True):
    order = '0'
  else:
    order = input('Choose a order: \n0 - not reorder\n1 - Ascending\n2 - Descending\n\n')
  while True:
    if(order == '0' or order == '1' or order == '2'):
      break;
  if(order!='0'):
    nameBook.sort()
    if(order == '2'):
      nameBook.reverse()
  print('List of Names: ')
  for item in range(len(nameBook)):
    print(f'{item} - {nameBook[item]}')

def counterNames():
  counter = len(nameBook)
  message = f'Number of names is {counter}'
  print(message)

def getOption():
  menu = """
    Choose a option:

    0 - Exit program
    1 - Enter a name
    2 - Search a name
    3 - Delete a name
    4 - List names
    5 - Counter names
    6 - Replace a name

  """
  while True:
    print(menu)
    option = input('Enter a option: ')
    if(option.isdigit() and int(option) >= 0):
      break
  return int(option)

def main():  
  while True:
    option = getOption()
    if(option == 0):
      print('Exit program')
      break;
    elif(option == 1): # Enter a name
      enterName()
    elif(option == 2): # Search a name
      searchName()
    elif(option == 3): # Delete a name
      deleteName()
    elif(option == 4): # List names
      listNames()
    elif(option == 5): # Counter names
      counterNames()
    elif(option == 6): # Replace a name
      replaceName()
