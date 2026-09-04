i = 1
for i in range(1,11):
    if i == 6:
        break
    print(i)

m = 4
for i in range(1,11):
    if i == 7:
        continue # Skip the rest of the loop body for i == 7
    print(f"{m} x {i} = {m*i}") 

sum = 0
while True:
    n = int(input("enter a number: "))
    if n<0:
        break
    sum = sum+n
print(sum)
#pattern printing
n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range (n):
#         print("*", end="")
#     print()

#right triangle
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

#inverted 
for i in range(n):
    for j in range(n-i):
        print("* ", end=" ")
    print()