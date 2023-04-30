list1 = [1,5,3,7,4]

list2 = [394,573,58]
#create the new empty list where the 2 above lists will go
joined_list = []

# add all the numbers in list2 to joined_list
for i in list2:
    joined_list.append(i)

# add all the numbers in list1 to joined_list
for i in list1:
    joined_list.append(i)

print(joined_list)