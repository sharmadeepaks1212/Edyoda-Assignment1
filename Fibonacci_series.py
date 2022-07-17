#Python program to find Fibonacci series.
num= int(input("enter any number to find the fibonacci series:   " ))
num1=0
num2=1
if num<=0:
    print("Enter a valid number")
else:
    
    for i in range(0,num):
        sum=num1+num2 
        num1=num2 
        num2=sum  
        print(sum)    