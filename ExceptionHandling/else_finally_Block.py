try:
      num1=int(input("enter First number:-"))
      num2=int(input("enter Second number:-"))
      result=num1//num2
except ZeroDivisionError:#
      print("Zero Division Error plese enter vallid number")

except ValueError:
      print("value Error occurs Enter correct Type Value")

else:# try doen occure error  whe occure else block
      print("The result of division is::",result)

finally:
      print("ITS OPESIONAL BLOCK ITS ALWAYS EXECUTE")