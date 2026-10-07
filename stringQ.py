word = input("Enter a word: ")
result = ""
for ch in word:
    if ch not in result:
        result = result + ch
print(result)
'''
toh is code ka use ye hai ki same word me 
bar bar ane wale character ek hi bar 
print karega jaise ki agar input me banana 
aaya toh output me ban print hoga 
'''