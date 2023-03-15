array = ["a",1,23,"d","p",256,"l",6]


alpha_arr = []

for element in array:
    if(isinstance(element, str)):
        alpha_arr.append(element)

print(alpha_arr)
