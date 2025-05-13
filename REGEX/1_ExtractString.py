'''1.	Extract all words starting with 'a' from a sentence.
	Task: Write a regex pattern to find all words that start with the letter 'a', regardless of case, in a given sentence.
	Input: 
	Expected Output: ['Apple', 'and', 'avocado', 'are', 'amazing']
'''


import re

sentence = "Apple and avocado are amazing fruits."
matches = re.findall(r'[\baA]\w*', sentence)

print(matches)