# overloading
def sum(datatype, *args):
    if datatype == 'int':
        ans = 0
    elif datatype == 'str':
        ans = ''
    for x in args:
        ans = ans + x
    return ans


print(sum('int', 2, 3, 4))
print(sum('int', 2, 3))
print(sum('str', 'hello ', 'this'))

#call method with int and str and const with *args
