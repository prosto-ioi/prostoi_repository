import re
word = str(input())
def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)

camel = snake_to_camel(word)
print("Camel case:", camel)

word = str(input())

def addspace(s):
    return re.sub(r"([A-Z])", r" \1", s)
x = addspace(word)
print(x)

import re
word = str(input())
def snake_to_camel(s):
    return re.sub(r"([A-Z])", r'_\1', s).lower()

camel = snake_to_camel(word)
print("Camel case:", camel)
