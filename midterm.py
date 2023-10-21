#!usr/bin/env python3
#Jacob Foppes Midterm- Campsite Reservtions 2.0 - CampRezi

import tkinter
import time
import os
import sys
from pathlib import Path
import json
import copy 
''' This program will enhace the reservation ysstemn i created for a previous project. It will store reservationa in  a master file. 
The master file will be imported as a dictionary.
EX {2023-05-19:jfoppes, 2023-05-20:jfoppes, 2023-05-30:timmyB}
reservations wikll be appended to the dictionary where created, and popped when removed.
the authenticated user will only be able to pop reservations under thier name 
progrma will use tkinter to create window with picture of campsites 
'''

''' User will authenticate with a username and password or they will create one '''

auth_usr = ""
auth_usrInfo = {} # dictionary of autherized user info 
owd = os.getcwd()
allsites = []# Defeine sites and reservations 
available = []
reserved = {}


with open("allsites.txt") as alls: #import allsites list from file
    for line in alls:
        allsites.append(line.rstrip()) 
        
with open("reservations.txt", "r") as rezis: #Import reserved sites list from file 
    for line in rezis:
        line = line.rstrip()
        (s,u) = line.split(" ", 1)
        reserved[(s)]=u # update site dictionary with site as key and person who reved as value
available = list(set(allsites) - set(reserved.keys())) #the diffenrce between all sites and reserved sites is avaible sites      


'''def loby():
    lobyW = tkinter.Tk()
    lobyW.title("CampRezi Welcome")
    lobyW.geometry("500x500")
    lobyW.configure(bg = "#333333")
    lobframe = tkinter.Frame(bg = "#333333")

    lobLab = tkinter.Label(lobframe, text = ("Hello "+ auth_usrInfo['first']+"!\n\nWelcome to CampRezi,\n Login or Make an account"),bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    lobBut1 = tkinter.Button(lobframe, text = "View Available Sites", bg = "#000000",command=lambda:[lobyW.destroy(),view()])
    lobBut2 = tkinter.Button(lobframe, text = "New Reservation",command=lambda:[lobyW.destroy(), resWin()])
    lobBut3 = tkinter.Button(lobframe, text = "Cancel Reservation",command= lambda:[lobyW.destroy(),cancelWin()])
    back = tkinter.Button(lobframe, text = "Back", command=lambda:[lobyW.destroy(),welcome()])
    
    lobLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40)
    lobBut1.grid(row = 2, column = 1)
    lobBut2.grid(row = 3, column = 1,pady = 10)
    lobBut3.grid(row = 4, column = 1)
    back.grid(row= 5,column=4)
    lobframe.pack()
    lobyW.mainloop()

def welcome(): # User greeted with login or create new account option 
    print("\n\nCamp Rezi")
    global auth_usr 
    global auth_usrInfo
    auth_usr = ""
    auth_usrInfo = {}
    
    global welcomeW
    welcomeW = tkinter.Tk()# create tkinter window
    welcomeW.title("CampRezi Welcome")
    welcomeW.geometry("500x500")
    welcomeW.configure(bg = "#333333")
    wframe = tkinter.Frame(bg = "#333333")

    welcomeLab = tkinter.Label(wframe, text = "Welcome to CampRezi!\n Login or Make an account",bg = "#333333",fg = "#FFFFFF", font=("Ariel",20)) # add labels and button to tkinter window 
    welcomeBut1 = tkinter.Button(wframe, text = "Login", bg = "#000000",command =lambda:[welcomeW.destroy(),login()]) # button lauches login window/fucntions and closes welcome winmdow 
    welcomeBut2 = tkinter.Button(wframe, text = "New Account",command= lambda: [welcomeW.destroy(),createUsrWin()]) #button laucned new account window/function and clsoese welcome window 

    welcomeLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40) # "pysically" place objects in tkiner window 
    welcomeBut1.grid(row = 4, column = 0)
    welcomeBut2.grid(row = 4, column = 2)
    wframe.pack()
    welcomeW.mainloop() # window lives off od this loop
    while True: # this while loop will handle user input and call login/ new account functions
        action = input("\nWelcome to CampRezi!\n \n What would you like to do? \n \n Login? or create an account?\n\n Type 'Login' or 'New'\n\n").lower()
        if action == "login":
            login()
            break        
        elif action == "new":
            createUsr()
            
            break
        elif action == "exit":
            break
        else: 
            print("Please enter a valid choice")
    pass

def login(): #exisiting useres login window
    global loginW
    loginW = tkinter.Tk()# define login window 
    loginW.title("CampRezi Login") #login window title 
    loginW.geometry("500x500") #window size 
    lframe = tkinter.Frame(bg = "#333333")
    loginW.configure(bg = "#333333")#window color 
   
    loginLabel = tkinter.Label(lframe, text = "Enter your Credietials",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
    loginUNT = tkinter.Label(lframe, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    loginPWT = tkinter.Label(lframe, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    loginUN = tkinter.Entry(lframe)
    loginPW = tkinter.Entry(lframe, show="*")
   # print(cusername,cpassword)
    loginBut = tkinter.Button(lframe, text = "Login",command=lambda: [chklogin(loginUN.get(),loginPW.get()),loginW.destroy()])
    back = tkinter.Button(lframe, text = "Back", command=lambda:[loginW.destroy(),welcome()])

    loginLabel.grid(row = 0, column = 0,columnspan=2,pady = 15)
    loginUNT.grid(row=1, column=0,pady=15)
    loginPWT.grid(row=2,column=0)
    loginUN.grid(row=1,column=1)
    loginPW.grid(row=2,column=1,pady = 15)
    loginBut.grid(row=3,column=0,columnspan=2)
    back.grid(row= 4,column=4)


    lframe.pack()
    loginW.mainloop()### This is a blocking function nothing after this line will run untill mainloops is loginW is destroyed '''
def chklogin(cusername,cpassword): # checks login credntials 
    #print(cusername,cpassword)
    accounts = {}
    global auth_usrInfo

    with open("accounts.txt") as auth:
        for line in auth: 
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    print("\n Login to a CampRezi account, or type exit to return to main\n")
    if cusername not in accounts:
        error("Looks look that account does not exit, try agin!")
    elif accounts[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
        global auth_usr
        auth_usr = cusername
        with open("userinfo.txt","r") as info: #opens the accounts fike to read the new accoun t info
            users = {} 
            for line in info: # reading user info file and adding it to dict of users:userinfo
                line = line.replace("\'", "\"")
                (un,inf) = line.split(" ", 1)
                inf = json.loads(inf) #intitate the values in inf as dict insterad of string
                users[(un)] = inf #string key in the dictionary users has value of the inf dicationary for that user 
            for cusername in users: # for the authenticated user: find thier entry in the users DICT and make it that authorized user info
                (un,inf) = line.split(" ", 1)
                inf = json.loads(inf)
                global auth_usrInfo
                auth_usrInfo = inf            
        print("\n Login Succesful \n")
        print("Logged in as", auth_usr,"\n")
        print("lin107",auth_usrInfo)
        auth.close() # close username and passwrod file
    else:
        error("Wrong password try agin!")
    
'''def createUsrWin(): # New users create accounts
    global mkaccW
    mkaccW = tkinter.Tk()# define login window 
    mkaccW.title("CampRezi New User") #login window title 
    mkaccW.geometry("500x500") #window size 
    mkaccframe = tkinter.Frame(bg = "#333333")
    mkaccW.configure(bg = "#333333")#window color 
    
    mkaccLabel = tkinter.Label(mkaccframe, text = "Let Make you an Account!",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
    mkaccLabel2 = tkinter.Label(mkaccframe, text = "Enter your information below",bg = "#333333",fg = "#FFFFFF",font=("Ariel",16))
    newFirstT =  tkinter.Label(mkaccframe, text = "First Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14)) #reatig text feilds in wondow 
    newLastT =  tkinter.Label(mkaccframe, text = "Last Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newNumT =  tkinter.Label(mkaccframe, text = "Phone Number",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newUNT = tkinter.Label(mkaccframe, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newPWT = tkinter.Label(mkaccframe, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newFirst = tkinter.Entry(mkaccframe)
    newLast = tkinter.Entry(mkaccframe)
    newNum = tkinter.Entry(mkaccframe)
    newUN = tkinter.Entry(mkaccframe)
    newPW = tkinter.Entry(mkaccframe, show="*")
   # print(cusername,cpassword)
    loginBut = tkinter.Button(mkaccframe, text = "Login",command=lambda: [createUsr(newFirst.get(),newLast.get(),newNum.get(),newUN.get(),newPW.get()),mkaccW.destroy(),loby()]) # run the mkuser fucntion with the information entered into the windo on press of this button , then run the loby function 
    back = tkinter.Button(mkaccframe, text = "Back", command=lambda:[mkaccW.destroy(),welcome()])

    mkaccLabel.grid(row = 0, column = 0,columnspan=2,pady = 15)
    mkaccLabel2.grid(row = 1, column = 0,columnspan=2,pady = 15)
    newFirstT.grid(row=2, column=0,pady=15)
    newLastT.grid(row=3, column=0)
    newNumT.grid(row=4, column=0,pady=15)
    newUNT.grid(row=5, column=0)
    newPWT.grid(row=6,column=0,pady =15 )
    newFirst.grid(row=2,column=1)
    newLast.grid(row=3,column=1,pady=15)
    newNum.grid(row=4,column=1)
    newUN.grid(row=5,column=1,pady = 15)
    newPW.grid(row=6,column=1)
    loginBut.grid(row=7,column=0,columnspan=2)
    back.grid(row= 8,column=4)
    mkaccframe.pack()
    
    mkaccW.mainloop()'''
def createUsr(first,last,num,un,pasw):  # these variables are passed to this fucntion form the create account window in the new user function 
    accounts = {}
    with open("accounts.txt") as auth:
        for line in auth:
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    breaker = True
    while breaker == True:
        nusername = un
        npassword = pasw
        if nusername in accounts:
            error("Looks look that account already exits, try agin!")
        else:
            global auth_usr
            auth_usr = nusername
            accounts[nusername] = npassword
            with open("accounts.txt","w") as auth: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for key, value in accounts.items():
                    auth.write('%s %s\n' % (key, value))
            with open("userinfo.txt", "a") as info:
                uInfo = {}
                uInfo['username'] = auth_usr
                uInfo['first'] = first
                uInfo['last'] = last
                uInfo['phone'] = num
                info.write('%s %s\n' % (auth_usr, uInfo)) # write the collected user info to the userinfo file 
                time.sleep(.5)
                global auth_usrInfo
                auth_usrInfo = uInfo # the acount that was jsut created is now the authrized user 
            print("Your Info : \n Name: ", auth_usrInfo["first"],auth_usrInfo["last"], "\nContact Numnber: ", auth_usrInfo['phone'])
            print("Account creation sucessfull. Logged in as: ", auth_usrInfo['username'],"\n")
            break


'''User will be able to view available sites and choose one to reserve, or cancel a reservation '''
'''def view(): # 
    print("Availvbale \n",available,"\nreserved\n",reserved)
    viewWin = tkinter.Tk()
    viewWin.title("View Sites & Reservations ")
    viewWin.geometry("900x600")
    viewWin.configure(bg="#333333")
    viewFrame = tkinter.Frame(bg="#333333")
    viewWinT = tkinter.Label(viewFrame,text="The Following Sites are reserved:")
    viewWinT.grid(row=0)
    viewWinT2 = tkinter.Label(viewFrame, text="These sites are avaible for reservation:")
    viewWinT2.grid(row=4)
    locX = 1
    for key in reserved: #create button for each key in reserved sites
        locX += 1 # increate the button location number by 1 so thye odnt overlap 
        button = tkinter.Label(viewFrame, text=key, bg="#696969", padx=10)
        button.grid(row=2,column=locX)
    locX = 1
    for site in available:
        locX += 1
        button = tkinter.Label(viewFrame, text=site,bg="#696969", padx=10)
        button.grid(row=6,column=locX)
    viewBack = tkinter.Button(viewFrame, text="Back", bg="#696969", command=lambda:[viewWin.destroy(),loby()])
    viewBack.grid(row = 8,column=0)
    viewFrame.pack()
    viewWin.mainloop()
    print("View Reservations:")
    print("\n Our location is home to the follwowing sites\n", allsites)
    print("\nThe following sites are avaialbe",available)
    print("\n The Following Sites are reserved\n",reserved)
    time.sleep(1)'''
    

'''def resWin():
    global reswin
    reswin = tkinter.Tk()
    reswin.title("Reserve")
    reswin.geometry("600x600")
    reswin.configure(bg="#333333")
    resframe = tkinter.Frame(bg="#333333")
    rwinNewT = tkinter.Label(resframe, text="Choose one of the following sites to reserve: ",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))
    locX = 1
    locY =  1
    for site in available:
        locX += 1
        if locX % 2 ==0:
            button = tkinter.Button(resframe, text=site, command=lambda site=site:[reswin.destroy(),reserve(site), sucess((site+" reserved successfully")),resWin()])# site=site ensures each button gets a unique value for site 
            button.grid(row=2,column=locX)
        else:
            locX-=1
            button = tkinter.Button(resframe, text=site, command=lambda site=site:[reswin.destroy(),reserve(site), sucess((site+" reserved successfully")),resWin()])# site=site ensures each button gets a unique value for site 
            button.grid(row=3,column=locX)
            locX+=1
        
    #error("This site is not available or des not exist")
    rwinNewT.grid(row = 0, column = 0,columnspan=10,pady = 15)
    rwinBack = tkinter.Button(resframe, text="back",command=lambda:[reswin.destroy(),loby()])
    rwinBack.grid(row=5)
    resframe.pack()
    reswin.mainloop()'''

        
'''
def cancelWin():
    canWin= tkinter.Tk()
    canWin.title("Cancel")
    canWin.geometry("900x600")
    canWin.configure(bg="#333333")
    canFrame = tkinter.Frame(bg="#333333")
    canT = tkinter.Label(canFrame,text="You have reserved the following sites:")
    locX = 1
    for key,value in reserved.items():
        if value==auth_usr: # if the site is reserved under the name of the currently loged in user
            button=tkinter.Button(canFrame,text=key,command= lambda key=key,value=value:[canWin.destroy(),cancel(key),sucess("Reservation for ",value, "removed.",cancelWin())])
            locX += 1
            button.grid(row=2,column=locX)
    canBack = tkinter.Button(canFrame,text="back", command=lambda:[canWin.destroy(),loby()])
    canT.grid(row=0)
    canBack.grid(row=5)
    canFrame.pack()
    canWin.mainloop()
    '''
def cancel(deletion):
    print("Cancel Reservation ")
    print(deletion)
    valid = reserved.get(deletion)
    if valid is not None:
        pass
    else:
        error("Please choose an available site")
    if deletion in reserved:
        reserved.pop(deletion) # add reservation to list 
        available.append(deletion) #remove reservatio nfrom avialable 
        with open("reservations.txt","w") as rezis: # writes updated reservations dict to reservations file
            for key,value in reserved.items():
                rezis.write('%s %s\n' % (key,value))
        print("Reserved Sites:\n" , reserved)
        print("Available Sites:\n" , available)
        time.sleep(1)
        
    else:
        error("Please enter a valid choice")

def error(message): # this can be called when a user makes an incorrect inout. pass the error message to this fucntion when calling it 
    errorW = tkinter.Toplevel()
    errorlab= tkinter.Label(self, text = message,bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    okBut = tkinter.Button(self, text = "Try again.",command= errorW.destroy)
    errorlab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=20,padx = 30)
    okBut.grid(row = 1, column = 0,pady=20,padx=40)


    
def sucess(message):
    successW = tkinter.Toplevel()
    successW.title("YAY!")
    successW.geometry("")
    successW.configure(bg = "#333333")
    sframe = tkinter.Frame(bg = "#333333")
    successlab= tkinter.Label(sframe, text = message,bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    okBut = tkinter.Button(sframe, text = "Back.",command= successW.destroy)
    successlab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=20,padx = 30)
    okBut.grid(row = 1, column = 0,pady=20,padx=40)
    sframe.pack(expand = True, fill="both")
    successW.mainloop()
