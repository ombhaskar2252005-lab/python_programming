#AgeError is created raise error
class AgeError(Exception):
    pass

age = int(input("Enter the age: "))
if age <=18:
    raise AgeError("Age must be greater than 18")
print("Age is valid")