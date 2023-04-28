#15. program to check given number is palindrome or not
num=input("ENter any number: ")
for i in num:
    if i[::-1]==i:
       print("It is a palindrom number")
       break
    else:
      print("It is not a palindrom number")
      break

# num=input("Enter a number: ")
# if num[::-1]==num:
#     print("It is palindrom")
# else:
#     print("It is not palindrom")