#Start
a:int;b:int;c:int; isSum:bool

print("enter 3 numbers and isSum parameter:\n")
a:int=int(input("enter the first number:\n"))
b:int=int(input("enter the second number:\n"))
c:int=int(input("enter the third number:\n"))
isSumStr:str=input("enter 'y' if is Sum, or 'n':\n")
isSum:bool
if isSumStr== "y":
    isSum=True
else:
    isSum=False
if isSum:
    print(a+b+c)
else:
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    elif b>c:
        print(b)
    else:
        print(c)
#end