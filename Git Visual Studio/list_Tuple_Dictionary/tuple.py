'''
Creating the empty tuple
'''
#Example 1
t=()
print(t)

#Example 2
t1=tuple()
print(t)

#tuple is heterogenous in nature
t2=(1,2, True,"Python")
print(t2)

#find the length of the tuple
print(len(t))

#Can we print the tuple inside tuple
t3=(1,2,4,False,(8,9,10),("Python","selenium"))
print(t3)

#count how much times value 4 is repeated
t4=(1,2,4,False,4,4,(2,4,10),(4,"Python","selenium"))
print(t4.count(4))

#print the value with index position 
print(t4.index(4)) #prints the index position of the value 

'''
Sorted function is used to sort the item on the tuple
'''
t5=(1,2,5,4,3)
print(sorted(t5))

'''
Convert the tuple into list to make the tuple into mutable
'''
print(id(t5))
ls=list(t5)
print(ls)
print(id(ls)) # will have different ids 


del ls[0]
t6=tuple(ls)
print(t6)



