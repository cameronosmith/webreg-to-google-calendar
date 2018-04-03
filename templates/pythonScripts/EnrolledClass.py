class EnrolledClass:
    """
        constructor for the enrolled class
        @param name: name of class 
        @param days: the days of the class in format 'MWF'
        @param time: time in form '8:00p-8:50p'
        @param place: the location of the class
        """
    def __init__(self):
        self.extraMeetings = list()
        self.name="TBA"
        self.teacher="TBA"
        self.days="TBA"
        self.time="TBA"
        self.building="TBA"
        self.room="TBA"

    #self explanatory getter/setter methods
    def setName(self,name):
        self.name=name
    def setTeacher(self,teacher):
        self.teacher=teacher
    def setDays(self,days):
        self.days=days
    def setTime(self,time):
        self.time=time
    def setBuilding(self,building):
        self.building=building
    def setRoom(self,room):
        self.room=room
    #getters
    def getName(self):
        if(self.name):
            return self.name
        else:
            return ""
    def getTeacher(self):
        if(self.teacher):
            return self.teacher
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
    def getExtraMeetings(self):
        return self.extraMeetings

    #other helper methods

    #method to print the stats of this class
    def printStats(self):
        print "printing stats..."
        print self.getName()+self.getDays()+self.getTime()+self.getBuilding()+self.getRoom()
        print "printing extra classes for "+self.getName()
        for elem in self.extraMeetings:
            elem.printStats()

    #method to add an extra meeting to the list of extra meetings
    #@param extraClass: the extra class object to add
    def addExtraMeeting(self, extraMeeting):
        self.extraMeetings.append(extraMeeting)


