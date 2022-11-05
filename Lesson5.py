class Grandparents:
    height = 170
    age = 60
    sick = 'COVID'

class Parents(Grandparents):
    age = 40
class Children(Parents):
    height = 180
    def __init__(self):
        print(self.sick)
        print(self.age)
        print(self.height)
daun = Children()

class Hello:
    def  __init__(self):
        print('Hello')
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print ("World")
HELLO_WORLD = Hello_World()
