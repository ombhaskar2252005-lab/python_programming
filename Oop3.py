#static ka code likhna ha 
# static variable
class student:
    college = "ABC College" # static variable
    def __init__(self, name):
        #instance variable
        self.name = name
s1 = student("OM")
print(s1.name)
print(s1.college)
s2 = student("Riya")
print(s2.name)
print(s2.college)

#static methods
#1
class student:
    college = "RISU"

    def show(self):
        print("Instance method")

    @staticmethod
    def info():
        print("Static method")
no = student()
print(no.college)
student.info()
no.show()
#2
class calculator:
    @staticmethod
    def add(a,b):
        return a+b
c1 = calculator()
print(calculator.add(12,33))
print(c1.add(10,20))