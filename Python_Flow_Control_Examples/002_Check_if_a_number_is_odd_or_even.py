# num=int(input("Can you enter number?"))

# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd/n")

#########################

# list=range(1,20)

# for val in list:
#     if (val%2)==0:
#         print("number is even",val)
#     else:
#         print("number is odd",val)
     
#################################

even=0
odd=0
sumEven=0
sumOdd=0

n=int(input("how many enter the number?"))
for i in range(n):
    num=int(input("sayi: "))
    if(num%2==0):
        even+=1
        sumEven+=num
    else:
        odd+=1
        sumOdd+=num
if(even!=0):
    print("Sum of even numbers:",sumEven/even)
if(odd!=0):
    print("Sum of odd numbers:", sumOdd/odd)
    
    
    
    
