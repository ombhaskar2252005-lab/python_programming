#write method will be used here
with open('sample2.txt','w') as file:
    file.write("Hello my name is Ranjan\n")
    file.write("And i study at RISU")
# writelines uses
with open("example.txt", "w") as file:
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)

# input
# is se ek new file bhi ban shakta ha or yah phir existing file me kuch change kr shakte ha
filename = input("Enter the file name: ")
content = input("Enter the content for the file: ")
with open(filename,'w') as file:
    file.write(content)
#read is use to print or givr output
with open (filename, 'r') as file:
    data = file.read()
    print(data)

#append mode
with open('example.txt','a') as file:
    file.write("This is append line.\n")