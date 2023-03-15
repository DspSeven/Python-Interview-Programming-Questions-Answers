arr = [1,2,3,3,4,5,6,6,7]

new_arr = []
duplicates = []
for i in arr:
    if(i in new_arr):
        duplicates.append(i)
    else:
        new_arr.append(i)
        
print("Original Array are: ",new_arr)
print("duplicates are: ",duplicates)
