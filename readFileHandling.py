# 1. read()
with open('sample1.txt','r') as file:
    f = file.read() # 10 se 10 character count karke print kr dega
    print(f)

print()
# 2.readline()
with open('sample1.txt','r') as files:
    print(files.readline(), end='')
    print(files.readline(), end='')

    print()

# this is the code to print the all content which is in the file
with open('sample1.txt','r') as file:
    while True:
        data = file.readline()
        if data == '':
            break
        else:
            print(data.strip())

#3.readlines()
with open('sample1.txt','r') as filee:
    print(filee.readlines()) # it will print in list
# to print them without list
with open('sample1.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

print()
# tell and seek
# 1. tell
with open('text.txt','r') as file:
    print(file.read(10))
    print(file.tell())
    file.seek(0) #2.seek
    print(file.read(5))