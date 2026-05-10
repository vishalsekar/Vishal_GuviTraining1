class role:
    roleName="Tester"

    @classmethod   #annotation
    def changerole(cls,newrole):
         cls.roleName = newrole
         print(cls.roleName)
role.changerole("Developer")
