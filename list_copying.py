import copy


a: list[list[int]] = [[1,2,3], [4,5,6]]
b: list[list[int]] = copy.deepcopy(a)

print("a:", id(a))
print("b:", id(b))

b.extend([[7,8,9]])

b[0][0] = 999
print("a[0]:", id(a[0]))
print("b[0]:", id(b[0]))

print("a:", a)
print("b:", b)