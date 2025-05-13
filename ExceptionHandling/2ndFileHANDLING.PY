def FileOperation():
      try:
            with open("data.txt","r") as file:
                  data=file.read()
                  print(data)
                  
            # with open("bhupendra.txt","w") as file:
            #       data=str(input("enter any text"))
            #       print("FILE CONTENT \n",data)
            #       writenconten=file.write(data)
            #       print(writenconten)
      except FileNotFoundError as e:
            print("file Not Found",e)   

      except IOError as e:
            print("INPUT OUTPUT ERROR",e)
            
     
FileOperation()