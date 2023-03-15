mul_of_3_and_5=[]
for i in range(1,101):
    three = i%3 == 0
    five = i%5 == 0
    combination = three and five
    if(combination):
        mul_of_3_and_5.append(i)
print(mul_of_3_and_5)
