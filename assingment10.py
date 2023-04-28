#10. Write a python program to display all the prime numbers within a given range.
a=int(input("Enter any number: "))
for aa in range(2,a):
    if aa>1:
       for i in range(2,aa):
            if aa%i==0:
                # print(i,"is not a prime number")
                break
       else:
            print(aa,"It is a prime number")
            
        


