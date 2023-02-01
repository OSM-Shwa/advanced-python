def do_one(x):
    print("one: x*1 = ", x*1)
    
def do_two(x):
    print("two: x*2 = ", x*2)
    
def do_three(x):
    print("three: x*3 = ", x*3)
    
    
def do_default(x):
    print("default: x = ", x)
  
  
# bad control flow  
x = 2

if x == 1:
    do_one(x)
elif x == 2:
    do_two(x)
elif x == 3:
    do_three(x)
else:
    do_default(x)
    
    
# good flow control with dictionaries
actions = {1:do_one, 2:do_two, 3:do_three}
actions.get(x, do_default)(x)

# https://www.youtube.com/shorts/UFdEp9wrtOY