'''3.	Write a function that takes a string and a character,
and returns the number of times the character appears in the string. 
For example, in the string "banana", the letter "a" appears 3 times.
'''
string="Banana"
# print(string.count("a"))
# print(string.count("b"))
# print(string.count("n"))
# def findcount(character,text):
#       countWorld=string.count(character)
#       return countWorld

findworld={}

for world in string:
     if world not in findworld:
           findworld[world]=1
     else:
           findworld[world]= findworld[world]+1          

print(findworld)