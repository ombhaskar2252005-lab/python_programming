name = ["om", "bhaskar", "ALOK", 77, False, 77]
numbers = [1,2,3,4,5]
if (name[3]==name[5]):
    print("it can have duplicate values.")
print(type(name))
print(len(name))
print(name[1])
print(name[-2]) #toh yahan pe  length of list -2 toh hmko jo milega woh kisika index hoga
print(name[4])
if "77" in name: #yahan "77" ek string ha or aise check string me bhi kar shakte ha
    print("yes")
else:
    print("no")

print(name[0:6:2]) #jumping

#lists comprehension
numbers = [1,2,3,4,5]
cube = [num*num*num for num in numbers]
print(cube)

#List Methods
num = [1,4,9,3,5,8]
print("List Methods " , num)
# num.append(7)
# print("appends " , num)

# num.sort()
# print("Sort\n " ,num)

# num.reverse()
# print("Reverse\n ",num)

# num.insert(1,2)
# print("add one new value: " ,num)

# name1 = ['om','sumi','namita']
# name2 = ['mannu','bhaskar']
# name1.extend(name2)
# print("added new element in list: ",name1)

# combined_name = name1 + name2
# print("same as extend: " ,combined_name)

# ind = num.index(4)
# num[ind] = 6
# print("4 ke jagah new value: " , num)

# num.remove(3)
# print(num)

# x = num.pop(2)
# print(x)
# print(num)

# del(num[0])
# print(num)

# num.clear()
# print(num)

# word = ['ok', 'okay','ok','k'] it is used to count how many time that value appear in list
# n=word.count("ok")
# print(n)

new_num = num.copy()
print(new_num)