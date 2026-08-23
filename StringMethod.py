text = "hello Python World"
print(len(text))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
word = "   good   "
print(word.strip()) #there are also lstrip() which remove space from left and rstrip() from right
print(text.replace("World", "Java")) #last word ko replace krta ha
print(text.split())
line = ['hello', 'Python', 'World']
print(" ".join(line))
print(text.find("Python"))
print(text.count("o"))
print(text.startswith("hello"))
print(text.endswith("Java"))
num = "1234556"
print(num.isdigit())
name = "om"
print(name.isalpha())
you = "ehw7y39"
print(you.isalnum())