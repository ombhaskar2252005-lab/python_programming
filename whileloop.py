# i = 0
# while i<5:
#     print("om")
#     i = i+1

#ulta number
# n = int(input("Enter a number: "))
# while n>0:
#     print(n)
#     n = n-1

#count 1 to 10
# i =1
# while i<=10:
#     print(i)
#     i = i+1

#even number count
# n = int(input("Enter a number: "))
# i = 1
# count =0
# while i<=n:
#     if (i % 2 == 0):
#         count = count +1
#     i = i+1
# print(count)

#table of n
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i = i + 1


#sum 1 to n
# n = int(input("Enter a number: "))
# i =1 
# sum =0
# while i <=n:
#     sum = sum + i
#     i = i+1
# print(sum)

#sum of odd number
# n = int(input("Enter a number: "))
# i =1
# sum = 0
# while i<=n:
#     if(i%2 != 0):
#         sum = sum +i
#     i = i+1
# print(sum)


#reverse number
# n = int(input("Enter a number: "))
# rev =0
# while n>0:
#     temp = n%10 #remainder deta ha yah last digit deta ha
#     rev = rev*10 + temp
#     n = n//10 #decimal number hata deta ha or last digit ko hata deta ha
# print(rev)

#count the number of digits
n = int(input("enter number: "))
count = 0
while n>0:
    n = n//10
    count = count + 1
print(count)