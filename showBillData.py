import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Show_Bill_Data():
    def __init__(self):
        self.root = tk.Tk()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        label = tk.Label(self.root, text="Billing Software", font=("Arial", 30, "bold"),bg=self.clr(27, 38, 49), bd=4, relief="groove", fg="white")
        label.pack(side="top", fill="x", ipady=10)
        
        self.backBtn = tk.Button(self.root, text="<--Back",command=self.backFunc,width=18,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.backBtn.pack(anchor="nw",padx=20,pady=10)

        
        
        #Table frame 
        #details frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(160, 240, 200))
        self.detFrame.place(width=self.width-200,height=self.height-250 ,x=100, y=150)
        
        lbl=tk.Label(self.detFrame, text="Create Product Details", font=("Arial", 16, "bold"), bg=self.clr(27, 38, 49), pady=10,fg="white")
        lbl.grid(row=0,column=0,padx=40,ipadx=20, pady=8)
        
        self.options = ttk.Combobox(self.detFrame, font=("Arial", 16,"bold" ),values=("Show All","Lowest Amount", "Highest Amount"),state="readonly")
        self.options.set("Filter")
        self.options.grid(row=0,column=1,padx=20, pady=8)
        
        srchBtn = tk.Button(self.detFrame, text="Search",command=self.filterProduct,font=("Arial", 16,"bold"), bg=self.clr(27, 38, 49),fg="white")
        srchBtn.grid(row=0, column=2, pady=8)
        
    
        self.tabFun()  
        
        self.showPro()
        self.root.mainloop()
        
        # tk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=20)
    
    def filterProduct(self):
        opt = self.options.get()
        if opt=="Show All":
            self.tabFun()
            self.table.delete(*self.table.get_children())  
            self.dbFun()
            self.cur.execute("SELECT id, customerId, customerName, totalAmount, products, quantities, productNames FROM billData")
            data = self.cur.fetchall()
            for i in data:
                self.table.insert('',tk.END,values=i)  
        
            self.con.close()
        elif opt=="Lowest Amount":
            self.tabFun()
            self.table.delete(*self.table.get_children())  
            self.dbFun()
            self.cur.execute("SELECT id, customerId, customerName, totalAmount, products, quantities, productNames FROM billData order by totalAmount")
            data = self.cur.fetchall()
            for i in data:
                self.table.insert('',tk.END,values=i)    
        
            self.con.close()
        elif opt=="Highest Amount":
            self.tabFun()
            self.table.delete(*self.table.get_children())  
            self.dbFun()
            self.cur.execute("SELECT id, customerId, customerName, totalAmount, products, quantities, productNames FROM billData order by totalAmount desc")
            data = self.cur.fetchall()
            for i in data:
                self.table.insert('',tk.END,values=i)    
        
            self.con.close()
        else:
            pass
    
    
    def showPro(self):
        self.dbFun()
        self.cur.execute("SELECT id, customerId, customerName, totalAmount, products, quantities, productNames FROM billData")
        data = self.cur.fetchall()
        for i in data:
            self.table.insert('',tk.END,values=i)    
        
        self.con.close()
        
    
    def tabFun(self):
        
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14))              # Table content font
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))  # Header font
        

        
        tabFrame = tk.Frame(self.detFrame, bd=5, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width-240, height=self.height-340, x=7, y=70)
        
        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
        
        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set,columns=("id", "cid", "cname","tamount","pids","pnames","quant"))	
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        
        
        
        self.table.heading("id", text="BILL ID")
        self.table.heading("cid", text="CustomerId")
        self.table.heading("cname", text="Customer NAME")
        self.table.heading("tamount", text="Amount")
        self.table.heading("pids", text="Product ID")
        self.table.heading("pnames", text="Product NAME")
        self.table.heading("quant", text="Quantity")
        self.table["show"] = "headings"
        self.table.column("id", width=50, anchor="center")
        self.table.column("cid", width=50, anchor="center")
        self.table.column("cname", width=100, anchor="w")
        self.table.column("tamount", width=50, anchor="center")
        self.table.column("pids", width=250, anchor="w")
        self.table.column("pnames", width=300, anchor="w")
        self.table.column("quant", width=50, anchor="center")


        self.table.pack(fill="both", expand=True)
        
        
    def dbFun(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="S@fi830068",database="billing_software")
        self.cur = self.con.cursor()
        
        
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def backFunc(self):
        self.root.destroy()