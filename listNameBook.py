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
  nameBook.append(newName)

def searchName():
  searchFor = input('Enter a name to search: ')
  negative = ''
  if (not searchFor in nameBook):
      negative = 'not '
  message = searchFor + ' was ' + negative + 'founded'
  print(message)

def deleteName():
  
  print('Choose a name to delete: ')
  for item in range(len(nameBook)):
    print(f'{item} - {nameBook[item]}')
  choosedName = int(input('Enter the number: '))
  
  nameTarget = nameBook[choosedName]
  del nameBook[choosedName]
  print(f'{nameTarget} was deleted')

def listNames():
  order = input('Choose a order: \n1 - Ascending\n2 - Descending\n\n')
  while True:
    if (order == '1' or order == '2'):
      break;
  nameBook.sort()
  if(order == '2'):
    nameBook.reverse()
  print('List of Names: ')
  print(nameBook)

def getOption():
  menu = """
    Choose a option:

    0 - Exit program
    1 - Enter a name
    2 - Search a name
    3 - Delete a name
    4 - List Names

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
