class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def check_pass_fail(self):
        return True if self.marks >= 60 else False


# Student 1
s1 = Student("Harry", 80)
print(s1.name)
print(s1.marks)

did_pass = s1.check_pass_fail()
print(did_pass)

# Student 2
s2 = Student("Janet", 50)
print(s2.name)
print(s2.marks)

did_pass = s2.check_pass_fail()
print(did_pass)
