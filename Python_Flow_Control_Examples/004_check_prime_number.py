from operator import truediv


num=int(input("Enter a number to find out if the number is prime"))
flag=False

if num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
     
