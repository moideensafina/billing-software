import tkinter as tk
from tkinter import messagebox
from menu import MenuPage  
import pymysql

class home():
    def __init__(self, root):
        self.root = root
        self.root.title("Admin LogIn")
        self.root.config(bg=self.clr(174, 182, 191))
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        label = tk.Label(self.root, text="Billing Software", font=("Arial", 30, "bold"),
                         bg=self.clr(27, 38, 49), bd=4, relief="groove", fg="white")
        label.pack(side="top", fill="x", ipady=10)
        
        # Login Frame
        LogInFrame = tk.Frame(self.root, bg=self.clr(27, 38, 49), bd=4, relief="ridge")
        LogInFrame.place(width=self.width / 3, height=self.height - 350, x=self.width / 3, y=170)
        
        Labe = tk.Label(LogInFrame, text="ADMIN LOGIN", font=("Arial", 18, "bold"),
                        bg=self.clr(27, 38, 49), fg="white")
        Labe.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        nameLbl = tk.Label(LogInFrame, text="UserName", font=("Arial", 16, "bold"), padx=30,
                           bg=self.clr(27, 38, 49), fg="white")
        nameLbl.grid(row=1, column=0, padx=15, pady=30)
        self.nameIn = tk.Entry(LogInFrame, font=("Arial", 16, "bold"), bd=2, width=18, bg=self.clr(174, 182, 191))
        self.nameIn.grid(row=1, column=1, padx=15, pady=30)
        
        passLbl = tk.Label(LogInFrame, text="Password", font=("Arial", 16, "bold"), padx=30,
                           bg=self.clr(27, 38, 49), fg="white")
        passLbl.grid(row=2, column=0, padx=15, pady=15)
        self.passIn = tk.Entry(LogInFrame, font=("Arial", 16, "bold"), width=18, bg=self.clr(174, 182, 191))
        self.passIn.grid(row=2, column=1, padx=15, pady=15)
        
        logBtn = tk.Button(LogInFrame, text="Register", width=18, font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black",command=self.logIn)
        logBtn.grid(row=3, column=0, columnspan=2, pady=30)

    def logIn(self):
        name = self.nameIn.get()
        password = self.passIn.get()
        if name and password:
        #if True:
            try:
                self.dbFun()
                self.cur.execute("select name from login where name=%s and password=%s",(name,password))
                username = self.cur.fetchone()
                if name == username[0]:
                #if True:
                    self.go_to_menu()
                else:
                    tk.messagebox.showError("Error","Enter valid username and Password") 
                
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showError("Error","Please enter userName and password")
        
    def go_to_menu(self):
        self.root.destroy() 
        MenuPage()             

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def dbFun(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="S@fi830068",database="billing_software")
        self.cur = self.con.cursor()

# Run the home window
if __name__ == "__main__":
    root = tk.Tk()
    onj = home(root)
    root.mainloop()
