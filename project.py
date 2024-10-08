num=int(input("Enter number : "))
count=0
while num !=0:
    num//=10
    count+=1
print("The number of digits in number are",count)