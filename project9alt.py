import tkinter as tk
from tkinter import ttk
import midterm as mid
import os
import json
auth_usr = {"username":"", "first":"", "last":"", "phone":""}
auth_usrInfo = {"username":"", "first":"", "last":"", "phone":""} # dictionary of autherized user info 
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


LARGE_FONT =("Verdona", 12)
class CampReziApp(tk.Tk): # this is the parent class for the application itself, hower it takes tk.Tk as a parent to initialze an instace of tkinter 
    
    def __init__(self, *args, **kwargs):# define a calss that takes an unkmnown number are arguments and keyword arguments 
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"CampRezi")
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for f in (StartPage, Login, NewUser, Lobby, View, New, Cancel):#n add the frames within each of these calsses to the frames Dict to be called upon wehn the class is called 
            frame = f(container,self)
            self.frames[f]=frame 
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
        
    def show_frame(self,cont): # show the frame requested in the over arching container frame for the application 
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame): # this calss takes tk.Frame as a parent in order to establish a window frame that this class and the rest can use to display obejct 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        welcomeLab = tk.Label(self, text = "Welcome to CampRezi!\n Login or Make an account",bg = "#333333",fg = "#FFFFFF", font=("Ariel",20)) # add labels and button to tkinter window 
        welcomeBut1 = ttk.Button(self, text = "Login",command =lambda: controller.show_frame(Login)) # button lauches login window/fucntions and closes welcome winmdow 
        welcomeBut2 = ttk.Button(self, text = "New Account",command= lambda: [controller.show_frame(NewUser)]) #button laucned new account window/function and clsoese welcome window 
        welcomeLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40) # "pysically" place objects in tkiner window 
        welcomeBut1.grid(row = 4, column = 0)
        welcomeBut2.grid(row = 4, column = 2)
        
class Login(StartPage):
    global authuserinfo
    authuserinfo = {"username":"", "first":"", "last":"", "phone":""}
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        loginLabel = tk.Label(self, text = "Enter your Credietials",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
        loginUNT = tk.Label(self, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        loginPWT = tk.Label(self, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        loginUN = tk.Entry(self)
        loginPW = tk.Entry(self, show="*")
    # print(cusername,cpassword)
        loginBut = ttk.Button(self, text = "Login",command=lambda: [self.chklogin(loginUN.get(),loginPW.get(),controller)])
        back = ttk.Button(self, text = "Back", command=lambda:[controller.show_frame(StartPage)])

        loginLabel.grid(row = 0, column = 0,columnspan=2,pady = 15)
        loginUNT.grid(row=1, column=0,pady=15)
        loginPWT.grid(row=2,column=0)
        loginUN.grid(row=1,column=1)
        loginPW.grid(row=2,column=1,pady = 15)
        loginBut.grid(row=3,column=0,columnspan=2)
        back.grid(row= 4,column=4)
    def chklogin(self,cusername,cpassword,controller): # checks login credntials 
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
            mid.error("Looks look that account does not exit, try agin!")
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
                    global authuserinfo
                    authuserinfo = inf            
            #print("\n Login Succesful \n")
            #print("Logged in as", auth_usr,"\n")
            #print("lin109",authuserinfo)
            auth.close() # close username and passwrod file
            auth_usr = AuthUsr(authuserinfo["username"],authuserinfo["first"],authuserinfo["last"],authuserinfo["phone"])
            Lobby(self,controller)
            controller.show_frame(Lobby)
        else:
            mid.error("Wrong password try agin!")
            


class NewUser(StartPage):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="CampRezi New Account",font=LARGE_FONT)
        label.grid(pady=10,padx=10)
        mkaccLabel = tk.Label(self, text = "Let Make you an Account!",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
        mkaccLabel2 = tk.Label(self, text = "Enter your information below",bg = "#333333",fg = "#FFFFFF",font=("Ariel",16))
        newFirstT =  tk.Label(self, text = "First Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14)) #reatig text feilds in wondow 
        newLastT =  tk.Label(self, text = "Last Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        newNumT =  tk.Label(self, text = "Phone Number",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        newUNT = tk.Label(self, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        newPWT = tk.Label(self, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
        newFirst = ttk.Entry(self)
        newLast = ttk.Entry(self)
        newNum = ttk.Entry(self)
        newUN = ttk.Entry(self)
        newPW = ttk.Entry(self, show="*")
    # print(cusername,cpassword)
        loginBut = ttk.Button(self, text = "Login",command=lambda: [mid.createUsr(newFirst.get(),newLast.get(),newNum.get(),newUN.get(),newPW.get()),mid.loby()]) # run the mkuser fucntion with the information entered into the windo on press of this button , then run the loby function 
        back = ttk.Button(self, text = "Back", command=lambda:[controller.show_frame(StartPage)])

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
class Lobby(Login):
    def __init__(self,parent,controller):
        auth_usr = AuthUsr(authuserinfo["username"],authuserinfo["first"],authuserinfo["last"],authuserinfo["phone"])
        print(auth_usr.first)
        tk.Frame.__init__(self,parent)
        labstr = ("Hello     "+auth_usr.first+"!\n\nWelcome to CampRezi,\n Login or Make an account")
        lobLab = tk.Label(self, text =labstr,bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
        lobBut1 = ttk.Button(self, text = "View Available Sites",command=lambda:[controller.show_frame(View)])
        lobBut2 = ttk.Button(self, text = "New Reservation",command=lambda:[controller.show_frame(New)])
        lobBut3 = ttk.Button(self, text = "Cancel Reservation",command= lambda:[controller.show_frame(Cancel)])
        back = ttk.Button(self, text = "Back", command=lambda:[controller.show_frame(Login)])
        lobLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40)
        lobBut1.grid(row = 2, column = 1)
        lobBut2.grid(row = 3, column = 1,pady = 10)
        lobBut3.grid(row = 4, column = 1)
        back.grid(row= 5,column=4)
        
class Cancel(Lobby):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        canT = tk.Label(self,text="You have reserved the following sites:")
        locX = 1
        for key,value in reserved.items():
            x = lambda:[auth_usr.username]
            if value==x: # if the site is reserved under the name of the currently loged in user
                button=tk.Button(self,text=key,command= lambda key=key,value=value:[self.can(key),mid.sucess("Reservation for ",value, "removed.")])
                locX += 1
                button.grid(row=2,column=locX)
        canBack = tk.Button(self,text="back", command=lambda:[controller.show_frame(Lobby)])
        canT.grid(row=0)
        canBack.grid(row=5)
        
    def can(self,deletion):
        print("Cancel Reservation ")
        print(deletion)
        valid = reserved.get(deletion)
        if valid is not None:
            pass
        else:
            mid.error("Please choose an available site")
        if deletion in reserved:
            reserved.pop(deletion) # add reservation to list 
            available.append(deletion) #remove reservatio nfrom avialable 
            with open("reservations.txt","w") as rezis: # writes updated reservations dict to reservations file
                for key,value in reserved.items():
                    rezis.write('%s %s\n' % (key,value))
            print("Reserved Sites:\n" , reserved)
            print("Available Sites:\n" , available)

class View(Lobby):
     def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        viewWinT = tk.Label(self,text="The Following Sites are reserved:")
        viewWinT.grid(row=0)
        viewWinT2 = tk.Label(self, text="These sites are avaible for reservation:")
        viewWinT2.grid(row=4)
        locX = 1
        for key in reserved: #create button for each key in reserved sites
            locX += 1 # increate the button location number by 1 so thye odnt overlap 
            button = tk.Label(self, text=key, bg="#696969", padx=10)
            button.grid(row=2,column=locX)
        locX = 1
        for site in available:
            locX += 1
            button = tk.Label(self, text=site,bg="#696969", padx=10)
            button.grid(row=6,column=locX)
        viewBack = tk.Button(self, text="Back", bg="#696969", command=lambda:[controller.show_frame(Lobby)])
        viewBack.grid(row = 8,column=0)

class New(Lobby):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        rwinNewT = tk.Label(self, text="Choose one of the following sites to reserve: ",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))
        locX = 1
        locY =  1
        for site in available:
            locX += 1
            if locX % 2 ==0:
                button = ttk.Button(self, text=site, command=lambda site=site:[self.reserve(site), mid.sucess((site+" reserved successfully")),controller.show_frame(New)])# site=site ensures each button gets a unique value for site 
                button.grid(row=2,column=locX)
            else:
                locX-=1
                button = ttk.Button(self, text=site, command=lambda site=site:[self.reserve(site), mid.sucess((site+" reserved successfully")),controller.show_frame(New)])# site=site ensures each button gets a unique value for site 
                button.grid(row=3,column=locX)
                locX+=1
            
        #error("This site is not available or des not exist")
        rwinNewT.grid(row = 0, column = 0,columnspan=10,pady = 15)
        rwinBack = ttk.Button(self, text="back",command=lambda:[controller.show_frame(Lobby)])
        rwinBack.grid(row=5)
        
    def reserve(self,site): # reserve will be able to input the day they want to reserve and it will be stored in a dictionary in a file local to the program 
        available.remove(site) # add reservation to list 
        reserved[site]=auth_usr.username #remove reservatio nfrom avialable 
        print("Reserved Sites:\n" , reserved)
        print("Available Sites:\n" , available)
        with open("reservations.txt","a") as rezis: 
            a = reserved[site] 
            rezis.write('%s %s\n' % (site,a))

class AuthUsr:
    def __init__(self,username,first,last,phone):
        self.username = username
        self.first = first
        self.last = last
        self.phone = phone


app= CampReziApp()
app.mainloop()
print("the user is",auth_usr.first)