num=int(input("enter a number:"))
fact=1

if (num==0):
    print(num, "=1")
elif (num<0):
    print("Fact doesn't negative number")
else: 
    for i in range(1,num+1):
          fact=fact*i
    print(num,"! is ",fact)