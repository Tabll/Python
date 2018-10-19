import re

x = "$123￡"

x = x.replace('$', '')
x = x.replace('￡', '')

print(x)

s = "hello world! how are you? 0"
re.sub("[^A-Za-z]", "", s)

# Using regular expressions 使用正则表达式
print(s)
