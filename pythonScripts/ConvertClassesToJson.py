import json
import datetime as dt
import dateutil.parser as dparser


"""
method to return a list of gcal api standard event objects
from a list of EnrolledClass objects
""" 
def convertClassesListToJson(classesList):
    #we are going to design the json tree structure to mirror
    #the google calendar event api 
    events = list()
    for course in classesList:
        #end
        events.append(createEvent(course.getName(),course))
        #handle extra meeting classes
        for em in course.getExtraMeetings():
            events.append(createEvent(\
                    em.getType()+':'+course.getName(),em))
       
#    print json.dumps(events)
    return events

#helper methods to convert the time to google api standards
"""
method thats returns an event (google event) object 
from a course or extra meeting
@param name: the name of the meeting
@param meeting: the meeting object (either enrolled class or extra meeting)
"""
def createEvent(name, course):
    eventData = {}
    eventData['summary']=name
    eventData['location']="Building:"+course.getBuilding()\
            +", Room:"+course.getRoom()
    #new objects for time data
    start={}
    start['timeZone']='America/Los_Angeles'
    start['dateTime']=convertDateStandard(course.getDays())[0]+'T'+\
            convertTimeStamp(course.getTime())[0]
    eventData['start']=start
    end={}
    end['timeZone']='America/Los_Angeles'
    end['dateTime']=convertDateStandard(course.getDays())[0]+'T'+\
            convertTimeStamp(course.getTime())[1]
    eventData['end']=end
    #recurrences
    if len(convertDateStandard(course.getDays()))>1:
        strDays = ""
        for index, val in enumerate(convertDateStandard(course.getDays())):
            if index==0:
                continue
            strDays=strDays+val
            if index!=len(convertDateStandard(course.getDays()))-1:
                strDays=strDays+','
        eventData['recurrence']=['RRULE:FREQ=WEEKLY;WKST=SU;BYDAY='+strDays]
    return eventData
"""
method to convert the default webreg time stamp to 
rfc standard
@param wrts: the webreg timestamp
@return: a list of the two stamps
    input: 9:30a-2:29p
    output:[date1,date2]
"""
def convertTimeStamp(wrts):
    twoStamps = wrts.split("-")
    ts1Converted = convertTime12To24Hour(twoStamps[0])
    ts2Converted = convertTime12To24Hour(twoStamps[1])
    return [ts1Converted,ts2Converted]
"""
method to convert a single stamp stamp to military time
@param stamp: the single time stamp
example:
    input:2:30p
    output:14:30
"""
def convertTime12To24Hour(stamp):
    date=dparser.parse(stamp)
    return date.strftime('%H:%M:%S')
"""
method to convert the date to rfc standard
there are two possible types of inputs:
    for normal classes is a list of days: TuTh
    for a final exam is a date: M 06/11/2018
output should be in format of 2015-05-28
the output is going to be a list. the first value in the list will be the 
date of the first meeting. subsequent elements will be the days it reoccurs
in format of MW,F
"""
def convertDateStandard(wrdate): #wrdate is webreg date
    #check if it is the final date with /'s
    if '/' in wrdate:
        #this is a final exam date
        truncated = (wrdate.split(' '))[1] #removed the day letter
        columns = truncated.split('/')
        day = columns[1]
        month = columns[0]
        year = columns[2]
        dates = list()
        correctDateFormat=year+'-'+month+'-'+day
        dates.append(correctDateFormat)
        return dates
    else: #this is a MTuF format
        listOfDays = list() #list of recurring days capitalized
        listOfDistancesFromMonday = list() #monday is 0, tu is 1, etc
        #iterate through chars to get MWF days
        for index, char in enumerate(wrdate):
            if char=='M':
                listOfDays.append('MO') #monday
                listOfDistancesFromMonday.append(0)
            elif char=='T': #tuesday or thursday
                if wrdate[index+1]=='u': 
                    listOfDays.append('TU') #tuesday
                    listOfDistancesFromMonday.append(1)
                else:
                    listOfDays.append('TH') #thursday
                    listOfDistancesFromMonday.append(3)
            elif char=='u' or char=='h':
                continue
            elif char=='W':
                listOfDays.append('WE') #wednesday
                listOfDistancesFromMonday.append(2)
            else:
                listOfDistancesFromMonday.append(4) #friday
                listOfDays.append('FR')
        #now create the dates list
        startDate=dparser.parse("4/2/18") #this is the start of spring quarter
        firstDate=startDate+dt.timedelta(days=\
                listOfDistancesFromMonday[0])
        return [firstDate.strftime('%Y-%m-%d')]+listOfDays
            
#print convertDateStandard('MTuW')
print convertTimeStamp('3:00p-5:59p')
