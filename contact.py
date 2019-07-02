import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'call me at 222-202-5555 or 414-666-5555'
mo = phoneNumberRegex.search(message)
print(mo.group())
print(phoneNumberRegex.findall(message))
phoneNumberRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group(1))
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)
print(mo.group(2))
message = "Call me at (222)-202-5555 or (414)-666-5555"
phoneNumberRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)
print(mo.group(2))
print(mo.group(1))
pipeExample = re.compile(r'(wo|man|mobile)')
sample = "This is movie of batman"
print(pipeExample.search(sample).group())
# ? when string appears 0 or one times
useOfQuestionMark = re.compile(r'Bat(wo)?man')
sample = "this is movie of Batman Batwoman"
print(useOfQuestionMark.search(sample).group())
sam = "manpreet1234@@@"
print(re.findall("[a-zA-Z]+", sam))

'''use of 0 or * ---0or more'''
sam = "this is  Batman movie"
useOfStarSign = re.compile(r'Bat(wo)*man')
print(useOfStarSign.search(sam).group())
'''use of 0 or + atleast 1'''
# sam="this is  Batman movie"
# useOfStarSign=re.compile(r'Bat(wo)+man')
# print(useOfStarSign.search(sam).group())
startsWith = re.compile(r'^The')
sam = "The Hindu Newspaper"
print(startsWith.search(sam).group())
endsWith = re.compile(r'paper$')
sam = "The Hindu Newspaper"
print(endsWith.search(sam).group())
samInteger = "this is sample string with some numbers 123456"
IntegerRegex = re.compile(r'(\d+)*')
print(IntegerRegex.search(samInteger).group())
print(IntegerRegex.findall(samInteger))
'''use of \s for white space'''
spaceRefex = re.compile(r'(\s+)*')
print(spaceRefex.search(" without spACE").group())
print(spaceRefex.findall(" without spACE"))
'''use of \S for white space'''
spaceRefex = re.compile(r'(\S+)*')
print(spaceRefex.search(" without spACE").group())
print(spaceRefex.findall(" without spACE"))
'''\W neither no. nor alphabets only special characters'''
StringWordNumder = "this is to check @!$@!$$ word and 123dhsaidj15645"

StringWordNumderRegex = re.compile(r'(\s\W+)+')
print(StringWordNumderRegex.search(StringWordNumder).group())
'''Start() to find out number of spaces'''
x = re.search("\s", "The rai in Spain")
print(x.start())
''' split() method will split the string as per given regex'''
s = re.split("\W", "The$rain&*inSpain")
print(s)
'''use of span function that gives start and end index'''
sm = "the rain 123 in spain Singapore"

reForSpan = re.search(r'(\bS\w+)', sm)
print(reForSpan.span())
print(reForSpan.group())
print(reForSpan.string)
'''use of +?* with escape characters'''
escapeCharacter = "we lear use of +?*"
escapeCharacterRegex = re.compile(r'(\+\?\*)')
print(escapeCharacterRegex.search(escapeCharacter).group())
slicingRegex = re.compile(r'(HA){3}')
print(slicingRegex.search("HAHAHAHAHAHAHAHAHA").group())
slicingRegex = re.compile(r'(HA){3,5}')
print(slicingRegex.search("HAHAHAHAHAHAHAHAHA").group())
'''non-greedy way'''
slicingRegex = re.compile(r'(HA){3,7}?')
print(slicingRegex.search("HAHAHAHAHAHAHAHAHA").group())

''' Search vowels from String'''
vowelsRegex = re.compile(r'[aeiouAEIOU]+')

print(vowelsRegex.findall("This is to find vowel As"))

''' Search consonants from String'''
vowelsRegex = re.compile(r'[^aeiouAEIOU]+')

print(vowelsRegex.findall("This is to find vowel"))

''' Search only alphabets in string'''

alphaRegex = re.compile(r'([A-Za-z]+)+')

print(alphaRegex.findall("Python123164Projects"))

''' Search only alphanum in string'''

alphaRegex = re.compile(r'([A-Za-z0-9]+)+')

print(alphaRegex.findall("Python 123164 Pro&&&&jects"))

''' Search only num in string'''

alphaRegex = re.compile(r'([0-9]+)+')

print(alphaRegex.findall("Python 123164 Pro&&&&jects 121654"))

''' Search only special character in string'''

alphaRegex = re.compile(r'([^a-zA-Z0-9]+)+')

print(alphaRegex.findall("Python 123164 Pro&&&&jects 121654"))

onlyDigitsRegex = re.compile(r'(^\d+$)+')

stringWithNum = "123194"

print(onlyDigitsRegex.findall(stringWithNum))

''' . to remove first char'''
removeFirstCharRegex = re.compile(r'(.*)+')
print(removeFirstCharRegex.search("dfjsad1 32156").group())

'''DOTALL operator'''

DotRegex = re.compile(r'.at')

strdot = "This is cat fat flat rat"
print(DotRegex.findall(strdot))

DotRegexWith2 = re.compile(r'.{,2}at')
strdot = "This is cat fat flat rat"
print(DotRegexWith2.findall(strdot))

IntCharRegex = re.compile(r'(\d\s\w+)')
lyrics = '''On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree




On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''
print("CharRegex", IntCharRegex.findall(lyrics))

'''greedy '''
regexAnything = re.compile(r'<(.*)>')
print(regexAnything.search("<This is dinner> for you>").group())

'''non-greedy'''
regexAnything = re.compile(r'<(.*?)>')
print(regexAnything.search("<This is dinner> for you>").group())

script = "Serve public trust.\nProtect the innocent.\nUphold the law."
scriptRegex = re.compile(r'.*')
print(scriptRegex.search(script).group())
print(scriptRegex.findall(script))

'''.DOTALL operator'''
scriptRegex = re.compile(r'.*', re.DOTALL)
print(scriptRegex.search(script).group())
###############################################
'''IgnoreALL keyword'''
VowelRegEx = re.compile(r'[aeiou]', re.I)
print(VowelRegEx.findall("This is to Test Vowel with Capital AIE"))

''' sub() to find and replace string as per regex '''
script = "Agent Alice give secret documents to Agent Bob"
agentRegex = re.compile(r'Agent \w+')
print(agentRegex.findall(script))

print(agentRegex.sub("READACTED", script))

agentRegex = re.compile(r'Agent (\w)(\w)\w*')
print(agentRegex.findall(script))
print(agentRegex.sub(r'Agent \1***', script))

''' Email regex'''

EmailRegex = re.compile(r'[A-za-z0-9_.+]+@[A-za-z0-9_.]+[^(.$)]')
emailScript = "This is my email ankitkrmittal@gmail.com and ankit.mital@lendkey.net."
print(EmailRegex.findall(emailScript))

'''Phone num Regex'''

phoneNumRegex = re.compile(r'(((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?)')
PhoneRegexScript = "This is my phone number (415)-555-9678 and 415 999-6578 and 515-9999"
print(phoneNumRegex.findall(PhoneRegexScript))

'''Q) copy contact details frm website and print list of emails phone no. and name using pyperclip and regex'''
