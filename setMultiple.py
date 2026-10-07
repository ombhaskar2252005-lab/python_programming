set1 = set(map(int,input().split()))
product=1
for i in set1:
    product=product*i
if product>1000:
    product = (product//10)+10
else:
    product = product+50
print(product)
'''
set ka use karke yahan duplicate 
value ko remove kar denge phir product
ka calculation karenge.
'''