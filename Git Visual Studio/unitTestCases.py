# import unittest

# def add(a,b):
#     return a+b

# class TestAddition(unittest.TestCase):
#     def testadd(self):
#         self.assertequal(add(10,30),30)

# unittest.main()
        
# import unittest

# def oddoreven1(n):
#     return n%2==0
# class oddeven(unittest.TestCase):

#  def even(self):
#     self.assertTrue(oddoreven1(10))

#  def odd(self):
#     self.assertFalse(oddoreven1(5))

# unittest.main()

# import unittest

# def primenumber(n):
#    if n<=1:
   
# class oddeven(unittest.TestCase):

#  def even(self):
#     self.assertTrue(oddoreven1(10))

#  def odd(self):
#     self.assertFalse(oddoreven1(5))

# unittest.main()

# import unittest 

# def login(username,password):
#     if username =="admin" and password =="Password123":
#         return "Successfull Login"
#     return "Failed login"

# class loginTest(unittest.TestCase):
#     def test_validLogin(self):
#         self.assertEqual(login("admin","Password123"),"Successfull Login")

#     def test_IvalidLogin(self):
#         self.assertEqual(login("systemadmin","123"),"Failed login")

# unittest.main()


# import  unittest

# def swappingtwonumbers(a,b):
#     if username =="admin" and password =="Password123":
#         return "Successfull Login"
#     return "Failed login"

# class loginTest(unittest.TestCase):
#     def test_validLogin(self):
#         self.assertEqual(login("admin","Password123"),"Successfull Login")

#     def test_IvalidLogin(self):
#         self.assertEqual(login("systemadmin","123"),"Failed login")

# unittest.main()

import  unittest

def swappingtwonumbers(a,b):
    a=a+b
    b=a-b
    a=a+b
    return a,b

class Swap(unittest.TestCase):
    def test_swap(self):
        self.assertEqual((10,20),(20,10))

unittest.main()