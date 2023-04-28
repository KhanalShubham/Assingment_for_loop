#16. program to check given number is armstrong or not
#armstrong number=371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.
num=int(input("ENter a number: "))
sum=0
num_length=len(str(num))
for i in str(num):
    sum+=int(i)**num_length
if num==sum:
    print("GIven number is armstrong")
    
else:
    print("GIven number is not armstrong")
    
