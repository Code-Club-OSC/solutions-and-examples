my_list = [1,2,3,4,5,6,7,8,9]

# for every number in the list, remove the number IF the number 
# can't be divided by 2 without there being a remainder
for i in my_list:
    if i % 2 != 0:
        my_list.remove(i)

print(my_list)