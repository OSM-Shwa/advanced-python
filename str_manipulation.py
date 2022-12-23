# Basic Syntax
# s[start:step:stop]

# Relevant Links
# - [https://www.learnbyexample.org/python-string-slicing/, https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/]


# Question 1:
def question1():
    str1 = input("Enter a string: ")
    if len(str1) < 3:
        print("The string you entered is too short!")
    else:
        print(str1[-3:])


# Question 2:
def question2():
    str = input("Please enter a string: ")
    idx = 0
    while True:
        print(str[idx])
        idx += 1
        if idx > len(str):
            break


# Question 3:
def question3():
    word = input("Please enter a string: ")
    idx = 1
    while True:
        print(word[idx])
        idx += 2
        if idx >= len(word):
            break


# Question 4:
def question4():
    sentence = input("Please enter a string: ")
    length = len(sentence)
    if length >= 4:
        newSentence = sentence[0:2] + sentence[-2:]
    else:
        print("The string you entered is too short!")

    return newSentence

    print(question4())


# Question 5: Solution 1
def middle_char(txt):
    text = input("Please enter a string: ")
    print(f"Middle character(s) of said string: {middle_char(text)}")

    return txt[(len(txt) - 1) // 2 : (len(txt) + 2) // 2]


# Question 5: Solution 2
def question5():
    sentence = input("Please enter a string: ")
    length = len(sentence)
    if length % 2 == 0:
        idx = length // 2 - 1
        print(sentence[idx : idx + 2])
    else:
        idx = length // 2
        print(sentence[idx])


# Question 6:
def question6():
    str = input("Please enter a string: ")
    length = len(str)
    if length >= 3:
        if str[-3:] == "ing":
            str = str + "ly"
        else:
            str = str + "ing"

        print(str)


# Question 7:
def question7():
    firstName = input("Enter your first name: ").capitalize()
    lastName = input("Enter your last name: ").capitalize()
    fullName = f"{firstName} {lastName}"
    print(fullName)


# Question 8:
def isPalindrome(s):
    return (
        s == s[::-1]
    )  # You can reverse a string by omitting the start, stop and setting the step as -1

    s = "joshua"
    ans = isPalindrome(s)

    if ans:
        print("Yes")
    else:
        print("No")


# Question 9
def question9():
    str = input("Enter a string: ")
    cats = str.count("cat")
    dogs = str.count("dog")

    if cats > dogs:
        print("There are more cats than dogs!")
    elif dogs > cats:
        print("There are more dogs than cats!")
    else:
        print("There are the same amount of dogs as cats!")

    """for idx in range(len(str)):
            if str[idx : idx + 3] == "cat":
                cats += 1
            elif str[idx : idx + 3] == "dog":
                dogs += 1
    """
