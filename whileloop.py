# i = 0
# while i<5:
#     print("om")
#     i = i+1

#ulta number
# n = int(input("Enter a number: "))
# while n>0:
#     print(n)
#     n = n-1
#maximum number
n= int(input("Enter how many numbers: "))
i =1
maximum = 0
while i<=n:
    num = int(input("Enter a number: "))
    if num > maximum:
        maximum = num
        i = i +1
        print("Maximum number is: ", maximum)
