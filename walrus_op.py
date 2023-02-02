# walrus operator

# assignment operator aka walrus operator
# assigns value to variables as part of a larger expression


# without
# foods = list()
# while True:
#     food  = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# with
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
    
    
# https://www.youtube.com/watch?v=2KzyvzeWFbQ