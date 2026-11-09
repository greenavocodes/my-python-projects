x = 1
list1 = []
list2 = []

# loop while condition is met
while (x < 11):
    list1.append(x)
    list2.append(x*x)
    x += 1

print (list1)
print (list2)

# collate 2 or more lists in 1
combined_lists = list1 + list2
print (combined_lists)

# make a list of lists
two_lists = (list1, list2)
print (two_lists)

# append - add to the list
list1.append(99)
print(list1)

# remove - delete an item based on value
list1.remove(99)
print(list1)

# pop - delete an item based on index
list1.pop(2)
print(list1)

print (two_lists[1])
