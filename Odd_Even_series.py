#Python program to find total number of odd and even numbers in a given series. 
series=(2,4,5,45,7,9,93,101,112,66,32)
even=0
odd=0
for n in series:
    if(n%2==0):
        even+=1
    else:
        odd+=1
print("even number",even)
print("odd number",odd)       