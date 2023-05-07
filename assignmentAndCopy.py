import copy

# assignment
ls1 = [3, 4, 5]
ls2 = ls1
print(id(ls1), id(ls2))     # same

# shallow copy
# list:
#   ls[:]
#   ls.copy()
#   copy.copy(ls)

list1 = [1, 2, 3]
list2 = list1[:]
list3 = copy.copy(list2)

print("Old list: ", list1, id(list1))
print("New list: ", list2, id(list2))
print("New list: ", list3, id(list3))

# dict:
#   dict.copy()
#   copy.copy(dict)
dict1 = {1: 100, 2: 200}
dict2 = dict1.copy()
dict3 = copy.copy(dict2)

print("Old dict: ", dict1, id(dict1))
print("New dict: ", dict2, id(dict2))
print("New dict: ", dict3, id(dict3))

# deep copy
# only method: copy.deepcopy(x)
old_list = [1, 3, 5]
new_list = copy.deepcopy(old_list)

print("Old list: ", old_list, id(old_list))
print("New list: ", new_list, id(new_list))
# ids are different

for x, y in zip(old_list, new_list):
    print(id(x), id(y))
# x, y's id are the same

old_list[0] += 10
print(old_list[0], new_list[0])
# change of old_list's element will not affect new_list

old_dict = {3: 100, 4: 200}
new_dict = copy.deepcopy(old_dict)
print("Old dict: ", old_dict, id(old_dict))
print("New dict: ", new_dict, id(new_dict))
