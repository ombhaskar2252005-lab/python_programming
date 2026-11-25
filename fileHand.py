with open('sample1.txt','r') as file:
    content = file.read()
    print(content)
with open('sample2.txt','w') as file:
    content = file.write("kaisa ho") 
''' w (write) ke use se sample2 file me likha hoya change ho jayega or naya line ajayega
agar koi file exist nhi krta hai toh woh bana dega jaise niche wale code ko se'''
with open('text.txt','w') as file:
    file.write("mera naam om ha") #text.txt se file me woh likha jo tm chahete ho

with open('sample1.txt','a') as file:
    file.write("\nHii I am fine") 
    """ a se jo line hmlok likhe ha woh sample1 me likha jayega """