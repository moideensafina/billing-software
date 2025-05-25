import tkinter as tk
from createProduct import Create_Product
from showProduct import Show_Product
from updateProduct import Update_Product
from invoice import Product_billing
from showBillData import Show_Bill_Data

class MenuPage():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Menu Page")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        label = tk.Label(self.root, text="Billing Software", font=("Arial", 30, "bold"),bg=self.clr(27, 38, 49), bd=4, relief="groove", fg="white")
        label.pack(side="top", fill="x", ipady=10)
        
        
        #menu frame
        
        menuFrame = tk.Frame(self.root, bg=self.clr(27, 38, 49), bd=4, relief="ridge")
        menuFrame.place(width=self.width-250, height=self.height -250, x=100, y=120)
        
        
        createBtn = tk.Button(menuFrame, text="Create Product", command=self.go_to_create_product,  width=22,padx=8,pady=8,font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black")
        createBtn.grid(row=0, column=0,padx=40,pady=100)
        
        ShowProductBtn = tk.Button(menuFrame, text="Show Product", command=self.go_to_show_product,width=22,padx=8,pady=8, font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black")
        ShowProductBtn.grid(row=0, column=1, padx=40,pady=100)
        
        updateProductBtn = tk.Button(menuFrame, text="Update Product",command=self.go_to_update_product, width=22,padx=8,pady=8, font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black")
        updateProductBtn.grid(row=0, column=2, padx=40,pady=100)
        
        lowestBtn = tk.Button(menuFrame, text="Show Bill Data",command=self.go_to_bill_data, width=22,padx=8,pady=8, font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black")
        lowestBtn.grid(row=1, column=0, padx=40,pady=100)
        
        invoiceBtn = tk.Button(menuFrame, text="Invoice",command=self.go_to_product_billing, width=22,padx=8,pady=8, font=("Arial", 16, "bold"),bg=self.clr(174, 182, 191), relief="raised", bd=2, fg="black")
        invoiceBtn.grid(row=1, column=1, padx=40,pady=100)
        
        #      tk.Button(self.root, text="Close", command=self.root.destroy).pack(pady=20)
        
        self.root.mainloop()
    def go_to_create_product(self):
            Create_Product()
            
    def go_to_show_product(self):
            Show_Product()
    def go_to_update_product(self):
            Update_Product()
    def go_to_product_billing(self):
            Product_billing()
    def go_to_bill_data(self):
            Show_Bill_Data()
                
    
        
        
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"