print("Loop Question")
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i%2 == 0:
#         print(i)

# num = int(input("Enter a number: "))
# sum =0
# for i in range(1,num+1):
#     sum = sum + i
# print(sum)

# num1 = int(input("Enter a number: "))
# for i in range(1, num1+1):
#     for j in range(1, i+1):
#         print("*", end ="") # end ka use krne se woh dus
#     print()

# n = int(input("Number: "))
# fact =1
# for i in range(1,n+1):
#     fact = fact * i
# print("Factorial: ", fact)

# #prime number
# number = int(input())
# if number <2:
#     print("Not prime")
# else:
#     for i in range(2, number+1):
#         if number % i == 0:
#             print("Not prime")
#         break
#     else:
#         print("prime")

print()
print("String practice question")
#reverse of string
word = input("Enter a word: ")
result = ""
for ch in word:
    result = ch + result
if word == result:
    print("Pallindrome")
else:
    print("Not pallindrome")
print("reverse: " + result)
# count vowel in a string
string = input("Enter a string: ")
count =0
for ch in string:
    if ch.lower() in "aeiou":   # lower used krne se sare letter string ke lower me ho jayenge
        count = count+1
print("Number of vowel: " , count)