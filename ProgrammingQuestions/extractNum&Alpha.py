array = [1,"a","d","s","p",2,3,"r","g",2]

num_arr = []
alpha_arr = []
for char in array:
    if str(char).isdigit():
        num_arr.append(char)
    else:
        alpha_arr.append(char)

print(alpha_arr)
print(num_arr)
