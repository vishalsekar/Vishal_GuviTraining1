#method created and called 
class Car:
   def start(self):
       print("Car started")

c1 = Car()
c1.start()

#method calling twice with same object
class Student:
   def set_name(self, name):
       self.name = name

   def show_name(self):
       print(self.name)

s1 = Student()
s1.set_name("Deebak")

s2 = Student()
s2.set_name("Rahul")

s1.show_name()
s2.show_name()

#class method
class Student:
   school = "ABC School"

   @classmethod
   def change_school(cls, new):
       cls.school = new

Student.change_school("XYZ School")
print(Student.school)

#Static methods
class Math:
   @staticmethod
   def add(a, b):
       print(a + b)

Math.add(2, 3)

#method overriding
class Father:
   def skill1(self):
       print("Driving")

class Mother:
   def skill2(self):
       print("Cooking")

class Child(Father, Mother):
   pass

c = Child()
c.skill1()
c.skill2()

#Method overloading
class Payment:

    def pay(self):
        print("Payment processing")


class UPI(Payment):

    def pay(self):
        print("Pay using UPI")


class CreditCard(Payment):

    def pay(self):
        print("Pay using Credit Card")


u = UPI()
c = CreditCard()

u.pay()
c.pay()

#generators
def gen():
    yield 100
    yield 200
    yield 300
for i in gen():
    print(i)

# create a decorator
def decoratorfunction(func):
    def wrapper():
        print("Welcome you all !!")
        func()
        print("Thanks for comming!!")
    return wrapper
   
#Use the decorator

@decoratorfunction
def test():
    print("How Are you !!")
test()


@decoratorfunction
def numberPrinting():
    print(1)