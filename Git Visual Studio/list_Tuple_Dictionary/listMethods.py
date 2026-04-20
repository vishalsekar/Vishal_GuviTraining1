'''
Append : used to create only one item at the end of the list 
Item can be any kind of datatype
'''
ls1=[10,20,30]
ls2=["Python"]
#ls1.append(40)
#print(ls1)
#ls1.append("Selenium")
#print(ls1)
#ls3=ls1.append(50,60) --> False >> Append takes only one arguement at a time

ls1.append([40,50])

'''
Extend Used to add multiple item in the list 
It adds each item individually in the end
'''
ls1.extend([60,50])
print(ls1)

'''
Insert Function >> Used to insert a item in a specific index position 
Variable.insert(x,y) will add item element "Y" at location index "X"
'''

ls3=[11,12,13,14] 
ls3.insert(3,15)
print(ls3)

'''
Remove >> 
helps remove the item in the cart from the index position
If value repeats it removes the first value 
'''
ls3.remove(11) #removes the 11 from the existing list 
print(ls3)

'''
Pop>>
Used to remove a item based on the index
By default it selects the index number as -1 which is the last value if the index value is not provided 
'''
ls3.pop(3)
print(ls3)

'''
Clear>>
Used to clear all items in the list and return empty list 
'''
ls4=[1,2,3,4]
ls4.clear
print(ls4)

'''
Delete >>
Delete will clear/delete the entire object 
'''
# ls5=["Pune","Chennai","Mumbai","Banglore"]
# del ls5
# print(ls5)

'''
count function >>
Helps to count how much time the specific value is repeated
'''
ls6=[1,2,1,1,2,4,5,1,6,1]
print(ls6.count(1))

'''
Reverse>>
helps to reverse the list 
'''
ls6.reverse()
print(ls6)

'''
Sort >>
Sort function helps to print in the asscending order 
to print in the descending order we need to use the reverse function with the sort function
'''

ls7=[1,3,4,5,6,0,1]
ls7.sort()
print(ls7)
ls7.sort(reverse=True)
print(ls7)

'''
Deep copy >> indicates the same object of the copied object
'''
a=[1,2,3,4]
b=a
b.append(5)
print(a) 
print(id(a))
print(b)
print(id(b))

'''
Shallow copy >> it indicates the different object 
'''
x=[1,2,3]
y=a.copy()
y.append(5)
print(x)
print(id(x))
print(y)
print(id(y))