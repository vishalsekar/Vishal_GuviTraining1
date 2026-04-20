'''
List is one of the most used data type and its very flexible
List is a ordered sequence of item
Each element or value that is inside the list is called an item
Declaring the list seperated by comma's are items seperated by commas are enclosed with in 
All items in the list donot need to be same type(Heterogeneous)
List is mutable ,Value of the elements of the list can be altered in the same object
'''
#create a empty list
ls1=[]
print(ls1)
ls2=list()
print(ls2)

#heterogenous
ls3=[100, 200,99.10,True,"python", 'p', "selenium"]
print(ls3)

#count of items of the list can be declared using length function 
print(len(ls3))

ls4=[100,[20,40],300]
print(len(ls4))
print(ls4)

#index
print (ls4[0])
print (ls4[1])
print (ls4[2])

#concat
ls5=[10,20,30]
ls6=["python","selenium"]
ls7=ls5+ls6
print(ls7)

#Address function
print(id(ls7))
print(id(ls6))

#Replace the existing value 
#Id will be same for the variable even if the value is changed 
ls5[1]=40
print(id(ls5))
print(ls5)
print(id(ls5))