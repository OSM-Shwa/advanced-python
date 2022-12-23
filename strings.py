numbers = [5, 10, 15, 20, 25]

# postive indexes
print(numbers[0])
print(numbers[3])

# negative indexes
print(numbers[-1])
print(numbers[-3])

# list slicing to create a new list containing first 3 elements of original list
new_numbers = numbers[:3]
print(new_numbers)

# slicing using steps
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums[1:6:2])
print(nums[1:6:3])

# reverse a list using step of -1
list = [1, 2, 3, 4, 5, 6, 7]
new_list = list[::-1]
print(new_list)

# changing multiple list items
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers[:3] = [-1, -2, -3]
print(numbers)
