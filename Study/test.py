x = "$123"

x = x.replace('$', '')

print(x)


import re
s = "hello world! how are you? 0"
re.sub("[^A-Za-z]", "", s)

# Using regular expressions 正则表达式
print(s)
