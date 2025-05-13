def FileOperation():
      try:
            with open("data,txt","r") as file:
                  data=file.read()
                  print("FILE CONTENT \n",data)
                  
      except FileExistsError as e:
            print(e)   

      except PermissionError as e:
            print(e)
FileOperation()