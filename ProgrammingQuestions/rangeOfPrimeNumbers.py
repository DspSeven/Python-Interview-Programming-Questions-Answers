fst_number = int(input())
scd_number = int(input())

count = 0
for i in range(fst_number, scd_number+1):
    for j in range(1, i+1):
        if(i%j)==0:
            count += 1
    if(count == 2):
        print(i,"is prime number")
    else:
        print(i,"is not prime number")
    count = 0
