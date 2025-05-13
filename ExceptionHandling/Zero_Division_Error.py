try:
      num1=int(input("enter First number:-"))
      num2=int(input("enter Second number:-"))
      result=num1//num2
      print(result)
except ZeroDivisionError:
      print("Zero Division Error plese enter vallid number")