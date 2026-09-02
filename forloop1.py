l = [1,2,3,7]
for abc in l:
    print(abc)
for num in range(1, 15, 5): # yeh 1 se 15 tak ke number print karega 5 ke gap me
    print(num)
# for k in range(10):
#     print(k + 1) yeh 1 se 10 tak ke number print karega 1 add isliye kiya gya hai taki 0 se 9 ke bajaye 1 se 10 print ho

    for j in range(11,20):
        print(j) # yeh 11 se 19 tak ke number print karega
name = ["om", "sumi", "bhaskar"]
for naam in name:
    print(naam) # yeh name list ke sare elements print karega
Name = "omBhaskar"
for char in Name:
    print(char) # yeh Name string ke sare characters print karega
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i) # yeh 1 se n tak ke number print karega
m = int(input("Enter a number: "))
#write table of any number loop
for k in range(1, 11):
    print(f"{m} x {k} = {m*k}")