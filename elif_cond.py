num = int(input("Enetr a number: "))
if(num<0):
    print("Negative")
elif(num == 0):
    print("zero")
elif(num == 100):
    print("special number")
else:
    print("positive") 
# nested if else
n = int(input("Enter number: "))
if(n<0):
    print("negative")
elif(n>0):
    if(n <= 10):
        print("number between 1-10")
    elif(n%2==0):
        print("even")
    else:
        print("odd")
else:
    print("positive")