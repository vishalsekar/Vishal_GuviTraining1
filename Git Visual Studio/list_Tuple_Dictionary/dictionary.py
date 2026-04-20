# creating a empty dictionary
#example 1
dict1 = {}
print(dict1)

#example 2
dict2=dict()
print(dict1)

d={"a":100,1:200}
print(d)

#nested dictonary values 
d1={"car1":"Suzuki","car2":"Honda,toyata","car3":"Mahindra"}
print(d1)

#Indexing in dictionary
print(d1["car1"])

#Items >>

print(d1.items())

print(d1.keys())

print(d1.values())

#add element to the dictionary 

d1['car4']="nissan"
print(d1)

d2=d1.copy() #shallow copy 
d1.update({'car5':"Benz"}) #update the data 
print(d1)

print(d2)
print(id(d1))
print(id(d2))

d3={"history":40,"biology":50}
print(d.get("history"))

