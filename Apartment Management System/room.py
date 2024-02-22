from tkinter import*
from PIL import Image,ImageTk   #pip install pilow
from tkinter import ttk
import random
import mysql.connecter
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Apartment Management System")
        self.root.geometry("1295x550+230+220")
         
        #==============title=========================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #==================logo=====================
        img2=Image.open(C:\Users\saad9\OneDrive\Desktop\Apartment Management System\images)
        img2=img2(resize(100,40),Image.ANTIALIAS)     
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,releif=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        #==================LabelFrame====================
        labelframeleft=Label.Frame(self.root,bd=2,releif=RIDGE,text="Roombooking Details",font=("arial",12,"bold"),padx=2,pady=6)
        labelframeleft.place(x=5,y=5,width=425,height=490)

        #===================labels and entrys=================
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=w)
        
        empty_contact=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=20)
        empty_contact.grid(row=0,column=1,sticky=w)
        
            
        #Check_in Date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=w)
        txtcheck_in_date=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check_in Date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=w)
        txt_Check_out=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=w)

        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","laxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,cxolumn=1)

        #Available Room
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=w)
        txtRoomAvailable=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=w)
        txtMeal=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        #No of Days
        lblNoofDays=Label(labelframeleft,font=("arial",12,"bold"),text="No of Days:",padx=2,pady=6)
        lblNoofDays.grid(row=6,column=0,sticky=w)
        txtNoofDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoofDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=w)
        txtPaidTax=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=w)
        txtSubTotal=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(labelframeleft,font=("arial",12,"bold"),text="TotalCost:",padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=w)
        txtTotalCost=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)

        


























if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()