# Dictionary: key-value pairs, unordered, mutable

d = {"name": "Max", "age": 28, "city": "New York"}
print(d)

d2 = dict(name="Mary", age="27", city="Boston")

# access key-value pairs
value = d["name"]
print(value)

# add items to dictionary
d["email"] = "max@xyz.com"
print(d)
