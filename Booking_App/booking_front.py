from tkinter import *
from backend import Database
import sqlite3
root=Tk()
class Booking:
    def __init__(self,root):
        self.database=Database('ticket.db')
        self.conn=sqlite3.connect('ticket.db')
        self.cur=self.conn.cursor()
        self.font=("Arial",14)
        self.seat=[]
        self.str_seat=None
        self.button_create()
        self.check_ticket()
        
        self.l5=Label(root,text="")
        self.l5.grid(row=2,column=0)

        self.list1=Listbox(root,height=8,width=90)
        self.list1.grid(row=5,column=0,columnspan=9,pady=6)

        self.list1.bind("<<ListboxSelect>>",self.get_selected_row)

        self.l1=Label(root,text="Name:",font=self.font)
        self.l1.grid(row=0,column=5)

        self.name_text=StringVar()
        self.e1=Entry(root,textvariable=self.name_text)
        self.e1.grid(row=0,column=6)
        self.e1.focus()

        self.l2=Label(root,text="Age:",font=self.font)
        self.l2.grid(row=0,column=7)

        self.age_text=StringVar()
        self.e2=Entry(root,textvariable=self.age_text)
        self.e2.grid(row=0,column=8)

        self.l3=Label(root,text="E-Mail:",font=self.font)
        self.l3.grid(row=1,column=5,padx=3)

        self.email_text=StringVar()
        self.e3=Entry(root,textvariable=self.email_text)
        self.e3.grid(row=1,column=6,padx=3)

        self.l4=Label(root,text="Number:",font=self.font)
        self.l4.grid(row=1,column=7,padx=3)

        self.number_text=StringVar()
        self.e4=Entry(root,textvariable=self.number_text)
        self.e4.grid(row=1,column=8,padx=3)

        self.b22=Button(root,text="Book",width=5,font=self.font,command=self.book_ticket)
        self.b22.grid(row=3,column=6,columnspan=2)

        cancel=Button(root,text="Cancel",width=5,font=self.font,command=self.cancel_ticket)
        cancel.grid(row=2,column=8,columnspan=1)

        clear=Button(root,text="Clear",width=5,font=self.font,command=self.clear_seat)
        clear.grid(row=2,column=5,columnspan=1)

        view=Button(root,text="View",width=5,font=self.font,command=self.view_seats)
        view.grid(row=2,column=6,columnspan=2)

    def check_ticket(self):
    
        try:
            self.cur.execute("SELECT * FROM ticket")
            self.view_tuple=self.cur.fetchall()
            for row in self.view_tuple:
                self.n=row[5]
                self.n1=self.n.split(",")
                #print(self.n)
                #print(self.n1)
                for ind in self.n1:
                    self.button_change(int(ind))
                    #print(ind)
        except:
            pass
    def get_selected_row(self,event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def button_create(self):
        self.b1=Button(root,text="1",width=2,height=1,command=lambda: self.button_click(1))
        self.b1.grid(row=0,column=0,padx=3,pady=3)

        self.b2=Button(root,text="2",width=2,height=1,command=lambda: self.button_click(2))
        self.b2.grid(row=1,column=0,padx=3,pady=3)

        self.b5=Button(root,text="5",width=2,height=1,command=lambda: self.button_click(5))
        self.b5.grid(row=0,column=1,padx=3,pady=3)

        self.b6=Button(root,text="6",width=2,height=1,command=lambda: self.button_click(6))
        self.b6.grid(row=1,column=1,padx=3,pady=3)

        self.b9=Button(root,text="9",width=2,height=1,command=lambda: self.button_click(9))
        self.b9.grid(row=0,column=2,padx=3,pady=3)

        self.b10=Button(root,text="10",width=2,height=1,command=lambda: self.button_click(10))
        self.b10.grid(row=1,column=2,padx=3,pady=3)

        self.b13=Button(root,text="13",width=2,height=1,command=lambda: self.button_click(13))
        self.b13.grid(row=0,column=3,padx=3,pady=3)

        self.b14=Button(root,text="14",width=2,height=1,command=lambda: self.button_click(14))
        self.b14.grid(row=1,column=3,padx=3,pady=3)

        self.b17=Button(root,text="17",width=2,height=1,command=lambda: self.button_click(17))
        self.b17.grid(row=0,column=4,padx=3,pady=3)

        self.b18=Button(root,text="18",width=2,height=1,command=lambda: self.button_click(18))
        self.b18.grid(row=1,column=4,padx=3,pady=3)

        self.b3=Button(root,text="3",width=2,height=1,command=lambda: self.button_click(3))
        self.b3.grid(row=3,column=0,padx=3,pady=3)

        self.b4=Button(root,text="4",width=2,height=1,command=lambda: self.button_click(4))
        self.b4.grid(row=4,column=0,padx=3,pady=3)

        self.b7=Button(root,text="7",width=2,height=1,command=lambda: self.button_click(7))
        self.b7.grid(row=3,column=1,padx=3,pady=3)

        self.b8=Button(root,text="8",width=2,height=1,command=lambda: self.button_click(8))
        self.b8.grid(row=4,column=1,padx=3,pady=3)

        self.b11=Button(root,text="11",width=2,height=1,command=lambda: self.button_click(11))
        self.b11.grid(row=3,column=2,padx=3,pady=3)

        self.b12=Button(root,text="12",width=2,height=1,command=lambda: self.button_click(12))
        self.b12.grid(row=4,column=2,padx=3,pady=3)

        self.b15=Button(root,text="15",width=2,height=1,command=lambda: self.button_click(15))
        self.b15.grid(row=3,column=3,padx=3,pady=3)

        self.b16=Button(root,text="16",width=2,height=1,command=lambda: self.button_click(16))
        self.b16.grid(row=4,column=3,padx=3,pady=3)

        self.b19=Button(root,text="19",width=2,height=1,command=lambda: self.button_click(19))
        self.b19.grid(row=2,column=4,padx=3,pady=3)

        self.b20=Button(root,text="20",width=2,height=1,command=lambda: self.button_click(20))
        self.b20.grid(row=3,column=4,padx=3,pady=3)

        self.b21=Button(root,text="21",width=2,height=1,command=lambda: self.button_click(21))
        self.b21.grid(row=4,column=4,padx=3,pady=3)

    def clear_seat(self):
        self.seat.clear()
        self.button_create()
        self.check_ticket()

    def button_change(self,number):
        if number==1:
            self.b1.destroy()
            self.lb1=Label(root,text='1',width=2,height=1)
            self.lb1.grid(row=0,column=0,padx=5,pady=5)
        elif number==2:
            self.b2.destroy()
            self.lb2=Label(root,text='2',width=2,height=1)
            self.lb2.grid(row=1,column=0,padx=5,pady=5)
        elif number==3:
            self.b3.destroy()
            self.lb3=Label(root,text='3',width=2,height=1)
            self.lb3.grid(row=3,column=0,padx=5,pady=5)
        elif number==4:
            self.b4.destroy()
            self.lb4=Label(root,text='4',width=2,height=1)
            self.lb4.grid(row=4,column=0,padx=5,pady=5)
        elif number==5:
            self.b5.destroy()
            self.lb5=Label(root,text='5',width=2,height=1)
            self.lb5.grid(row=0,column=1,padx=5,pady=5)
        elif number==6:
            self.b6.destroy()
            self.lb6=Label(root,text='6',width=2,height=1)
            self.lb6.grid(row=1,column=1,padx=5,pady=5)
        elif number==7:
            self.b7.destroy()
            self.lb7=Label(root,text='7',width=2,height=1)
            self.lb7.grid(row=3,column=1,padx=5,pady=5)
        elif number==8:
            self.b8.destroy()
            self.lb8=Label(root,text='8',width=2,height=1)
            self.lb8.grid(row=4,column=1,padx=5,pady=5)
        elif number==9:
            self.b9.destroy()
            self.lb9=Label(root,text='9',width=2,height=1)
            self.lb9.grid(row=0,column=2,padx=5,pady=5)
        elif number==10:
            self.b10.destroy()
            self.lb10=Label(root,text='10',width=2,height=1)
            self.lb10.grid(row=1,column=2,padx=5,pady=5)
        elif number==11:
            self.b11.destroy()
            self.lb11=Label(root,text='11',width=2,height=1)
            self.lb11.grid(row=3,column=2,padx=5,pady=5)
        elif number==12:
            self.b12.destroy()
            self.lb12=Label(root,text='12',width=2,height=1)
            self.lb12.grid(row=4,column=2,padx=5,pady=5)
        elif number==13:
            self.b13.destroy()
            self.lb13=Label(root,text='13',width=2,height=1)
            self.lb13.grid(row=0,column=3,padx=5,pady=5)
        elif number==14:
            self.b14.destroy()
            self.lb14=Label(root,text='14',width=2,height=1)
            self.lb14.grid(row=1,column=3,padx=5,pady=5)
        elif number==15:
            self.b15.destroy()
            self.lb15=Label(root,text='15',width=2,height=1)
            self.lb15.grid(row=3,column=3,padx=5,pady=5)
        elif number==16:
            self.b16.destroy()
            self.lb16=Label(root,text='16',width=2,height=1)
            self.lb16.grid(row=4,column=3,padx=5,pady=5)
        elif number==17:
            self.b17.destroy()
            self.lb17=Label(root,text='17',width=2,height=1)
            self.lb17.grid(row=0,column=4,padx=5,pady=5)
        elif number==18:
            self.b18.destroy()
            self.lb18=Label(root,text='18',width=2,height=1)
            self.lb18.grid(row=1,column=4,padx=5,pady=5)
        elif number==19:
            self.b19.destroy()
            self.lb19=Label(root,text='19',width=2,height=1)
            self.lb19.grid(row=2,column=4,padx=5,pady=5)
        elif number==20:
            self.b20.destroy()
            self.lb20=Label(root,text='20',width=2,height=1)
            self.lb20.grid(row=3,column=4,padx=5,pady=5)
        elif number==21:
            self.b21.destroy()
            self.lb21=Label(root,text='21',width=2,height=1)
            self.lb21.grid(row=4,column=4,padx=5,pady=5)

    def button_click(self,seat_number):
        self.seat.append(str(seat_number))
        self.str_seat=",".join(self.seat)
        self.button_change(seat_number)
        
    def book_ticket(self):
        if self.name_text.get() and self.age_text.get() and self.email_text.get() and self.number_text.get() and self.str_seat:
            self.database.book(self.name_text.get(),self.age_text.get(),self.email_text.get(),self.number_text.get(),self.str_seat)
            self.list1.insert(END,self.name_text.get(),self.age_text.get(),self.email_text.get(),self.number_text.get(),self.seat)
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
            self.seat.clear()
        else:
            pass
        
    def cancel_ticket(self):
        try:
            self.database.cancel(self.selected_tuple[0])
            self.clear_seat()
        except AttributeError:
            pass
            
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.list1.delete(0,END)
        for row in self.database.view():
            self.list1.insert(END,row)

    def view_seats(self):
        self.list1.delete(0,END)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        for row in self.database.view():
            self.list1.insert(END,row)

booking=Booking(root)
root.wm_title("Booking")
root.mainloop()
