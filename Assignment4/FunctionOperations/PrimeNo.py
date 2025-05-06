def NoIsPrimeORNot(number):
      flag=True
      for i in range(2,number):
            if number % i  == 0:
                  flag=False 
                  break    
            else:
                  continue
      if(flag):
            print(number," number is prime")
      else:
            print(number," number is  not prime")


number=int(input("enter Any Number For Check Prime Or Not"))
NoIsPrimeORNot(number)