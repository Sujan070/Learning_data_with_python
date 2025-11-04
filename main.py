class person:
    occupation = "Data scientest"
    def person():
        print("hello .....")
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    def __init__(self, name, networth):
        self.name = name
        self.networth = networth

# a = person()
 # print(a.name)
# a.info()
# b = person()
# b.name = "Susmita"
# b.occupation = "Nurse"
# b.networth = 20000
# b.info()
c = person("Sudip",100)
c.info()

class car:
    def __init__(self):
        self.__accelator = False
        self.__brk =True
        self.clutch = False

    def start(self):
        self.clutch = True
        self.__brk = False
        self.__accelator = True
        print("car is starting")

c1 = car()
c1.start()
del c
# print(c1.__brk)

class truck():
    @staticmethod
    def start():
        print("truck is starting")

    @staticmethod
    def stop():
        print("truck is stoping")

class tatatruck(truck):
    def __init__(self, brand):
        self.brand = brand
            
t1 = tatatruck("razor")
print(t1.brand)
print(t1.start())    

class razor(tatatruck):
    def __init__(self, type):
        self.type = type

r1 = razor("gas")  
print(r1.start()) 

