#9. given number is prime or not
a=int(input("Enter any number: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
            
    
else:
    print("Invalid")