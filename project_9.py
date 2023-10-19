#/usr/bin/env python3
# Jacob Foppes Week 9 - OOP Subclasses

import time
import random     
import os  
from pathlib import Path
import sys
import csv
import shutil
'''Intro: Welocme to the game baisic tutorial.
    Choose your name '''
    
# GLOBAL VARIABLES 
savedGames = [] #list of all saved games 
auth_usr = ""
save = "" # users current location in the game  game
owd = os.getcwd()
wokeDex = [] #authenitcated users wokedex 
currentLevel = 0

with open("accounts.txt","r+") as users:
    games = users.read()
    savedGames = games.split("\n")

allwokemon = []# list of wokemon-----each poekemon is a list of the pokemon features 
  
with open("wokemon.csv","r") as allWok:
    reader = csv.DictReader(allWok)
    for i in reader: # create a list of dictionaires with atrributes of wokemon 
        allwokemon.append(i)
            
 
basicWokemon = []
electricWokemon = []
waterWokemon = []
fireWokemon = []
earthWokemon = []  
        

class Wokemon:
    def __init__(self):
        randomwokemon= random.choice(allwokemon)
        for key,value in randomwokemon.items():
            setattr(self,key,value) # for each key value pair in the random pokemon dictionary crete an attriburte (ie name,hp ,type)
        self.getHP(self.hp) # call the get HP function when an instace of this class is creates 
        self.effectiveness1(self.att1dammage)
        self.effectiveness2(self.att2dammage)
        self.hp = int(self.hp)  
    def getHP(self,hp): # this fucntion will Determin  a random hp number for wild wokemon witin 5 points of the default HP 
        self.hp = random.randrange((int(hp)-4),(int(hp)+5))
    def effectiveness1(self,att1dammage): # this will ranomize effectiveness of the wokmons attack
        self.att1dammage = random.randrange((int(att1dammage)-2),(int(att1dammage)+2))
    def effectiveness2(self,att2dammage): # this will ranomize effectiveness of the wokmons attack
        self.att2dammage = random.randrange((int(att2dammage)-2),(int(att2dammage)+2))
        
class PlayerWokemon:
    def __init__(self):
        self.choice = self.getWoke() # calls the function where player choses thier wokemon 
        for key,value in self.choice[0].items(): # self.choice is a tuple of the wokemon dictionary, and the index of said dictinary in the wokeDex list. this selcts the dict
            setattr(self,key,value)# extracts dicationary key value pairs and creates attributes for the object  
        self.hp = int(self.hp)  
    def getWoke(self):
        global breaker
        breaker = True
        while breaker == True:
            choice = input("\nChoose your Wokemon:\n"+str(wokeDex)+"\n")
            for i in wokeDex: # iterate thru each dictionary i nthe wokedex list 
                for p in i.items(): #iterate thru tuples of items in each wokemon dictionary, within the list of wokemon ex: ("Name","Wikachu")
                    if p[1] == choice: #if an entry in the dict matches the playerys choice:
                        self.choice = i #sets player pokemon object for battle 
                        self.wokloc = wokeDex.index(i) #creates varibale for index of selected woekmon within the woedex list 
                        breaker = False
                        return self.choice,self.wokloc # returns dictionary of player choice and location of said choice within the list of pokemon. these are reutned as tuple
                    else:
                        print("Please choose a Wokemon from your Wokedex")
                        break

def print_slow(str):# Credit : Sebastian - Stack overflow https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0005)
def input_slow(str): # Credit: https://www.101computing.net/python-typing-text-effect/
  for character in str:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0005)
  value = input()  
  return value  
def battle(randWokemon,pWokemon):# take the pokemon generated orivouse and perfom a battle 
    while True:
        print("\nYou chose :",pWokemon.Name,"\n")
        print_slow("\nYour HP: " + str(pWokemon.hp) + "\n") #print player helath 
        print_slow("Oponent HP: " + str(randWokemon.hp) + "\n")# print oponent helath 
        print_slow("\nLooks like its " + pWokemon.Name + " vs " + randWokemon.Name + "\n")
        time.sleep(1)
        def attack():
            phit1 = random.randrange(0,5,1)#randomly genreated player dammage to compouter 
            randWokemon.hp = int(randWokemon.hp)
            randWokemon.hp -= phit1 #subtract hit points form health 
            print_slow(pWokemon.Name + " Strikes!\nIt does " + str(phit1) + " dammage!\n\n")
            chit1 = random.randrange(0,5,1)#randomly genereated compouter dammage to play
            pWokemon.hp -= chit1#subtract hit points form health 
            print_slow(randWokemon.Name + " Strikes!\nIt does " + str(chit1) + " dammage!\n\n")
            print_slow("Oponent HP: " + str(randWokemon.hp) + "\n")
            print_slow("Your HP: " + str(pWokemon.hp) + "\n\n")
        attack()
    
            
        while pWokemon.hp > 0 and randWokemon.hp > 0: # while both players health greate than 0 comntinue the attack function 
            attack()
        if pWokemon.hp <= 0 and  pWokemon.hp <= randWokemon.hp: #if comoputer wins
            print_slow("Dang..., Thats tough boss. \nLooks like you lost this one.\nTime to head home and heal your Wokemon\n ")
            loby()
        elif randWokemon.hp <= 0 and pWokemon.hp >= randWokemon.hp: # if player wins
            global currentLevel
            currentLevel += 1
            print_slow("You won!!\nYou now have " + randWokemon.Name + " added to your wokedex!!\nYou will now move on to "+ str(currentLevel)+"!\n\n")
            capture = randWokemon.__dict__
            capture["hp"] = capture["defhp"] # reset wokemon HP 
            wokeDex.append(capture)
            saveg()
            loby()
            False
        
def l1():#game level 1
    print_slow("Welcome to level 1!\n")
    while True:
        path1 = input_slow("You are wlaking down the street and you encounter a set a of 2 trail heads:\n 'Elk Road', and 'Spoon Drive' which do you take \n Enter 'Elk' or 'Spoon'\n").lower()
        if path1 == "elk":
            print_slow("Your walking down the elk path when you spot something in the bushes...\n")
            time.sleep(.75)
            print_slow(".")
            time.sleep(.75)
            print_slow(".")
            time.sleep(.75)
            print_slow(".")
            randWokemon =  Wokemon()#create random wokemon object 
            rwok = randWokemon.Name # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or 'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    break 
                elif fight1 == "battle":
                    pWokemon = PlayerWokemon()
                    battle(randWokemon,pWokemon)
                else:
                    print_slow("Please choose run or battle\n")
                    continue
                
        elif path1 == "spoon":
            print_slow("\nYour walking down the Spoon Path and you come to a fork in the path\n The left looks like it leads to a river, and the right looks to be more forrest.\n ")
            while True:
                lefRig = input_slow("Do you Turn left or right\n").lower()
                if lefRig == "left":
                    print_slow("\nWhile Crossing the shallow end of the river, you see some splashing...")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    print_slow(".")
                    randWokemon = Wokemon()#create random wokemon object 
                    rwok = randWokemon.Name # extract just the name 
                    fight2 = input_slow("\n\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or 'Run'\n").lower()
                    if fight2 == "battle":
                        pWokemon = PlayerWokemon()
                        battle(randWokemon,pWokemon)
                    elif fight2 == "run":
                        print_slow("You got away just in time, better head back to that fork in the path...\n\n")
                        continue
                    else:
                        print_slow("Choose battle, or Run.\n")
                elif lefRig == "right":
                    print_slow("Your take a right on Spoon Path when you spot something in the bushes...\n")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    print_slow(".")
                    time.sleep(.75)
                    randWokemon = Wokemon()#create random wokemon objkect 
                    rwok = randWokemon.Name # extract just the name 
                    fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                    if fight1 == "run":
                        print_slow("You got away just in time! Better head back to that fork in the path.\n\n")
                        time.sleep(2)
                        continue 
                    elif fight1 == "battle":
                        pWokemon = PlayerWokemon()
                        battle(randWokemon,pWokemon)# run battle with the random workmon objec tand th player wokemon object 
                    else: 
                        print_slow("Choose battle, or Run.\n")
                else:
                    print_slow("Please choose left or right\n")
                    continue
                

def l2():#game level 2
    print_slow("Welcome to Level 2!\n\n")
    print_slow("You have entered a new area now...\n")
    time.sleep(.25)
    print_slow("You see new kinds of terrain ready to explore!\n")
    time.sleep(.25)
    while True:
        print_slow("To your left you see a massive volcano, and to your right you see a vast rocky desert.\n")
        time.sleep(.15)
        path3 = input_slow("Do you visit the desert or the volcano?\nsay 'Desert', or 'Volcano'\n").lower()
        if path3 == "desert":
            print_slow("You begin to wander the desert.\nThe Sun is beating down on you\n")
            time.sleep(.5)
            print_slow("You see something in the distance....\n")
            time.sleep(.5)
            print_slow("You walk closer......\n")
            time.sleep(.75)
            randWokemon = Wokemon()#create random wokemon objkect 
            rwok = randWokemon.Name # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    continue 
                elif fight1 == "battle":
                    pWokemon = PlayerWokemon()
                    battle(randWokemon,pWokemon)
                else: 
                    print_slow("Choose battle, or Run.\n")
        elif path3 == "volcano":
            print_slow("You start walking towards the volcano.\n")
            time.sleep(.75)
            print_slow("Suddenly a creature rushes twords you!")
            randWokemon = Wokemon()#create random wokemon objkect 
            rwok = randWokemon.Name # extract just the name 
            while True:
                fight1 = input_slow("\nA wild " + rwok + " appears!!\n Do you battle? or Run away?\n Enter 'Battle', or n'Run\n").lower()
                if fight1 == "run":
                    print_slow("You got away just in time! Better head back.\n\n")
                    time.sleep(2)
                    continue 
                elif fight1 == "battle":
                    pWokemon = PlayerWokemon()
                    battle(randWokemon,pWokemon)
                else: 
                    print_slow("Choose battle, or Run.\n")
        else:
            print_slow("Please choose desert, or volcano.\n")
            continue
def l3(): #Game level 3
    print("Level 3 Comming Soon!")
    time.sleep(3)
    pass
levels = {1:l1,2:l2,3:l3}

def loby():# lobby is where the player once logged in, can either view thier Wokedex, or continue playing at the start of thier current  level 
    global wokeDex
    global currentLevel
    lvl = open("saveG.txt","r")
    currentLevel = int(lvl.read())
    while True:
        lchoice = input("Hello "+auth_usr+" Welcome to the lobby!\n Your Currently at Level: " + str(currentLevel) + "\nSay 'start' to resume your game, 'view' to view your wokedex, 'Prev' to redo a previos level, or 'Exit' to retun to the main screen."+"\n").lower()
        if lchoice == "start":
            level = open("saveG.txt","r").read()# save game file
            level = int(level)
            if level >=3:
                print("No more levels Yet! You  can still visit previous levels\n")
                time.sleep(1)
                continue
            levels[level]()# read savegame file and call level finciton based on the text in the file. this text is used as a key in a dictionary of all levels where the values are the fucntions that start the levels 
        elif lchoice == "prev":
            if currentLevel == 1:
                print_slow("\nYou have not completed any levels yet!. Come back here after you have progressed.\n")
                time.sleep(1)
                continue
            elif currentLevel == 2:
                try:
                    lev = int(input("You can Visit the Following Levels:\nLevel 1, Level 2\nType the number of the level you want to visit\n"))
                    if lev > currentLevel:
                        print("You can not access this yet.")
                    else:
                        levels[lev]()
                except ValueError:
                    print("Level does not exist.\n")
                    continue
            elif currentLevel == 3:
                try:
                    lev = int(input("You can Visit the Following Levels:\nLevel 1, Level 2, Level 3\nType the number of the level you want to visit\n"))
                    if lev > currentLevel:
                        print("You can not access this yet.\n\n")
                    else:
                        levels[lev]()
                except ValueError:
                    print("Level does not exist.\n")
                    continue
            
        elif lchoice == "view":
            print("\n"+str(wokeDex)+"\n")
            time.sleep(1)
        elif lchoice == "exit":#exit loby and return to welocme/ main directory
            os.chdir(owd)
            wokeDex = {}
            currentLevel = 0
            welcome()
        else:
            print("Select a valid choice\n")
            time.sleep(.5)

def mkuser(): # if the user does not have an account they can make one
    breaker = True
    while breaker ==True:
        print_slow("Prof. Woke: Wecome to WokeyWorld!\n")
        pname = input("What shall I call you?\n")   
        if pname in savedGames or os.path.exists(pname+"/"):
            print("User already exists. Try again ")
            continue
        else:
            global auth_usr
            global wokeDex
            auth_usr = pname
            savedGames.append(pname) # ad new name to the saved games list 
            auth = open("accounts.txt","r+") 
            auth.write("\n".join(str(line) for line in savedGames))# write easch line of the saved gmaes list  to the accouts file
            auth.close()
            os.chdir("savedGames") # changes dir to the users folder so that a new game can be saved
            p = Path(pname)
            os.mkdir(p) # make player directory 
            default= "defaultWokedex.csv"
            shutil.copy2(default,str(p)+"/wokedex.csv") # copy defualt wokedex to player directory 
            os.chdir(pname) # enter player direcotry 
            sav = open("saveG.txt", "x") # create save file
            os.chdir(owd)
            print("Account creation sucessfull. Logged in as:", pname,"\n")
            breaker == False 
            newGame()
            break
def saveg():## this fuction can be called to save the game durring play by typing save 
    keys = wokeDex[0] 
    with open("wokedex.csv","w",newline="") as dex: #open player wokedex file 
        writer = csv.DictWriter(dex,keys) 
        writer.writeheader()
        writer.writerows(wokeDex)
        dex.close()
    lvl = open("saveG.txt","w")
    lvl.write(str(currentLevel))
    lvl.close()
    print("Game Saved. Your currnet level: "+str(currentLevel))
            
def newGame():# First Sequence in game after user amkes account
    global wokeDex
    wokeDex = []
    os.chdir("savedGames/" + auth_usr)
    with open("wokedex.csv","r") as dex:
        reader = csv.DictReader(dex)
        for i in reader: # create a list of dictionaires with atrributes of wokemon 
            wokeDex.append(i)
    time.sleep(.25)
    print_slow("\nProf Woke: Hello "+auth_usr+" My Name is Professor Woke! Ill show you arround\n")
    time.sleep(.1)
    print_slow("Prof Woke: Im giving you a wokedex.\n")
    time.sleep(.1)
    print_slow("Prof Woke: This is where you will store the wokemon you catch along the way.\n")
    time.sleep(.1)
    print_slow("Prof Woke: I going to start you off with this Wikachu.\n")
    print("\n",auth_usr,"'s Wokedex:",wokeDex,"\n")
    time.sleep(1)
    global currentLevel
    currentLevel = 1
    saveg()
    loby()
    pass

def welcome():# where user logs in to contine or creates new game
    while True:
        print("\n\nWokemon Gotta Snatch em' all!")
        game = input("To start a new game, say 'New', to continue a game, enter 'cont'\n").lower()
        if game == "new":
            mkuser()
        elif game == "cont":
            while True:
                print("Available saved Games:",savedGames,"\n")
                un = input("Enter your username or type 'Exit to return to main menue\n")
                if un == "exit":
                    welcome()
                    break
                elif un not in savedGames:
                    print("\n User not found. Try agian. OR Type Exit to return to the main screen \n")
                    time.sleep(1)
                elif un in savedGames: #checks username agains list of saved games
                    global auth_usr
                    auth_usr = un
                    global wokeDex
                    wokeDex= []
                    os.chdir("savedGames/")
                    os.chdir(auth_usr)
                    with open("wokeDex.csv","r") as dex:
                        reader = csv.DictReader(dex)
                        for i in reader: # create a list of dictionaires with atrributes of wokemon 
                            wokeDex.append(i)
                
                    print("\n Found Your Game!\n")
                    
                    print(" Lets Get to it ", auth_usr,"\n")
                    loby()
                    break
        else: print("Please select a valid choice")
welcome()            