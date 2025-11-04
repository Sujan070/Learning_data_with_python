class person():
    name = "anonomys"

    # def changename(self, name):
    #     self.__class__.name = name
    #     # self.name = name
    @classmethod
    def changename (cls, name):
        cls.name = name

p1 = person()
p1.changename("sujan simkhada") 
print(p1.name)
print(person.name)

class students():
    def __init__(self, phy, sci, mth):
        self.phy = phy
        self.sci = sci
        self.mth = mth
        # self.percentage = str((self.phy + self.sci + self.mth)/3) + "%"
    @property
    def percentage(self):
        return str((self.phy + self.sci + self.mth)/3) + "%"
        

st1 = students(96, 98, 95)        
print(st1.percentage)
st1.phy = 55
print(st1.percentage)
class product():
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,itm2):
        return self.price > itm2.price
    
p1 = product("rice", 2100)
p2 = product("cofee", 1600)
print(p1>p2)