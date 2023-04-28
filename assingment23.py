#23. Python program to count the space of a given string
string=input("Enter a string: ")
value=0
for i in string:
    if i.isspace():
      value+=1
print(value)
