class ClassesTextToJson:

    def __init__(self,listOfClasses):
        self.listOfClasses=listOfClasses
    
    def createClassesFromText(self, text):
        leadingSpaces = len(text)-len(text.lstrip(' '))
        if leadingSpaces == 0:
            #this is a class such as math lecture
            #self.lastClassRef = new EnrolledClass()
            tokens = text.split()
            #get department code
            deptCode = tokens[0]+tokens[1]
            print "dept.code = "+deptCode;
            #getName
            className=""
            classNameFin = False
            for t in tokens[2:]:
                if not self.isSectionCode(t) and not classNameFin:
                    className+=t+" "
                    continue
                elif self.isSectionCode(t):
                    classNameFin = True
                    continue

            print "className:"+className
            #ge
            for t in tokens:
                print t
        else:
            #this is a subclass such as discussion, lab
            print "subclass"

    """
    method to check whether the given input is a section code
    note: section code looks like A00
    @param input: the string to check whether it is a section code
    """
    def isSectionCode(self, input):
        input = input.replace(" ","")
        print input
        if len(input) != 3:
            return False
        if input[0].isdigit():
            return False
        if not input[1:2].isdigit():
            return False
        return True

a = ClassesTextToJson(["hi"])
a.createClassesFromText("CSE  20   Intro/Discrete Mathematics B00 LE Micciancio, Daniele L 4.00 MWF 10:00a-10:50a CENTR 212 Enrolled")


