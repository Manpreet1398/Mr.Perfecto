n=int(input())
for i in range(2,(n-1)):
    if n%i!=0 :
        flag=1
         print(" not prime")
else :
    flag=0

print(" prime")
