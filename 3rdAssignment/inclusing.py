'''5.	Write a function that checks if a number is within a certain range 
(between 10 and 20, inclusive) using boolean expressions. The function
should return True if the number is within the range,
and False otherwise '''

# print(number<=10)
# print(number>20)

number=30
def number_in_range(number):
      if (number<=10 and number>=20):
            return True
      
      else:
            return False

withinRange=number_in_range(number)
print(withinRange)