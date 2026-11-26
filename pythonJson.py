# serialization - converting python code into json using dump
import json
dict = {
    'name': 'nitish',
    'age': 20,
    'gender': 'male'
}
with open('pythonjson.txt','w') as file: #is se fild
    json.dump(dict,file,indent=4)
result = json.dumps(dict)
print(result)
print(type(result))

print()
#deserialization- converting json code into python
data = '{"name": "om", "age":19, "gender":"male"}'
student = json.loads(data)
print(student)
print(type(student))
with open('pythonjson.txt','r') as file:
    d = json.load(file)
    print(d)
    print(type(d))
