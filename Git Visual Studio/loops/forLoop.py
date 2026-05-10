'''
ForLoop >> Each value in sequence
'''
l=[10,20,30,40,50]
for i in l:
    print(i)
    
print("Range function with all parameters")
for j in range(0,10,1):
    print(j)

print("Range function without 2 parameters")
for k in range(5):
    print(k)

print("Name in sequence")
a="Vishal"
for m in a:
    print(m)

print("Print list in order")
b=(1,2,4,5,6)
for n in b:
    print(n)

print("values using the dictionary")
c={1:"Vishal",2:"Sekar"}
for o in c.values():
    print(o)

print("out of string values")
d=[10,11,13,5]
for p in d:
    if p==11:
        print("Automation")
print("python")

print("Even numbers and odd numbers")
e=[1,2,3,6,7,8,9]
even=[]
odd=[]

for q in e:
    if q%2==0:
        even.append(q)
    else:
        odd.append(q)
    q=q+1
print(even)
print(odd)
f=(10,2,3,4,5,7,8)
even_Sum=0
odd_Sum=0
for p in f:
    if p%2==0:
        even_Sum=even_Sum+p
    else:
        odd_Sum=even_Sum+p
print(even_Sum)
print(odd_Sum)
