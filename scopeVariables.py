def main():
  name = "Amelie"

  def showMessage():
    print(name)

  def showMessageWithDefaultValue(name="Chihiro"):
    print(name)

  def showMessage2():
    print(name)


  showMessage()  

  name = "Mia Wallace"

  showMessage()

  showMessageWithDefaultValue("Ripley")

  showMessageWithDefaultValue()