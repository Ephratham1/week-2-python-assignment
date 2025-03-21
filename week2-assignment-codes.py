#question 1: empty
my_list = []

#question 2: Append the following elements to my_list: 10, 20, 30, 40.
my_list.append([10, 20, 30, 40])

#question 3: Insert the value 15 at the second position in the list
my_list = [10, 20, 30, 40]
my_list.insert(1,15)
print(my_list)

#question 4: Extend my_list with another list: [50, 60, 70].
my_list = [10, 20, 30, 40]
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)

#question 5: Remove the element at index 2 from the list
my_list = [10, 20, 30, 40, 50, 60, 70]
my_list.remove(70)
print(my_list)

#question 6: Sort the list in ascending order
my_list = [10, 20, 30, 40, 50, 60, 70]
my_list.sort()
print(my_list)

#question 7:print index of value 30
my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list[2])

