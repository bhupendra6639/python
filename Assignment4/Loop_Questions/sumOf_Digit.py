num=int(input("enter any numbers"))
sumOfDigits=0
while num > 0:
      rem=num % 10
      sumOfDigits=sumOfDigits+rem
      num=num // 10
      
print("sum of Digits is:-",sumOfDigits)