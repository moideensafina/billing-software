import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Create_Product():
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
        createProductFrame.place(width=self.width/3,height=self.height-220 ,x=70, y=140)
        
        Labe = tk.Label(createProductFrame, text="CREATE PRODUCT", font=("Arial", 18, "bold"),bg=self.clr(27, 38, 49), fg="white")
        Labe.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        nameLbl=tk.Label(createProductFrame, text="Name:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        nameLbl.grid(row=1, column=0, padx=20, pady=40)
        self.name = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.name.grid(row=1, column=1, padx=20, pady=40)
        
        priceLbl=tk.Label(createProductFrame, text="price:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        priceLbl.grid(row=2, column=0, padx=20, pady=20)
        self.price = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.price.grid(row=2, column=1, padx=20, pady=20)
        
        
        quantityLbl=tk.Label(createProductFrame, text="Quantity:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        quantityLbl.grid(row=3, column=0, padx=20, pady=20)
        self.quantity = tk.Entry(createProductFrame, font=("Arial", 15, "bold"), bd=2)
        self.quantity.grid(row=3, column=1, padx=20, pady=20)
        
        unitLbl = tk.Label(createProductFrame, text="Unit", font=("Arial", 16,"bold"), bg=self.clr(27, 38, 49), fg="white")
        unitLbl.grid(row=4, column=0,padx=20, pady=30)
        
        self.options = ttk.Combobox(createProductFrame, font=("Arial", 16,"bold" ),values=("Pcs", "Kg"),state="readonly")
        self.options.set("Select One")
        self.options.grid(row=4,column=1,padx=20, pady=30)
        
        self.createBtn = tk.Button(createProductFrame, text="Create", command=self.createProduct, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.createBtn.grid(row=5,columnspan=2, column=1, padx=10, pady=10)
    
    
        #Table frame 
        #details frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(160, 240, 200))
        self.detFrame.place(width=self.width/2,height=self.height-220 ,x=self.width/3+140, y=100)
        
        lbl=tk.Label(self.detFrame, text="Create Product Details", font=("Arial", 16, "bold"), bg=self.clr(27, 38, 49), pady=10,fg="white")
        lbl.pack(side="top", fill="x")   
        self.tabFun()  
        
        
        self.root.mainloop()
        
        # tk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=20)
    
    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=5, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/2-40, height=self.height-310, x=17, y=70)
        
        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
        
        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set,columns=("id", "name", "pri","quan","uni"))	
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        
        self.table.heading("id", text="Product_ID")
        self.table.heading("name", text="NAME")
        self.table.heading("pri", text="PRICE")
        self.table.heading("quan", text="QUANTITY")
        self.table.heading("uni", text="UNIT")
        self.table["show"] = "headings"
        
        self.table.pack(fill="both", expand=1)
        
        
    def createProduct(self):
        productName = self.name.get()
        productPrice = int(self.price.get())
        productQuantity = int(self.quantity.get())
        productUnit = self.options.get()
        
        if productName and productPrice and productQuantity and productUnit:
            try:
                self.dbFun()
                self.cur.execute("insert into products (name,price,quantity,unit) values (%s,%s,%s,%s)",(productName,productPrice,productQuantity,productUnit))
                self.con.commit()
                    
                self.tabFun()
                self.table.delete(*self.table.get_children())    
                self.cur.execute("select * from products where name=%s",(productName))
                data = self.cur.fetchone()
                self.table.insert('',tk.END,values=data)
                self.con.close()
                
                self.name.delete(0,tk.END)
                self.price.delete(0,tk.END)
                self.quantity.delete(0,tk.END)
                self.options.delete(0,tk.END)
                
                
            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")
        else:
            tk.messagebox.showerror("Error", "All fields are required")
    
    def dbFun(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="S@fi830068",database="billing_software")
        self.cur = self.con.cursor()
        
        
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def backFunc(self):
        self.root.destroy()