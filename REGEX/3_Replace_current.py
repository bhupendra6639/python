import re

def replace_sub_String(text):
      result = re.sub(r'\bcat\b', 'dog', text)
      print(result)

text = "The cat is cute. The cat is playing."
replace_sub_String(text)