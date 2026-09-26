try:
    a = int(input("enter number: "))
    print(f"Multiplication table of {a} is: ")
    for i in range(1,11):
        print(f"{a} x {i}= {a*i}")
except:
    print("Invalid input! ")
print("done")

try:
    name = int(input("Enter a number: "))
    print(name)
except ValueError:
    print("ERROR! Enter a integer")

try:
    l = [1,2,3,4]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occur")
finally:
    print("always executed")