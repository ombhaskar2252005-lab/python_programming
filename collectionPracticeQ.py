print("List Practice question")
# num = list(map(int,input().split()))
# sum =0
# for i in num:
#     sum = sum + i
# print(sum)

# positive number in list
# count =0
# for i in num:
#     if i>0 :
#         print(i , end = " ")

# search an element
# ele = int(input("Enter an element to search: "))
# for i in num:
#     if i == ele:
#         print("found")

#remove a given element
# remove_num = int(input("Enter a number to remove: "))
# result = []
# for i in num:
#     if i != remove_num:
#         result.append(i)
# print(result)

# separate even and odd number
# even = []
# odd = []
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)  
# print("even: ", even)
# print("odd: ", odd)

# remove duplicate
# result = []
# for i in num:
#     if i not in result:
#         result.append(i)
# print(result)

print()
print("Dictionary practice question")
# take input and display dictionary
#student = { } # storing in dictionary or empty dictionary
# student["name"] = input("Enter name: ")
# student["age"] = int(input("Enter age: "))
# student["marks"] = int(input("Enter marks: "))
# print(student)

#Take dictionary details from the user and print every key and its corresponding value on a separate line
#n = int(input("Enter number of items: "))
# for i in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     student[key] = value
# print("Dictionary: " , student)

# for key, value in student.items(): #is se separate line me print ho jayega dictionary
#     print(key, ":", value)

# Search a key in dictionary
# search = input("Enter a key to search: ")
# if search in student:
#     print("key exists")
# else: 
#     print("not exist")

# Count the frequency of list elements
# numbers = [] #empty list
# for num in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# for num in numbers:
#     if num in student:
#         student[num] +=1
#     else:
#         student[num] = 1
# print(student) 

print()
print("Tuple question")
#Tuple Question
# tup = tuple(map(int,input().split()))
# print("Tuple: " ,tup)
# print("First element: ", tup[0])
# print("Last Element: ", tup[-1])
# target = int(input("Enter a number : "))
# count = tup.count(target)
# print(count)
# if target in tup:
#     print("Index: " ,tup.index(target))
# else:
#     print("Not exist")

#tuple in list
# temp = list(tup)
# temp.append(34)
# print("Added element in tuple: " ,tuple(temp))

#largest element in tuple
# largest = tup[0]
# for i in tup:
#     if i>largest:
#       largest = i
# print(largest)
    
print()
print("Set practice question")
list = [1,2,2,5,5,7,3,1]
temp = set(list)
print(temp) #duplicate ko print nhi karega
word = "hello"
unique = set(word)
print(unique)