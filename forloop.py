for i in range(1,11):
    print("token ", i)
    #table of 2
for i in range(1,11):
    print(f"2 x {i} = {2*i}") #yahan pe f ka use string ke sath variables likhne ke liye krte hai {} ke sath
    #print("2 x", i, "=", 2*i)
#pattern
n = input("Enter the number: ")
n = int(n)
i = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ") #end ka use same line pe stay krne or space dene ke liye hota ha
    print() #it is for new line and comes in 1st for loop
    