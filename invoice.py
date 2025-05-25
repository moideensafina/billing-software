import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import platform

class Product_billing():
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
        self.createProductFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(27, 38, 49))
        self.createProductFrame.place(width=self.width/2+50,height=self.height-230 ,x=10, y=140)
        
        self.totalBtn = tk.Label(self.createProductFrame, width=28, font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white",)
        self.totalBtn.grid(row=6, column=2, columnspan=3, padx=(20), pady=10)
        

        
        productIdSearchLbl=tk.Label(self.createProductFrame, text="ProductId:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        productIdSearchLbl.grid(row=0, column=0,padx=(10,0),pady=(40,35))
        self.productIdSearchEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.productIdSearchEntry.grid(row=0, column=1,pady=(40,35))
        self.productIdSearchBtn = tk.Button(self.createProductFrame, text="Search",command=self.searchFunc,font=("Arial", 15, "bold"), bg="light gray", fg="black")
        self.productIdSearchBtn.grid(row=0,column=2,pady=(40,35))
        
        customerIdLbl=tk.Label(self.createProductFrame, text="CustomerId:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        customerIdLbl.grid(row=1, column=0,padx=(10,0),pady=(20,0))
        self.customerIdEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.customerIdEntry.grid(row=1, column=1,pady=(20,0))
        
        customerNameLbl=tk.Label(self.createProductFrame, text="CustomerName:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        customerNameLbl.grid(row=1, column=2,padx=(10,0),pady=(20,0))
        self.customerNameEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.customerNameEntry.grid(row=1, column=3,pady=(20,0))
        
        
        productNameLbl=tk.Label(self.createProductFrame, text="ProductName:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        productNameLbl.grid(row=2, column=0,padx=(10,0),pady=(60,0))
        self.productNameEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.productNameEntry.grid(row=2, column=1,pady=(60,0))
        
        productPriceLbl=tk.Label(self.createProductFrame, text="ProductPrice:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        productPriceLbl.grid(row=2, column=2,padx=(10,0),pady=(60,0))
        self.productPriceEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.productPriceEntry.grid(row=2, column=3,pady=(60,0))
        
        
        productQuantityLbl=tk.Label(self.createProductFrame, text="Enter Number Of Quantity:", font=("Arial", 15, "bold"), bg=self.clr(27, 38, 49), fg="white")
        productQuantityLbl.grid(row=3, column=0,columnspan=2,padx=(40,0),pady=(30,0))
        self.productQuantityEntry = tk.Entry(self.createProductFrame,width=19, font=("Arial", 15, "bold"))
        self.productQuantityEntry.grid(row=3, column=2,pady=(30,0))
        
        self.addItemBtn = tk.Button(self.createProductFrame, text="Add Item",command=self.addItemFunc, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.addItemBtn.grid(row=4,columnspan=2, column=2, padx=(20), pady=30)

        self.clearBtn = tk.Button(self.createProductFrame, text="Clear All",command=self.clearAllFunc, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="black",relief="raised", bd=2)
        self.clearBtn.grid(row=4,columnspan=2, column=0, padx=(20), pady=30)
        
        self.billBtn = tk.Button(self.createProductFrame, text="Bill",command=self.billFunc, width=23,font=("Arial", 15, "bold"), bg="light gray", fg="red",relief="raised", bd=2)
        self.billBtn.grid(row=5,columnspan=2, column=2, padx=(20), pady=30)
        
        
        
         
        #Table frame 
        #details frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(160, 240, 200))
        self.detFrame.place(width=self.width/3+100,height=self.height-230 ,x=self.width/2+120, y=140)
        
        lbl=tk.Label(self.detFrame, text="Added Product Details", font=("Arial", 16, "bold"), bg=self.clr(27, 38, 49), pady=10,fg="white")
        lbl.pack(side="top", fill="x")  
        
        self.tabFun()
        
        self.root.mainloop()
        # tk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=20)
    
    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=5, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/3+100, height=self.height-300, x=5, y=60)
        
        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
        
        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set,columns=("pid", "cid", "cname","pname","pprice","cquantity","ctotal"))	
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        
        self.table.heading("pid", text="Product_ID")
        self.table.heading("cid", text="Customer_Id")
        self.table.heading("cname", text="Customer_Name")
        self.table.heading("pname", text="Product_Name")
        self.table.heading("pprice", text="Price")
        self.table.heading("cquantity", text="Quantity")
        self.table.heading("ctotal", text="Total")
        self.table["show"] = "headings"
        
        self.table.pack(fill="both", expand=1)
   
    
    
    def searchFunc(self):
        id = int(self.productIdSearchEntry.get())
        if id:
            self.dbFun()
            self.cur.execute("select * from products where id=%s",(id))
            data = self.cur.fetchone()
            if data:
                self.productNameEntry.delete(0,tk.END)
                self.productPriceEntry.delete(0,tk.END)
                self.productQuantityEntry.delete(0,tk.END)
                productName=data[1]
                productPrice=data[2]
                self.productNameEntry.insert(0,productName)
                self.productPriceEntry.insert(0,productPrice)
                self.productQuantityEntry.insert(0,1)
            else:
                messagebox.showinfo("Error","pls valid product Id")
                self.root.destroy()
        else:
            messagebox.showinfo("Error","pls  product Id!")
            self.root.destroy()
    
    def addItemFunc(self):
        productId = int(self.productIdSearchEntry.get())
        customerId= int(self.customerIdEntry.get())
        customerName=self.customerNameEntry.get()
        productQuantity= int(self.productQuantityEntry.get())
        if productId and customerId and customerName and productQuantity:
            self.dbFun()
            self.cur.execute("insert into billing (productId,customerId,customerName,quantity,total) values (%s,%s,%s,%s,%s)",(productId,customerId,customerName,productQuantity,0))
            self.con.commit()
            
            
            self.cur.execute("select price from products where id=%s",(productId))
            price=self.cur.fetchone()
            priceData = price[0]
            totalPrice =priceData*productQuantity
            
            self.cur.execute("update billing set total=%s where productId=%s",(totalPrice,productId)) 
            self.con.commit()
            
            self.cur.execute("select quantity from products where id=%s",(productId))
            data = self.cur.fetchone()
            Qdata = data[0]
            updateQuantity = Qdata-productQuantity
            self.cur.execute("update products set quantity=%s where id=%s",(updateQuantity,productId))
            self.con.commit()
            
            self.tabFun()
            self.table.delete(*self.table.get_children())    
            self.cur.execute("select b.productId,b.customerId,b.customerName,p.name,p.price,b.quantity,b.total from billing as b inner join products as p on b.productId=p.id where customerId=%s;",(customerId))
            addData= self.cur.fetchall()
            for i in addData:
                self.table.insert('',tk.END,values=i)
                
            self.cur.execute("select sum(total) from billing where customerId=%s",(customerId))
            totalPri=self.cur.fetchone()
            print(totalPri)
            print(totalPri[0])
            self.totalBtn.config(text=f"Total Amount: Rs.{totalPri[0]}/-")
            
        else:
            messagebox.showerror("Error","pls enter all fields!")
            self.root.destroy()
    def billFunc(self):
        productId = int(self.productIdSearchEntry.get())
        customerId= int(self.customerIdEntry.get())
        customerName=self.customerNameEntry.get()
        productQuantity= int(self.productQuantityEntry.get())
        if productId and customerId and customerName and productQuantity:
            self.dbFun()
            self.tabFun()
            self.table.delete(*self.table.get_children())    
            self.cur.execute("select b.productId,b.customerId,b.customerName,p.name,p.price,b.quantity,b.total from billing as b inner join products as p on b.productId=p.id where customerId=%s;",(customerId))
            addData= self.cur.fetchall()
            for i in addData:
                self.table.insert('',tk.END,values=i)
            
            self.cur.execute("insert into billData (customerId,customerName,totalAmount,products,quantities,productNames) select b.customerId,max(b.customerName) as customerName,sum(b.total) as totalAmount,group_concat(b.productId) as productIds , group_concat(p.name) as productNames ,group_concat(b.quantity) as quantities from billing as b inner join products as p on b.productId = p.id where b.customerId=%s group by b.customerId",(customerId))
            self.con.commit()
            
            
            self.productNameEntry.delete(0,tk.END)
            self.productIdSearchEntry.delete(0,tk.END)
            self.productPriceEntry.delete(0,tk.END)
            self.productQuantityEntry.delete(0,tk.END)
            self.customerIdEntry.delete(0,tk.END)
            self.customerNameEntry.delete(0,tk.END)
            self.tabFun()
            self.table.delete(*self.table.get_children()) 
            self.totalBtn.config(text="")
            self.saveBillToPDF(customerId)
            self.root.destroy()
            
            


        else:
            messagebox.showerror("Error","pls enter all fields!")
            self.root.destroy()
            
    def clearAllFunc(self):
        self.productNameEntry.delete(0,tk.END)
        self.productIdSearchEntry.delete(0,tk.END)
        self.productPriceEntry.delete(0,tk.END)
        self.productQuantityEntry.delete(0,tk.END)
        self.customerIdEntry.delete(0,tk.END)
        self.customerNameEntry.delete(0,tk.END)
        self.tabFun()
        self.table.delete(*self.table.get_children()) 
        self.totalBtn.config(text="")
        


    def saveBillToPDF(self, customerId):
        try:
            self.dbFun()
            self.cur.execute("""
            SELECT b.productId, p.name, p.price, b.quantity, b.total
            FROM billing AS b
            INNER JOIN products AS p ON b.productId = p.id
            WHERE b.customerId = %s;
            """, (customerId,))
            data = self.cur.fetchall()

            self.cur.execute("""
            SELECT MAX(customerName), SUM(total)
            FROM billing
            WHERE customerId = %s;
            """, (customerId,))
            customer_data = self.cur.fetchone()
            customer_name, total_amount = customer_data

            if not data:
                messagebox.showerror("Error", "No data to save for this customer.")
                return

            filename = f"bill_customer_{customerId}.pdf"
            pdf = canvas.Canvas(filename, pagesize=A4)
            width, height = A4
            y = height - 50

            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawCentredString(width / 2, y, "SAFIE STORE BILL RECEIPT")
            y -= 40

            pdf.setFont("Helvetica", 12)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            pdf.drawString(50, y, f"Date: {now}")
            y -= 20
            pdf.drawString(50, y, f"Customer ID   : {customerId}")
            y -= 20
            pdf.drawString(50, y, f"Customer Name : {customer_name}")
            y -= 30

            pdf.line(40, y, width - 40, y)
            y -= 20
            pdf.drawString(50, y, f"{'PID':<6} {'Product Name':<20} {'Qty':<5} {'Price':<7} {'Total':<7}")
            y -= 20
            pdf.line(40, y, width - 40, y)
            y -= 20

            for row in data:
                pid, name, price, qty, total = row
                pdf.drawString(50, y, f"{pid:<6} {name:<20} {qty:<5} {price:<7} {total:<7}")
                y -= 20
                if y < 100:
                    pdf.showPage()
                    y = height - 50

            pdf.line(40, y, width - 40, y)
            y -= 20
            pdf.drawRightString(width - 50, y, f"Total Amount: Rs. {total_amount}")
            y -= 40
            pdf.drawCentredString(width / 2, y, "Thank you for shopping with us!")
            
            
            pdf.save()

            # Open the PDF automatically
            try:
                if platform.system() == "Windows":
                    os.startfile(filename)
                elif platform.system() == "Darwin":  # macOS
                    os.system(f"open {filename}")
                else:  # Linux
                    os.system(f"xdg-open {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"PDF saved but failed to open: {e}")
                self.root.destroy()

            self.cur.execute("delete from billing where customerId=%s",(customerId))
            self.con.commit()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF: {e}")
            self.root.destroy()
         
    def dbFun(self):
        self.con = pymysql.connect(host="localhost",user="root",passwd="S@fi830068",database="billing_software")
        self.cur = self.con.cursor()
        
    
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def backFunc(self): 
        self.root.destroy()
