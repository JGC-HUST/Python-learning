# io_input.py
# coding=UTF-8
# 判断回文字符串，其中将字符串中的标点（非英文字母）全剔除掉
def reverse(text):
      '''返回逆序'''
      return text[::-1]

def is_palindrome(text):
      '''判断是否是回文'''
      return reverse(text) == text

something = input('Enter text:')

#处理字符串
list1 = []
for i in something:
      if i.isalpha():
            list1.append(i)
str1 = ''.join(list1)

if is_palindrome(str1):
      print('Yes')
else:
      print('No')
