
def main():
  
  theList = [5]*8
  print(theList)

  theList = [1, 2, 3, 4]
  
  print(theList)

  print(2* theList)
  
  theList.insert(2, '2/5')
  theList.insert(10, '38')
  
  print(theList)
  
  print(len(theList))


  status = 2 in theList
  print(status)

  status = '8' in theList
  print(status)

  status = '8' in theList[5]
  print(status)

  mix = [42, 33, 2, 15]
  mix.sort()
  print(mix)
  
  mix = [42, 33, 2, 15]
  mix.reverse()
  print(mix)

  del mix[2]
  print(mix)
