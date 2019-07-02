import pyperclip

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
s=pyperclip.paste()
print(s)
print(phoneNumberRegex.findall(s))