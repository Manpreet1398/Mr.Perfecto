import pyperclip
import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
EmailRegex = re.compile(r'[A-za-z0-9_.+]+@[A-za-z0-9_.]+[^(.$)]')
s=pyperclip.paste()
print(s)
print(phoneNumberRegex.findall(s))
print(EmailRegex.findall(s))
