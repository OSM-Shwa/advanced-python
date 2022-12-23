# tuples: ordered, immutable, allows duplicate elements
my_tuple = ("Max", 28, "Boston")
print(my_tuple)

item = my_tuple[0]
print(item)

# unpacking
my_tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple2

print(i1) # first element
print(i3) # last element
print(i2) # list with all middle elements
