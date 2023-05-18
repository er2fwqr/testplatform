import re

# 在字符串中查找匹配的模式
pattern = r"Hello (\w+)"
text = "Hello Python"
match = re.search(pattern, text)

# 打印匹配对象
print(match)  # <re.Match object; span=(0, 12), match='Hello Python'>

# 使用group方法获取匹配的子字符串
print(match.group())  # Hello Python

# 使用start和end方法获取子串的位置信息
print(match.start())  # 0
print(match.end())    # 12

# 使用span方法获取子串的起始和结束位置信息
print(match.span())   # (0, 12)
