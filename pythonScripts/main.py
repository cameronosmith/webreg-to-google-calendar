import LoginScrape
import ConvertClassesToJson
import json

def run(username,password):
    listOfClasses = LoginScrape.loginRetrieveListOfCourses(username,password)
    if listOfClasses == False:
        return 'false'
    else:
        eventsData = ConvertClassesToJson.convertClassesListToJson(listOfClasses)
        print eventsData
        return eventsData
