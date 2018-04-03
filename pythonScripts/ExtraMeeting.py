#class for meetings other than lecture
class ExtraMeeting:
    def __init__(self):
        self.type="TBA"
        self.days="TBA"
        self.time="TBA"
        self.building="TBA"
        self.room="TBA"


    #self explanatory setter methods
    def setType(self,type):
        if type == 'DI':
            self.type='Discussion'
        elif type == 'LA':
            self.type='LAB'
        elif type == 'FI':
            self.type='Final'
        else:
            self.type=type
    def setDays(self,days):
        self.days=days
    def setTime(self,time):
        self.time=time
    def setBuilding(self,building):
        self.building=building
    def setRoom(self,room):
        self.room=room
    #getters
    def getType(self):
        if(self.type):
            return self.type
        else:
            return ""
    def getDays(self):
        if(self.days):
            return self.days
        else:
            return ""
    def getTime(self):
        if(self.time):
            return self.time
        else:
            return ""
    def getBuilding(self):
        if(self.building):
            return self.building
        else:
            return ""
    def getRoom(self):
        if(self.room):
            return self.room
        else:
            return ""

    def printStats(self):
        print self.getType()+self.getDays()+self.getTime()+self.getBuilding()+self.getRoom()



