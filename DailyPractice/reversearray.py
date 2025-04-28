listNumber=[20,1,56,89,68,97]
newList=[]
for i in range(0,len(listNumber)-1):
      smallRange=listNumber[i]
      for j in range(i+1, len(listNumber) - 1):
            if(listNumber[i] <= listNumber[j+1]):
                  temp=listNumber[i]
                  listNumber[i]=listNumber[j+1]
                  listNumber[j+1]=temp
            
print(listNumber)
newlist=listNumber.sort()
print(listNumber)