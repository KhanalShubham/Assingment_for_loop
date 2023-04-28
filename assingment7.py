#7. reverse a list
a=eval(input("Enter the number in list: "))
reversed=[]
for i in a:
    reversed =[i]+reversed
print(reversed)
