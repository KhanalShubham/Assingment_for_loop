#22. Python program to calculate the sum 
#of all the even numbers within the given range.
num=int(input("Enter the range of numbers to print the sum of even numbers: "))
sum=0
for i in range(num+1):
    if i%2==0:
        sum+=i
print(f"THe sum of all even number up to range{num} is {sum}")

    