import tkinter as tk
from tkinter import ttk
auth_Usr = "jake"

class MainWindow(tk.Tk):
    
    def __init__(self):
        super().__init__() # tk.tk is ther superclass bing called by super()
        self.username = auth_Usr
        frame_main = ttk.Frame(self)
        frame_main.pack(fill= tk.BOTH, expand=True)
        btn_show_Authuser = ttk.Button(frame_main,
                                       text="Show Username",
                                       command=self.show_cred) 
        btn_show_Authuser.pack(padx=10, pady=10)
        
    def show_cred(self):
        username_window = LoginWindow(self,username=self.username)

class  LoginWindow(tk.Toplevel): #creating class for toplevel tk widgets 
    def __init__(self,master,username): #
        super().__init__(master)#initializes top level widget ---tk.toplevel is the super class bein g clle by super ----- passes master to the toplevel superclasss  
        self.username = username
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH,expand = True)
        un_lbl = ttk.Label(self.frame_main,
                           text=("My name is: ", self.username))
        un_lbl.pack(padx=50,pady=50)
        
        
if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
    
