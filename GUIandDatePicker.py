""""
Provides GUI and Date

"""

import datetime 

import tkinter
from tkinter import *
from tkinter import messagebox

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

global INQUIRYDATE

def visitSiteInputDate(date):
    browser = webdriver.Firefox()
    browser.get('https://imperial.courts.ca.gov/CourtCalendars/Public/MCalendars.aspx')
    
    dateelem = browser.find_element_by_id('datepicker')
    dateelem.send_keys(date.strftime('%x'))

    submitbutton = browser.find_element_by_name('Button1')
    submitbutton.click()

def makedatetoday():
    global INQUIRYDATE 
    INQUIRYDATE = datetime.date.today()
    
def makedatetomorrow():
    global INQUIRYDATE
    INQUIRYDATE = datetime.date.today() + datetime.timedelta(days=1)
    
def makeotherdate():
    global INQUIRYDATE
    INQUIRYDATE = customDate.get()
    
def pullcalendar():
    global INQUIRYDATE
    print(INQUIRYDATE)
    visitSiteInputDate(INQUIRYDATE)

master = Tk()
Label(master, text="Date").grid(row=4)
customDate = Entry(master)
customDate.grid(row=5)

b1 = Button(master, relief="raised", text="TODAY", command=makedatetoday)
b1.grid(row=1)
b2 = Button(master, relief="raised", text="TOMORROW", command=makedatetomorrow)
b2.grid(row=2)
b3 = Button(master, relief="raised", text="CUSTOM", command=makeotherdate)
b3.grid(row=3)
b4 = Button(master, relief='raised', text='PULL CALENDAR', command=pullcalendar)
b4.grid(row=6)

mainloop()



