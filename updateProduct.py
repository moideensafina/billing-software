import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Update_Product():
    def __init__(self):
        self.root = tk.Tk()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        label = tk.Label(self.root, text="Billing Software", font=("Arial", 30, "bold"),bg=self.clr(27, 38, 49), bd=4, relief="groove", fg="white")
        label.pack(side="top", fill="x", ipady=10)
        
        self.backBtn = tk.Button(self.root, text="<--Back",command=self.backFunc,width=18,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.backBtn.pack(anchor="nw",padx=20,pady=10)
        
        
        
        # CREATE PRODUCT FRAME
        createProductFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(27, 38, 49))
        createProductFrame.place(width=self.width/3,height=self.height-230 ,x=self.width/3, y=140)
        
        Labe = tk.Label(createProductFrame, text="UPDATE PRODUCT", font=("Arial", 18, "bold"),bg=self.clr(27, 38, 49), fg="white")
        Labe.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.searchEntry = tk.Entry(createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.searchEntry.grid(row=1, column=0, padx=(20,0),pady=(30,0))
        
        self.searchBtn = tk.Button(createProductFrame, text="Search",command=self.searchFunc,font=("Arial", 15, "bold"), bg="light gray", fg="black")
        self.searchBtn.grid(row=1,column=1,padx=(0,20),pady=(30,0))
        
        nameLbl=tk.Label(createProductFrame, text="Name:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        nameLbl.grid(row=2, column=0, padx=(20,0), pady=40)
        self.name = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.name.grid(row=2, column=1, padx=(0,20), pady=40)
        
        priceLbl=tk.Label(createProductFrame, text="price:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        priceLbl.grid(row=3, column=0, padx=(20,0), pady=20)
        self.price = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.price.grid(row=3, column=1, padx=(0,20), pady=20)
    
        
        quantityLbl=tk.Label(createProductFrame, text="Quantity:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        quantityLbl.grid(row=4, column=0, padx=(20,0), pady=20)
        self.quantity = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.quantity.grid(row=4, column=1, padx=(0,20), pady=20)
        
        unitLbl = tk.Label(createProductFrame, text="Unit", font=("Arial", 16,"bold"), bg=self.clr(27, 38, 49), fg="white")
        unitLbl.grid(row=5, column=0,padx=(20,0), pady=30)
        
        self.options = ttk.Combobox(createProductFrame, font=("Arial", 14,"bold" ),values=("Pcs", "Kg"),state="readonly")
        self.options.set("Select One")
        self.options.grid(row=5,column=1,padx=(0,20), pady=30)
        
        self.createBtn = tk.Button(createProductFrame, text="Update",command=self.updateFunc, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.createBtn.grid(row=6,columnspan=2, column=0, padx=(20), pady=10)

        self.deleteBtn = tk.Button(createProductFrame, text="Delete",command=self.deleteFunc, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="red",relief="raised", bd=2)
        self.deleteBtn.grid(row=7,columnspan=2, column=0, padx=(20), pady=10)
        
        
        self.root.mainloop()
        # tk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=20)
    
    def searchFunc(self):
        id = int(self.searchEntry.get())
        if id:
            self.dbFun()
            self.cur.execute("select * from products where id=%s",(id))
            data = self.cur.fetchone()
            print(data)
            if data:
                nam=data[1]
                pri=data[2]
                quan=data[3]
                uni=data[4]
                self.name.insert(0,nam)
                self.price.insert(0,pri)
                self.quantity.insert(0,quan)
                self.options.insert(0,uni)
            else:
                messagebox.showinfo("Error","pls enter product Id")  
        else:
            messagebox.showinfo("Error","pls enter product Id!")
    
    def updateFunc(self):
        id = int(self.searchEntry.get())
        name = self.name.get()
        price = int(self.price.get())
        quantity = int(self.quantity.get())                
        uni =self.options.get()
        if id and name and price and quantity and uni:
            if uni!="Select One":
                self.dbFun()
                self.cur.execute("update products set name=%s,price=%s,quantity=%s,unit=%s where id=%s" ,(name,price,quantity,uni,id))
                self.con.commit()
                
                tk.messagebox.showinfo("Success","Product Updated!")
                self.root.destroy()
                
                self.name.delete(0,tk.END)
                self.price.delete(0,tk.END)
                self.quantity.delete(0,tk.END)
                self.options.delete(0,tk.END)
                
            else:
                tk.messagebox.showinfo("Error","Select Unit Field!")
                self.root.destroy()
        else:
            tk.messagebox.showinfo("Error","pls enter product Id!")
            self.root.destroy()
            
    def deleteFunc(self):
        id= int(self.searchEntry.get())
        if id:
            try:
                self.dbFun()
                self.cur.execute("delete from products where id=%s",(id))
                self.con.commit()
                
                tk.messagebox.showinfo("Success","Deleted Successfully!")
                self.root.destroy()
                
            except Exception as e:
                tk.messagebox.showinfo("Error",f"Error - {e}")
                self.root.destroy()
        else:
            tk.messagebox.showinfo("Error","pls enter product Id!")
            self.root.destroy()
            
    def dbFun(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="S@fi830068",database="billing_software")
        self.cur = self.con.cursor()
        
        
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def backFunc(self): 
        self.root.destroy()
    