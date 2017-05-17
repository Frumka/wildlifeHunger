
class Positional:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.age = 0
        self.size = size
class Plant(Positional):
    def __init__(self, x, y, size):
        super(Plant, self).__init__(x, y, size)
class Bush(Plant):
    def __init__(self, x, y):
        super(Bush, self).__init__(x,y,1.0)
class Tree(Plant):
    def __init__(self,x,y):
        super(Tree, self).__init__(x,y,0.5)
class Animals(Positional):
    def __init__(self,x,y,size):
        super(Animals, self).__init__(x,y,size)
        self.speed = 0
        self.hunger = 10
        self.visionAngle = 0
        self.visionRange = 0
class Wolf(Animals):
    def __init__(self,x,y):
        super(Wolf, self).__init__(x,y,0.3)
        self.visionAngle = 360
        self.visionRange = 30
class Horse(Animals):
    def __init__(self,x,y):
        super(Horse, self).__init__(x,y,0.2)
        self.visionAngle = 120
        self.visionRange = 20
class Controller:
    def __init__(this):
        this.m = {}
    def createPlants(this):                                 #CHANGE THIS ALGORITHM, YOU'D BETTER NOT USE THIS ONE
        for i in range(20):
            this.m[i] = Bush(i,-1 ** i)
            print(this.m[i].x, this.m[i].y)
i = Controller()
i.createPlants()
#githubCoopTestDone
def setstage(this,wolfcount,sheepcount,treecount,bushcount):        this.wolfcount = wolfcount        this.sheepcount = shipcount        this.treecount = treecount        this.bushcount = bushcount        this.wolfxy = []        for i in range(wolfcount):            this.wolfx[i] = wolf            this.x = round(random.uniform(0,50),4)            this.y = round(random.uniform(0,50),4)            if this.x in this.wolfx and this.y in this.wolfy:                i-=1            else:                    this.wolfx[2*i] = round(random.uniform(0,50),4)                #Продолжить здесь!!!
