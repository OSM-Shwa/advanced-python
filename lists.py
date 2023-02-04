# lists: ordered, mutable, allows duplicate elements
my_list = ["banana", "cherry", "apple"]
print(my_list)


# make a copy of a list
def list_copying():
	list_copy = my_list.copy()
	list_copy2 = list(my_list)
	list_copy3 = list_copy[:]

# list comprehension
def extracted_method():
    nums = [1, 2, 3, 4, 5, 6, 7]
    squares = [i * i for i in nums]
    print(squares)

extracted_method()

# reverses the list
my_list.reverse()
print(my_list)

new_list = sorted(my_list)
print(new_list)


# append a new item to the list
my_list.append("lemon")
print(my_list)

# insert a new item into the list at a specific index
my_list.insert(1, "blueberry")
print(my_list)

# remove the last item and return it
item = my_list.pop()
print(item)
print(my_list)

# remove a specific item
item = my_list.remove("cherry")
my_list.clear()
print(my_list)
