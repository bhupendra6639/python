'''
4.	Extract all numbers from a string.
	Task: Extract all numeric values (both single and multi-digit) from a string using regex.
	Input: "I have 2 apples and 3 oranges."
	Expected Output: ['2', '3']'''

import re
def ExtracString_Into_Digit(text):
      Number=re.findall(r'\d+', text) 
      print(Number)

ExtracString_Into_Digit("I have 2 apples and 3 oranges.")