num=int(input("enter any numbers")) 
while num > 0: 
      rem=num % 10 
      sum=sum+rem 
      num=num // 10
      
print("sum of Digits is:-",sum)