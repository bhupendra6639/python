def StringPallindrome(origionalString):
      string=origionalString
      reverString = ""
      i=len(string)-1
      while i >= 0:
            reverString = reverString + string[i]
            i=i-1
      print(string,reverString)
      if string == origionalString:
        print("String is a Palindrome:", string)
      else:
        print("String is not a Palindrome:", string)


string=input("enter any String")
StringPallindrome(string)