def EvenNo(list):
      evenNo=[]
      for i in list:
            if i % 2 == 0:
                  evenNo.append(i)
            else:
                  continue
      print(" EvenNo In List Are:-",evenNo)
list=[1,24,56,7,9,3,5,21,8,6,4]
EvenNo(list)