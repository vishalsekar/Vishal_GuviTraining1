class India:
    def state(self):
        print("States of india")

class Tamilnadu(India):
    def south(self):
        print("Chennai is a capital of tamilnadu")
obj=Tamilnadu()
obj.south()
obj.state()
    

class student():
    def __init__(self,name,id,Std):
        self.name=name
        self.id=id
        self.Std=Std

s1=student("vishal",12,"5th std")
print(s1.name)
print(s1.id)
print(s1.Std)

        