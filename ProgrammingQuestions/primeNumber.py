number = int(input())

count = 0
for i in range(1,number+1):
    if(number%i)==0:
        count+=1
if(count == 2):
    print("it's a prime number")
else:
    print("not a prime number")
