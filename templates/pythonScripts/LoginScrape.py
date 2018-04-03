#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re
from EnrolledClass import EnrolledClass
from ExtraMeeting import ExtraMeeting
from convertClassesToJson import convertClassesListToJson



"""
method to login to webreg and return a list of Enrolled Classes objects
"""
def loginRetrieveListOfCourses(username,password):
    #navigate to page
    browser = webdriver.PhantomJS('phantomjs')

    browser.get('https://act.ucsd.edu/webreg2')
    #login
    usernameField = browser.find_element_by_id("ssousername")
    passwordField = browser.find_element_by_id("ssopassword")
    usernameField.send_keys(username)
    passwordField.send_keys(password, Keys.RETURN)
    #page will now be redirected, wait for it
    try:
        wait = WebDriverWait(browser,10)
        wait.until(lambda browser: browser.current_url != 
                "https://a4.ucsd.edu/tritON/Authn/UserPassword")
    except TimeoutException as ex:
        #bad credentials
        print 'false credentials'
        print ('credentials'+username+password);
        return False
    #we are now at the page where we just press go
    #we need to select the spring 2018 option from the dropdown list
    WebDriverWait(browser, 4000).until( \
            EC.visibility_of_element_located((By.ID, "startpage-select-term")) \
            )
    dropdown = browser.find_element_by_id('startpage-select-term')
    for option in dropdown.find_elements_by_tag_name('option'):
        if option.text == 'Spring Quarter 2018':
            option.click() # some places online say this should be select
    #looking for button now
    print "looking for button"
    goButton = browser.find_element_by_id("startpage-button-go")
    goButton.click()
    #we are now at the page with the user's classes
    wait.until(lambda browser: browser.current_url !=
            "https://act.ucsd.edu/webreg2/start" )
    #browser.get('/home/cameron/Documents/projects/webregCalendar/sampleWebRegPage/webregMain.html')
    tbody = browser.find_elements_by_xpath("//tbody")



    td = tbody[7] 
    #print td.text
    children = td.find_elements_by_xpath(".//*")
    global er #enrolled class var
    global em #extra meeting class var
    lookingForClass = True #boolean to keep track of whether adding data to the class or extra meeting
    listOfClasses = list()

    for i, elem in enumerate(children):
        if elem.get_attribute("aria-describedby")=="list-id-table_CRSE_TITLE" \
                and elem.text and re.search('[a-zA-Z]', children[i-1].text):
                    #this is the start of a course

            #checking to see if there is an extra meeting object already stored in em
            #if there is, store it in the enrolledclasses list, if not, then create a new one
            try:
                if em is None: 
                    print "\n"
            except NameError:
                print "\n"
            else:
                er.addExtraMeeting(em)
            #checking to see if there is an enrolled class object already stored in er
            #if there is, store it in the enrolledclasses list, if not, then create a new one
            try:
                if er is None: 
                    print ""
            except NameError:
                print ""
            else:
                listOfClasses.append(er)

            lookingForClass = True
            er = EnrolledClass()
            er.setName(children[i-1].text+" "+elem.text)
            continue
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_FK_CDI_INSTR_TYPE" \
                and elem.text!="LE" and re.search('[a-zA-Z]', elem.text):
                    #this is a non-lecture class, such as discussion or lab
            #checking to see if there is an enrolled class object already stored in em
            lookingForClass = False
            try:
                if em is None: 
                    print "\n"
            except NameError:
                print "\n"
            else:
                er.addExtraMeeting(em)

            #crete a new enrolled class
            em = ExtraMeeting()
            em.setType(elem.text)
            continue
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_PERSON_FULL_NAME" \
                and re.search('[a-zA-Z0-9]', elem.text):
                    #print "teacher is " + elem.text
            er.setTeacher(elem.text)
            continue
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_DAY_CODE" \
                and re.search('[a-zA-Z0-9]', elem.text):
                    #print "days are " + elem.text
            if lookingForClass:
                er.setDays(elem.text)
            else:
                em.setDays(elem.text)
            continue
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_coltime" \
                and re.search('[a-zA-Z0-9]', elem.text):
                    #print "times are " + elem.text
            if lookingForClass:
                er.setTime(elem.text)
            else:
                em.setTime(elem.text)
            continue
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_BLDG_CODE" \
                and re.search('[a-zA-Z0-9]', elem.text):
                    #print "building is " + elem.text
            if lookingForClass:
                er.setBuilding(elem.text)
            else:
                em.setBuilding(elem.text)
            continue           
        elif elem.text and elem.get_attribute("aria-describedby")=="list-id-table_ROOM_CODE" \
                and re.search('[a-zA-Z0-9]', elem.text):
                    #print "room is " + elem.text
            if lookingForClass:
                er.setRoom(elem.text)
            else:
                em.setRoom(elem.text)
            continue           
    #take care of the 'dangling' class
    try:
        if em is None: 
            print ""
    except NameError:
        print ""
    else:
        er.addExtraMeeting(em)
    try:
        if er is None: 
            print ""
    except NameError:
        print ""
    else:
        listOfClasses.append(er)
    return listOfClasses

