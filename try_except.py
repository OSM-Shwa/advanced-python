def example1():
    try:
        f = open("text.txt")
        if f.name == "text.txt":
            raise Exception # jumps to where you handle that exception (in the except clause)
    except FileNotFoundError as e:
        print(e)
        # print("Sorry, this file does not exist!")
    except Exception as e2:
        print("Error!")
        # print("Sorry, something went wrong.")
    else: # run this code if the try clause does not throw an error/exception
        print(f.read())
        f.close()
    finally: # this code will run whether the above code throws an exception or not
        print("Executing Finally...")
        
        
    # https://www.youtube.com/watch?v=NIWwJbo-9_8&t=5s



try:
    # code that may cause an exception
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print(result)
    
    my_list = (1, 2, 3)
    i = int(input("\nEnter index: "))
    print(my_list[i])
except ZeroDivisionError:
    # code to run when the exception occurs
    print("Denominator cannot be 0. Please try again.")
except IndexError:
    print("Index cannot be greater than the size of the list!")
finally:
    print("Always printed.")
    
print("Program ends...")