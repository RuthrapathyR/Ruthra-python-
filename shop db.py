from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import MySQL_Interface
import trying
from datetime import date
from tkinter import *
import random
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter import messagebox
import MySQL_Interface
from datetime import date
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar


input_color = '#dbd9db'

def sum():
    def back():
        mpwin.withdraw()
        menuwin.deiconify()

    def add_product():
        mpwin.withdraw()
        a_pro = Toplevel()

        def on_closing1p1():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                a_pro.withdraw()
                menuwin.deiconify()

        a_pro.protocol("WM_DELETE_WINDOW", on_closing1p1)

        def backa_p():
            q=messagebox.askyesno("Warning","Your Data will be lost")
            if q==1:
                a_pro.withdraw()
                mpwin.deiconify()

        w = 500
        h = 500
        ws = a_pro.winfo_screenwidth()
        hs = a_pro.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        a_pro.geometry('%dx%d+%d+%d' % (w, h, x, y))
        a_pro.config(bg=input_color)
        a_pro.resizable(0, 0)
        add = Label(a_pro, text="   ADD PRODUCT", bg=input_color, font='boldUnderline 20', padx=30, pady=20).grid(
            row=0, column=0, columnspan=2)
        inp_id = Label(a_pro, text="PRODUCT_ID:", bg=input_color, font='bold 15', pady=20, justify='left').grid(row=1,
                                                                                                              column=0,
                                                                                                              sticky='w')
        inp_name = Label(a_pro, text="PRODUCT_NAME :", bg=input_color, font='bold 15', pady=20, justify='left').grid(
            row=2, column=0, sticky='w')
        inp_cat = Label(a_pro, text="PRODUCT_CATEGORY :", bg=input_color, font='bold 15', pady=20,
                        justify='left').grid(row=3, column=0, sticky='w')
        inp_qty = Label(a_pro, text="PRODUCT_QUANTITY :", bg=input_color, font='bold 15', pady=20,
                        justify='left').grid(row=4, column=0, sticky='w')
        inp_rate = Label(a_pro, text="PRODUCT_RATE :", bg=input_color, font='bold 15', pady=20, justify='left').grid(
            row=5, column=0, sticky='w')
        # call function when we click on entry box
        def click(*args):
            inp_id1.delete(0, 'end')

        inp_id1 = Entry(a_pro, justify="left", highlightcolor='#F24014', bg='#dbd9db', font='20')
        inp_id1.grid(row=1, column=1)
        inp_id1.insert(0, 'Enter Only Digits:- ')
        inp_id1.bind("<Button-1>", click)
        def callback(i):
            if i.isdigit() or i == '':
                return True

            else:
                return False

        reg = a_pro.register(callback)

        inp_id1.config(validate="all", validatecommand=(reg, '%P'))

        inp_id1.focus()


        inp_name1 = Entry(a_pro, justify="left", highlightcolor='#F24014', bg='#dbd9db', font='20')
        inp_name1.grid(row=2,   column=1)
        s = '''select category_name from category ;'''.format()
        status, error_msg, data = MySQL_Interface.Execute_Select(s)
        list1=data
        inp_cat1 = ttk.Combobox(a_pro,value=list1,state='readonly', justify="left", font='20')
        inp_cat1.grid(row=3,  column=1)
        inp_qty1 = Entry(a_pro, justify="left", highlightcolor='#F24014', bg='#dbd9db', font='20')
        inp_qty1.grid(row=4,column=1)
        def click(*args):
            inp_qty1.delete(0, 'end')

        inp_qty1.insert(0, 'Enter Only Digits:- ')
        inp_qty1.bind("<Button-1>", click)

        def callback(i):
            if i.isdigit() or i == '':
                return True

            else:
                return False

        reg = a_pro.register(callback)

        inp_qty1.config(validate="all", validatecommand=(reg, '%P'))

        inp_qty1.focus()

        inp_rate1 = Entry(a_pro, highlightcolor='#F24014', bg='#dbd9db', font='20', justify='center')



        inp_rate1.insert(0, 'Enter Only Digits:- ')
        def click(*args):
            inp_rate1.delete(0, 'end')
        inp_rate1.bind("<Button-1>", click)
        inp_rate1.grid(row=5,   column=1)

        def callback(i):
            if i.isdigit() or i == '':
                return True

            else:
                return False

        reg = a_pro.register(callback)

        inp_rate1.config(validate="all", validatecommand=(reg, '%P'))

        inp_rate1.focus()
        def submit1():
            a=True
            inp_id11 = inp_id1.get()
            inp_name11 = inp_name1.get()
            inp_cat11 = inp_cat1.get()

            sq = '''select category_name,category_id from category ;'''
            status, error_msg, data = MySQL_Interface.Execute_Select(sq)
            fq = {}
            for i in data:
                fq[i[0]] = i[1]
            print(fq)
            inp_qty11 = inp_qty1.get()
            inp_rate11 = inp_rate1.get()
            s = '''select product_id from product ;'''.format()
            status, error_msg, data = MySQL_Interface.Execute_Select(s)
            list11 = data
            op=""
            if inp_qty11=="" or inp_rate11=='' or inp_id11=='' or inp_name11=='' or inp_cat11=='':
                if inp_qty11=='':
                    op="NO OF QUANTITY is mandatory"
                elif inp_rate11=="":
                    op="RATE is mandatory"
                elif inp_id11=="":
                    op="PRODUCT ID is mandatory"
                elif inp_name11=="":
                    op="PRODUCT is mandatory"
                elif inp_cat11=="":
                    op="CATEGORY ID  is mandatory"

                messagebox.showwarning('Warning!', op)
                a=False
            else:
                if inp_id11.isalpha() == True:
                    messagebox.showwarning('Warning!', 'Entered product id is wrong! Only numbers allowed!')
                    a = False
                else:
                    if [int(inp_id11)] in list11:
                        messagebox.showwarning('Warning!', 'Entered Product_Id exist! Enter New Id')
                        a = False
                if inp_rate11.isalpha() == True:
                    messagebox.showwarning('Warning!', 'Entered rate is wrong! Only numbers allowed!')
                    a = False
                if inp_qty11.isalpha() == True:
                    messagebox.showwarning('Warning!', "Entered quantity is wr ong! Only numbers allowed!")
                    a = False
            if a!=False     and inp_rate1.get()!="Enter Only Digits:- ":
                Ins1 = '''insert into product(product_id,product_name,category_id,quantity_in_stock,rate)
                 values({},'{}',{},{},{})'''.format(inp_id11,inp_name11,fq[inp_cat11],inp_qty11, inp_rate11)

                lst = [Ins1]
                print(Ins1)
                status, error_msg = MySQL_Interface.Execute_IUD(lst)
                if status == False:
                    messagebox.showerror('WARNING!', error_msg)
                else:
                    messagebox.showinfo('Success', "Product Created Succesfully")
                a_pro.withdraw()
                mpwin.deiconify()


        submit = Button(a_pro, text="SUBMIT", font="5", bg=input_color, width=10, command=submit1).place(x=320,
                                                                                                        y=430)
        exit = Button(a_pro, text="BACK", font="5", bg=input_color, width=10, command=backa_p).place(x=10, y=430)
        a_pro.mainloop()

    def upd_product():
        mpwin.withdraw()
        u_pro = Toplevel()

        def on_closing1p2():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                u_pro.withdraw()
                mpwin.deiconify()

        u_pro.protocol("WM_DELETE_WINDOW", on_closing1p2)
        def back2():
            u_pro.withdraw()
            mpwin.deiconify()

        def backu_p():
            q=messagebox.askyesno("Warning","Your Data will be lost")
            if q==1:
                u_pro.withdraw()
                mpwin.deiconify()

        def pro_namee():
            u_pro.withdraw()
            p=Toplevel()

            def on_closing1q():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    p.withdraw()
                    u_pro.deiconify()

            p.protocol("WM_DELETE_WINDOW", on_closing1q)
            w = 400
            h = 190
            ws = p.winfo_screenwidth()
            hs = p.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            p.geometry('%dx%d+%d+%d' % (w, h, x, y))
            p.config(bg=input_color)
            p.resizable(0, 0)
            pro_id=Label(p,text='Product Id',font='30',bg=input_color).grid(row=1,column=0,pady=30,padx=15)
            new_pro_name=Label(p,text='Product Name',font='30',bg=input_color).grid(row=2,column=0,padx=15)
            s = '''select product_id from product ;'''.format()
            status, error_msg, data = MySQL_Interface.Execute_Select(s)
            print(data)
            list111 = data
            pro_id1=ttk.Combobox(p , value=list111,state='readonly', justify="left", font='30')
            pro_id1.grid(row=1,  column=1)
            new_pro_name1=Entry(p,width=35)
            new_pro_name1.grid(row=2,column=1)

            def submit11():
                pro_id11=pro_id1.get()
                new_pro_name11=new_pro_name1.get()
                s = '''update product set product_name='{}' where product_id={};'''.format(new_pro_name11 ,(pro_id11) )
                o = [s]
                sta=True
                if new_pro_name11 == "" :
                    sta=False
                    messagebox.showwarning('Warning!', "Required field is empty")
                if sta!=False:
                    status, error_msg = MySQL_Interface.Execute_IUD(o)
                    messagebox.showinfo("Succes","Changed succesfully!")
                    p.withdraw()
                    u_pro.deiconify()

            sub1=Button(p,text='SUBMIT',borderwidth=5,font='bold 12',command=submit11).place(x=150,y=130)
#            back1=Button(p,text='BACK',borderwidth=5,font='bold 15',command=submit11).place(x=10,y=130)

            p.mainloop()
#secon pro namee
        def q_p():
            u_pro.withdraw()
            p1=Toplevel()

            def on_closing1p3():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    p1.withdraw()
                    u_pro.deiconify()

            p1.protocol("WM_DELETE_WINDOW", on_closing1p3)
            w = 400
            h = 190
            ws = p1.winfo_screenwidth()
            hs = p1.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            p1.geometry('%dx%d+%d+%d' % (w, h, x, y))
            p1.config(bg=input_color)
            p1.resizable(0, 0)
            product_id=Label(p1,text='Product name',font='30',bg=input_color).grid(row=1,column=0,pady=30,padx=15)
            quantity_purchased=Label(p1,text='Quantity in Stock',font='30',bg=input_color).grid(row=2,column=0,padx=15)
            s1 = '''select product_name from product ;'''.format()
            status, error_msg, data = MySQL_Interface.Execute_Select(s1)
            list1111 = data
            pro_id11=ttk.Combobox(p1 , value=list1111,state='readonly', justify="left", font='30')
            pro_id11.grid(row=1,  column=1)
            quantity_purchased1=Entry(p1,width=35)
            quantity_purchased1.grid(row=2,column=1)

            def submit111():
                pro_id111=pro_id11.get()
                quantity_purchased11=quantity_purchased1.get()
                s = '''update product set Quantity_in_stock='{}' where product_name='{}';'''.format(quantity_purchased11 ,(pro_id111.strip('{}')) )
                o = [s]
                sta=True
                if quantity_purchased11 == "" :
                    sta=False
                    messagebox.showwarning('Warning!', "Required field is empty")
                else:
                    if quantity_purchased11.isdigit() != True :
                        sta=False
                        messagebox.showwarning('Warning!', "Only Digits allowed")
                    if sta!=False:
                        status, error_msg = MySQL_Interface.Execute_IUD(o)
                        messagebox.showinfo("Success","Changed succesfully!")
                        p1.withdraw()
                        u_pro.deiconify()
            sub11=Button(p1,text='SUBMIT',borderwidth=5,font='bold 12',command=submit111,bg=input_color).place(x=150,y=130)
            p1.mainloop()
#product_rate
        def p_r():
            u_pro.withdraw()
            p11=Toplevel()

            def on_closing1p4():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    p11.withdraw()
                    u_pro.deiconify()

            p11.protocol("WM_DELETE_WINDOW", on_closing1p4)
            w = 400
            h = 190
            ws = p11.winfo_screenwidth()
            hs = p11.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            p11.geometry('%dx%d+%d+%d' % (w, h, x, y))
            p11.config(bg=input_color)
            p11.resizable(0, 0)
            product_id1=Label(p11,text='Product name',font='30',bg=input_color).grid(row=1,column=0,pady=30,padx=15)
            product_rate=Label(p11,text='Rate',font='30',bg=input_color).grid(row=2,column=0,padx=15)
            s11 = '''select product_name from product ;'''.format()
            status, error_msg, data = MySQL_Interface.Execute_Select(s11)
            list11111 = data
            pro_id111=ttk.Combobox(p11 , value=list11111,state='readonly', justify="left", font='30')
            pro_id111.grid(row=1,  column=1)
            product_rate1=Entry(p11,width=35)
            product_rate1.grid(row=2,column=1)

            def submit1111():
                pro_id1111=pro_id111.get()
                product_rate11=product_rate1.get()
                s = '''update product set Rate='{}' where product_name='{}';'''.format(product_rate11 ,(pro_id1111.strip('{}')) )
                o = [s]
                sta=True
                if product_rate11 == "" :
                    sta=False
                    messagebox.showwarning('Warning!', "Required field is empty")
                else:
                    if product_rate11.isdigit() != True :
                        sta=False
                        messagebox.showwarning('Warning!', "Only Digits allowed")
                    if sta!=False:
                        status, error_msg = MySQL_Interface.Execute_IUD(o)
                        messagebox.showinfo("Success","Changed succesfully!")
                        p11.withdraw()
                        u_pro.deiconify()
            sub11=Button(p11,text='SUBMIT',borderwidth=5,font='bold 12',command=submit1111).place(x=160,y=130)
            p11.mainloop()

        w = 450
        h = 400
        ws = u_pro.winfo_screenwidth()
        hs = u_pro.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs /
             2) - (h / 2)
        u_pro.geometry('%dx%d+%d+%d' % (w, h, x, y))
        u_pro.config(bg=input_color)
        u_pro.resizable(0, 0)
        upd = Label(u_pro, text=" UPDATE PRODUCT", bg=input_color, font='boldUnderline 20').pack( padx=30, pady=20)
        pro_name = Button(u_pro, text="PRODUCT_NAME ", bg=input_color, font='bold 15',width=20,command=pro_namee).pack( padx=30, pady=20)
        qty_stk = Button(u_pro, text="QUANTITY_IN_STOCK", bg=input_color, font='bold 15',width=20,command=q_p).pack(padx=30, pady=20)
        pro_rate = Button(u_pro, text="PRODUCT_RATE ", bg=input_color, font='bold 15',width=20,command=p_r).pack( padx=30, pady=20)

        back = Button(u_pro, text="BACK", bg=input_color, font='bold 15',command=back2).place( x=200,y=350)

        u_pro.mainloop()
    def delete_product():
        mpwin.withdraw()
        pa1=Toplevel()

        def on_closing15p():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                pa1.withdraw()
                mpwin.deiconify()

        pa1.protocol("WM_DELETE_WINDOW", on_closing15p)
        w = 350
        h = 130
        ws = pa1.winfo_screenwidth()
        hs = pa1.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        pa1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        pa1.config(bg=input_color)
        pa1.resizable(0, 0)
        product_id2 = Label(pa1, text='Product Id :', font='40').grid(row=0, column=0, pady=30, padx=15)
        d = '''select product_id from product ;'''.format()
        status, error_msg, data = MySQL_Interface.Execute_Select(d)
        list2 = data
        l = []
        for i in range(0, len(list2)):
            a = list2[i][::].pop()
            l.append(a)
        pro1_id2 = ttk.Combobox(pa1, value=l, state='readonly', justify="left", font='30')
        pro1_id2.grid(row=0, column=1)
        def submi1t2():
            pro1_id22 = pro1_id2.get()
            d1 = '''delete from product where product_id={}'''.format(pro1_id22)
            o = [d1]
            status, error_msg = MySQL_Interface.Execute_IUD(o)
            if pro1_id22!='':
                if status == True:
                    messagebox.showinfo('success', "Product deleted Succesfully")
                    pa1.withdraw()
            else:
                messagebox.showwarning("Warning","Require Some Data")

        sub2 = Button(pa1, text='SUBMIT', borderwidth=5, font='bold 12', command=submi1t2).place(x=140, y=70)
        pa1.mainloop()
    #show Databases

    def search():
        mpwin.withdraw()
        search_tk = Toplevel()

        def on_closing1p6():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                search_tk.withdraw()
                mpwin.deiconify()

        search_tk.protocol("WM_DELETE_WINDOW", on_closing1p6)
        w = 320
        h = 130
        ws = search_tk.winfo_screenwidth()
        hs = search_tk.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        search_tk.geometry('%dx%d+%d+%d' % (w, h, x, y))
        search_tk.config(bg=input_color)
        search_tk.resizable(0, 0)

        product_ide = Label(search_tk, text='Product NAME :', font='40', bg=input_color).grid(row=0, column=0, pady=30,
                                                                                            padx=15)
        dv = '''select product_name from product ;'''.format()
        status, error_msg, data = MySQL_Interface.Execute_Select(dv)
        listv2 = data
        pro111_id2 = ttk.Combobox(search_tk, value=listv2, state='readonly', justify="left", font='30')
        pro111_id2.grid(row=0, column=1)

        def submit5678():
            pro1111_id2 = pro111_id2.get()
            if pro1111_id2 == '':
                messagebox.showerror("Error", "No Data!!")
            else:
                search_tk.withdraw()
                search1_tk = Toplevel()

                def on_closing1p6d():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        search1_tk.withdraw()
                        mpwin.deiconify()

                search1_tk.protocol("WM_DELETE_WINDOW", on_closing1p6d)
                w = 410
                h = 440
                ws = search1_tk.winfo_screenwidth()
                hs = search1_tk.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                search1_tk.geometry('%dx%d+%d+%d' % (w, h, x, y))
                search1_tk.config(bg=input_color)
                search1_tk.resizable(0, 0)
                add = Label(search1_tk, text="  PRODUCT DETAILS", bg=input_color, font='boldUnderline 20', padx=30,
                            pady=20).grid(
                    row=0, column=0, columnspan=2)
                inp_id12 = Label(search1_tk, text="  PRODUCT_ID                :", bg=input_color, font='bold 15',
                                 pady=20, justify='left').grid(row=1,
                                                               column=0,
                                                               sticky='w')
                inp_name12 = Label(search1_tk, text="  PRODUCT_NAME          :", bg=input_color, font='bold 15', pady=20,
                                   justify='left').grid(
                    row=2, column=0, sticky='w')
                inp_cat12 = Label(search1_tk, text="  PRODUCT_CATEGORY :", bg=input_color, font='bold 15', pady=20,
                                  justify='left').grid(row=3, column=0, sticky='w')
                inp_qty12 = Label(search1_tk, text="  PRODUCT_QUANTITY   :", bg=input_color, font='bold 15', pady=20,
                                  justify='left').grid(row=4, column=0, sticky='w')
                inp_rate12 = Label(search1_tk, text="  PRODUCT_RATE           :", bg=input_color, font='bold 15', pady=20,
                                   justify='left').grid(
                    row=5, column=0, sticky='w')
                s = '''select * from product where product_name = '{}';'''.format((pro1111_id2.strip('{}')))
                status, error_msg, l = MySQL_Interface.Execute_Select(s)
                print("pi",s)
                print("ererer",error_msg)
                print(l)
                #     l=[[1, 'rice ponni 25kg', 1, 100, 1200.0]]
                inp_id21 = Label(search1_tk, text=l[0][0], bg=input_color, font='bold 15', pady=20,
                                 justify='right').grid(
                    row=1,
                    column=1,
                    sticky='w')

                inp_name21 = Label(search1_tk, text=l[0][1], bg=input_color, font='bold 15', pady=20,
                                   justify='right').grid(
                    row=2, column=1, sticky='w')
                inp_cat21 = Label(search1_tk, text=l[0][2], bg=input_color, font='bold 15', pady=20,
                                  justify='right').grid(row=3, column=1, sticky='w')
                inp_qty21 = Label(search1_tk, text=l[0][3], bg=input_color, font='bold 15', pady=20,
                                  justify='right').grid(row=4, column=1, sticky='w')
                inp_rate21 = Label(search1_tk, text=l[0][4], bg=input_color, font='bold 15', pady=20,
                                   justify='right').grid(
                    row=5, column=1, sticky='w')
                search1_tk.mainloop()

                back21=Button(search_tk, text="BACK", font="5", bg=input_color, width=10, command=submit5678).grid()
        submit456 = Button(search_tk, text="SUBMIT", font="5", bg=input_color, width=10, command=submit5678).place(
            x=120, y=80)
        search_tk.mainloop()
#Display database
    def search_all():
        mpwin.withdraw()
        root = Toplevel()

        def on_closing1p7():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.withdraw()
                mpwin.deiconify()

        root.protocol("WM_DELETE_WINDOW", on_closing1p7)
        root.title('Product Table')
        root.geometry('1020x200')
        root.focus_force()

        # define columns
        columns = ('product_id', 'product_name', 'category_id', 'Quantity_in_stock', 'Rate')

        tree = ttk.Treeview(root, columns=columns, show='headings')

        # define headings
        tree.heading('product_id', text='PRODUCT ID')
        tree.heading('product_name', text='PRODUCT NAME')
        tree.heading('category_id', text='CATEGORY ID')
        tree.heading('Quantity_in_stock', text='QUANTITY IN STOCK')
        tree.heading('Rate', text='RATE')
        # generate sample data
        s = '''SELECT * FROM inventory.product;'''
        status, error_msg, contacts = MySQL_Interface.Execute_Select(s)
        # add data to the treeview
        for contact in contacts:
            tree.insert('', END, values=contact)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                messagebox.showinfo(title='Information', message=','.join(str(record)))

      #  tree.bind('<<TreeviewSelect>>', item_selected)
        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # run the app
        root.mainloop()



    def cat_wise():
        rpwin.withdraw()
        cwin = Toplevel()

        w = 850
        h = 560
        ws = cwin.winfo_screenwidth()
        hs = cwin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        cwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        cwin.config(bg=input_color)
        cwin.resizable(0, 0)
        def on_closinp1p():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                cwin.withdraw()
                rpwin.deiconify()

        cwin.protocol("WM_DELETE_WINDOW", on_closinp1p)
        pokes1 = Label(cwin, bg=input_color, font='bold 15', text="START DATE:")
        pokes1.pack()
        pokes1.place(x=10, y=90)
        ed2 = Label(cwin, text="CATEGORY-WISE", bg=input_color, font='bold 25')
        ed2.pack()
        ed2.place(x=280, y=10)

        cal1 = Calendar(cwin, selectmode='day',
                            year=2020, month=5,
                            day=9)

        cal1.pack(pady=2)
        cal1.place(x=150, y=90)



        pokes1g = Label(cwin, bg=input_color, font='bold 15', text="END DATE:")
        pokes1g.pack()
        pokes1g.place(x=430, y=90)

        cal1g = Calendar(cwin, selectmode='day',
                             year=2023, month=5,
                             day=22)

        cal1g.pack(pady=2)
        cal1g.place(x=550, y=90)

            # here we have to
        def SUB_date():
            rj4512 = cal1g.get_date()
            fwe2 = rj4512[len(rj4512) - 2:len(rj4512)] + '/' + rj4512[0:len(rj4512) - 3]

            rj451 = cal1.get_date()
            fwe = rj451[len(rj451) - 2:len(rj451)] + '/' + rj451[0:len(rj451) - 3]

            s = '''select 	DATE_FORMAT(now(),'%Y%m'), category_name, product_name, sum(value)
    from	inventory.order,order_item, product , category 
    where	order_item.product_id = product.product_id
    and	product.category_id = category.category_id
    and	date_purchased between '{}' and '{}'
    group by DATE_FORMAT(now(),'%Y%m'), category_name, product_name
    order by DATE_FORMAT(now(),'%Y%m'), category_name, product_name;'''.format(fwe,fwe2)

            status, error_msg, dataww1 = MySQL_Interface.Execute_Select(s)
            if status == True:
                print(s)
                cwin.withdraw()
                search_tk1p1 = Tk()
                w = 650
                h = 330
                ws = search_tk1p1.winfo_screenwidth()
                hs = search_tk1p1.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                search_tk1p1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                search_tk1p1.config(bg=input_color)
                search_tk1p1.resizable(0, 0)

                def on_closing1p1():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        search_tk1p1.withdraw()
                        rpwin.deiconify()

                search_tk1p1.protocol("WM_DELETE_WINDOW", on_closing1p1)
                    # define columns
                    # date_purchased, product_name, product.product_id, order_item.order_number, order_item.quantity_purchased, product.rate, value

                tree1W11 = ttk.Treeview(search_tk1p1, column=('DATE', 'category_name', 'product_name', 'value'),
                                            show='headings', selectmode='none',
                                            cursor='arrow')

                tree1W11.column("#1", stretch=False, minwidth=150, width=150, anchor=tk.CENTER)

                tree1W11.heading("#1", text="DATE")

                tree1W11.column("#2", stretch=False, minwidth=200, width=100, anchor=tk.CENTER)

                tree1W11.heading("#2", text="CATEGORY")

                tree1W11.column("#3", stretch=False, minwidth=200, width=100, anchor=tk.CENTER)

                tree1W11.heading("#3", text="PRODUCT NAME")

                tree1W11.column("#4", stretch=True, minwidth=250, width=250, anchor=tk.CENTER)

                tree1W11.heading("#4", text="VALUE")

                tree1W11.grid(row=0, column=0, sticky='nsew')
                    # define headings
                for contact in dataww1:
                    tree1W11.insert('', tk.END, values=contact)
                scrollbar = ttk.Scrollbar(search_tk1p1, orient=tk.VERTICAL, command=tree1W11.yview)
                tree1W11.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')

        ed1 = Button(cwin, text="SUBMIT",
                         command=SUB_date, bg=input_color, font='bold 15')
        ed1.pack()
        ed1.place(x=420,y=300)


    def date_wise():
        rpwin.withdraw()
        dwin = Tk()
        w = 440
        h = 680
        ws = dwin.winfo_screenwidth()
        hs = dwin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        dwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        dwin.config(bg=input_color)
        dwin.resizable(0, 0)

        def on_closin1p():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                dwin.withdraw()
                rpwin.deiconify()

        dwin.protocol("WM_DELETE_WINDOW", on_closin1p)
        pokes=Label(dwin,bg=input_color, font='bold 15',text="START DATE:")
        pokes.pack()
        pokes.place(x=10,y=90)
        ed1 = Label(dwin, text="DATE-WISE", bg=input_color, font='bold 25')
        ed1.pack()
        ed1.place(x=120, y=10)

        cal = Calendar(dwin, selectmode='day',
                       year=2023, month=5,
                       day=22,maxdate=date.today())

        cal.pack()
        cal.place(x=160,y=90)

        #here we have to
        def SUB_date():
            rj45 = cal.get_date()
            f = rj45[len(rj45) - 2:len(rj45)] + '/' + rj45[0:len(rj45) - 3]
            cal.place(x=150, y=90)
            s = '''select 	order_item.order_number,inventory.order.date_purchased, product_name, product.product_id, 
	order_item.quantity_purchased, product.rate, value
from	inventory.order , product ,order_item
where	product.product_id = order_item.product_id
and	date_purchased between '{}' and '{}'
order by date_purchased, product_name;'''.format(f, date.today())
            print(s)

            status, error_msg, dataww = MySQL_Interface.Execute_Select(s)

            if status == True:
                print(s)
                print(dataww)
                dwin.withdraw()
                search_tk1p = Tk()
                w = 1324
                h = 130
                ws = search_tk1p.winfo_screenwidth()
                hs = search_tk1p.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                search_tk1p.geometry('%dx%d+%d+%d' % (w, h, x, y))
                search_tk1p.config(bg=input_color)
                search_tk1p.resizable(0, 0)

                def on_closing1p():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        search_tk1p.withdraw()
                        rpwin.deiconify()

                search_tk1p.protocol("WM_DELETE_WINDOW", on_closing1p)
                # define columns
#date_purchased, product_name, product.product_id, order_item.order_number, order_item.quantity_purchased, product.rate, value


                tree1W1 = ttk.Treeview(search_tk1p, column=('order_number', 'Product_name','Product_id', 'Quantity_purchased', 'Rate', 'Value','Date_purchased'), show='headings', selectmode='none',
                                    cursor='arrow')

                tree1W1.column("#1", stretch=False, minwidth=150, width=120, anchor=tk.CENTER)

                tree1W1.heading("#1", text="ORDER NO")


                tree1W1.column("#4", stretch=False, minwidth=200, width=100, anchor=tk.CENTER)

                tree1W1.heading("#4", text="PRODUCT ID")

                tree1W1.column("#3", stretch=True, minwidth=250, width=200, anchor=tk.CENTER)

                tree1W1.heading("#3", text="PRODUCT NAME")

                tree1W1.column("#5", stretch=False, minwidth=200, width=200, anchor=tk.CENTER)

                tree1W1.heading("#5", text="QUANTITY PURCHASED")

                tree1W1.column("#2", stretch=False, minwidth=200, width=200, anchor=tk.CENTER)

                tree1W1.heading("#2", text="DATE PURCHASED")

                tree1W1.column("#6", stretch=False, minwidth=200, width=200, anchor=tk.CENTER)

                tree1W1.heading("#6", text="RATE")

                tree1W1.column("#7", stretch=False, minwidth=200, width=200, anchor=tk.CENTER)

                tree1W1.heading("#7", text="VALUE")

                tree1W1.grid(row=0, column=0, sticky='nsew')
                # define headings
                for contact in dataww:
                    tree1W1.insert('', tk.END, values=contact)
                scrollbar = ttk.Scrollbar(search_tk1p, orient=tk.VERTICAL, command=tree1W1.yview)
                tree1W1.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')

        ed=Button(dwin, text="SUBMIT",
               command=SUB_date,bg=input_color, font='bold 15')
        ed.pack()
        ed.place(x=150,y=310)



        # Execute Tkinter
        dwin.mainloop()
    def backee1():
        rpwin.withdraw()
        menuwin.deiconify()
    def Repots2():
        global rpwin
        menuwin.withdraw()
        rpwin = Tk()

        def on_closing1q1():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                rpwin.withdraw()
                menuwin.deiconify()

        rpwin.protocol("WM_DELETE_WINDOW", on_closing1q1)
        w = 400
        h = 440
        ws = rpwin.winfo_screenwidth()
        hs = rpwin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        rpwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rpwin.config(bg=input_color)
        rpwin.resizable(0, 0)
        titleW = Label(rpwin, text="REPORT", font="Helvectica 27", bg=input_color, pady=20).pack()
        b1W = Button(rpwin, text="DATE-WISE", font="30", bg=input_color, width=25,command=date_wise).pack(
            pady=(20, 0))
        b2W = Button(rpwin, text="CATEGORY-WISE", font=" 30", bg=input_color, width=25,command=cat_wise).pack(
            pady=(20, 0))
        b3W = Button(rpwin, text="MONTHLY-WISE", font="30", bg=input_color, width=25).pack(
            pady=(20, 0))
        b4W = Button(rpwin, text="CATEGORY//MONTHLY-WISE", font="30", bg=input_color, width=25).pack(
            pady=(20, 0))
        b5W = Button(rpwin, text="BACK", font="30", bg=input_color, width=15,command=backee1)
        b5W.pack(
            pady=(20, 0))
        b5W.place(x=125,y=380)
        rpwin.mainloop()
    def exitem():
        messagebox.showinfo("!","THANK YOU FOR VISITING THE SHOP")
        menuwin.withdraw()
    def B():
        global input_color ,menuwin
        menuwin = Tk()

        def on_closing1q3():
             messagebox.showinfo('!',"THANK YOU !")
             menuwin.withdraw()


        menuwin.protocol("WM_DELETE_WINDOW", on_closing1q3)
        w = 400
        h = 450
        ws = menuwin.winfo_screenwidth()
        hs = menuwin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        menuwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        menuwin.config(bg=input_color)
        menuwin.resizable(0, 0)
        title = Label(menuwin, text="PLEASE SELECT THE REQUIRED OPTION:",font="Helvectica 14", bg=input_color,pady=30).pack()
        b1=Button(menuwin,text="MAINTAIN PRODUCT",font="30",bg=input_color,width=25,command=Maintain_Product).pack(pady=(40,0))
        b2=Button(menuwin,text="MAINTAIN SALES",font=" 30",bg=input_color,width=25,command=Maintain_sales).pack(pady=(40,0))
        b3=Button(menuwin,text="REPORTS",font="30",bg=input_color,width=25,command=Repots2).pack(pady=(40,0))
        b4=Button(menuwin,text="EXIT",font="bold 15",bg=input_color,width=20,command=exitem).place(x=85,y=400)
   #     b5=Button(menuwin,text="EXIT",font="5",bg=input_color,width=10).place(x=290,y=395)
        menuwin.mainloop()


    def Maintain_Product():
        global mpwin
        menuwin.withdraw()
        mpwin=Toplevel()

        def on_closing1q4():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                mpwin.withdraw()
                menuwin.deiconify()

        mpwin.protocol("WM_DELETE_WINDOW", on_closing1q4)
        w = 425
        h = 450
        ws = mpwin.winfo_screenwidth()
        hs = mpwin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        mpwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        mpwin.config(bg=input_color)
        mpwin.resizable(0, 0)
        title = Label(mpwin, text="MAINTAIN PRODUCT",font="Helvectica 14", bg=input_color,pady=20).pack()
        b1=Button(mpwin,text="ADD PRODUCT",font="30",bg=input_color,width=25,command=add_product).pack(pady=(20,0))
        b2=Button(mpwin,text="MODIFY PRODUCT",font=" 30",bg=input_color,width=25,command=upd_product).pack(pady=(20,0))
        b3=Button(mpwin,text="DELETE PRODUCT",font="30",bg=input_color,width=25,command=delete_product).pack(pady=(20,0))
        b4=Button(mpwin,text="DISPLAY ALL PRODUCT",font="30",bg=input_color,width=25,command=search_all).pack(pady=(20,0))
        b5=Button(mpwin,text="SEARCH PRODUCT",font="30",bg=input_color,width=25,command=search).pack(pady=(20,0))
        b6=Button(mpwin,text="BACK",font="5",bg=input_color,width=10,command=back).place(x=10,y=395)
        b7=Button(mpwin,text="EXIT",font="5",bg=input_color,width=10).place(x=290,y=395)

        mpwin.mainloop()
        #MAINTAIN_SALES
    def add_sale():
        mswin.withdraw()
        a_sale = Toplevel()

        def on_closing1q5():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                a_sale.withdraw()
                mswin.deiconify()

        a_sale.protocol("WM_DELETE_WINDOW", on_closing1q5)

        def backa_p():
            q=messagebox.askyesno("Warning","Your Data will be lost")
            if q==1:
                a_sale.withdraw()
                mswin.deiconify()

        w = 450
        h = 250
        ws = a_sale.winfo_screenwidth()
        hs = a_sale.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        a_sale.geometry('%dx%d+%d+%d' % (w, h, x, y))
        a_sale.config(bg=input_color)
        a_sale.resizable(0, 0)
        ord= Label(a_sale, text="         ADD ORDER", bg=input_color, font='boldUnderline 20', padx=30, pady=20).grid(
            row=0, column=0, columnspan=2)
        ord_id = Label(a_sale, text="PHONE NO:", bg=input_color, font='bold 15', pady=20, justify='left').grid(row=1,
                                                                                                              column=0,
                                                                                                              sticky='w')
        ord_name = Label(a_sale, text="CUSTOMER_NAME :", bg=input_color, font='bold 15', pady=20, justify='left').grid(
            row=2, column=0, sticky='w')

        var_nwumber = StringVar()
        ord_id1 = Entry(a_sale, justify="left", highlightcolor='#F24014', bg='#dbd9db', font='20',textvariable=var_nwumber)
        ord_id1.grid(row=1,column=1)
        def click(*args):
            ord_id1.delete(0, 'end')


        max_len1 = 10

        def on_wrwite1(*args):
            print(var_nwumber.get())
            s1 = var_nwumber.get()
            if len(s1) > max_len1:
                var_nwumber.set(s1[:max_len1])

        def callwback(i):
            if i.isdigit() or i == '':
                return True
            else:
                return False

        rweg = a_sale.register(callwback)
        var_nwumber.trace_variable("w", on_wrwite1)

        ord_id1.config(validate="all", validatecommand=(rweg, '%P'))

        ord_id1.insert(0, 'Enter Only Digits:- ')
        ord_id1.bind("<Button-1>", click)



        ord_id1.focus()
        ord_name1 = Entry(a_sale, justify="left", highlightcolor='#F24014', bg='#dbd9db', font='20')
        ord_name1.grid(row=2,   column=1)
        def click(*args):
            ord_name1.delete(0, 'end')

        ord_name1.insert(0, 'Enter Only Alphabets:- ')
        ord_name1.bind("<Button-1>", click)

        def callback(i):
            if i.isalpha() or i == '':
                return True

            else:
                return False

        reg = a_sale.register(callback)

        ord_name1.config(validate="all", validatecommand=(reg, '%P'))

        ord_name1.focus()
        s = '''SELECT order_number FROM inventory.order;'''
        status, error_msg, data = MySQL_Interface.Execute_Select(s)
        list121 = data
        def bingo(event):
            ord_ord=ord_id1.get()
            if [int(ord_ord)] in list121:
                print("hi")
        ord_id1.bind("Return",bingo)
        def submit15665():
            p=date.today()
            ord_id11 = ord_id1.get()
            ord_name11 = ord_name1.get()
         #   print(ord_id11)
            if ord_id11=='' or ord_name11=='' or ord_name11=='Enter Only Alphabets:- ' :
                messagebox.showwarning('Warning!', "Required field is empty")
            if len(ord_id11)<max_len1:
                messagebox.showwarning('Warning!', "Please Check the  Values")
            else:
                if ord_id11.isalpha()==True:
                    messagebox.showwarning("Warning","Entered Order Id is wrong! Only numbers allowed!")

                else:
                    poke='''SELECT order_number FROM inventory.order;'''
                    status,error_msg,dat3=MySQL_Interface.Execute_Select(poke)
                    pok = str(ord_id11[:1]) + str(int(ord_id11[1:2]) + 1) + str(int(ord_id11[2:3]) + 1) + str(
                        ord_name11[:3]) + str(p)
                    if [ord_id11] in dat3:
                        messagebox._show("Success", f"Order inserted succesfully\nYOUR ORDER NO IS:{pok}")
                        # naam ningal
                        trying.trying(pok)
                        a_sale.withdraw()
                    else:
                        s = f'''INSERT INTO inventory.order (order_number, Customer_name, Date_purchased) VALUES ('{pok}', '{ord_name11}' , '{p}');'''
                        l = [s]

                        status, error_msg = MySQL_Interface.Execute_IUD(l)
                        if status == True:
                            messagebox._show("Success", f"Order inserted succesfully\nYOUR ORDER NO IS:{pok}")
                            #naam ningal
                            a_sale.withdraw()
                            trying.trying(pok,menuwin)

                    a_sale.withdraw()
                    mswin.deiconify()


                        #dei inga daan continue pannanum




        submit = Button(a_sale, text="SUBMIT", font="5", bg=input_color, width=10, command=submit15665).place(x=335,
                                                                                                        y=210)
        exit = Button(a_sale, text="BACK", font="5", bg=input_color, width=10, command=backa_p).place(x=10, y=210)
        a_sale.mainloop()
#function for creating modification
    '''def upsd_sales():
        def upd1_product():
            mswin.withdraw()
            sale_pro = Tk()

            def back12():
                sale_pro.withdraw()
                mswin.deiconify()

            def backu1_p():
                q = messagebox.askyesno("Warning", "Your Data will be lost")
                if q == 1:
                    sale_pro.withdraw()
                    mswin.deiconify()

            def pro1_namee():
                sale_pro.withdraw()
                p1 = Tk()
                w = 400
                h = 190
                ws = p1.winfo_screenwidth()
                hs = p1.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                p1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                p1.config(bg=input_color)
                p1.resizable(0, 0)
                pro_id = Label(p1, text='Product Id', font='30', bg=input_color).grid(row=1, column=0, pady=30, padx=15)
                new_pro_name = Label(p1, text='Product Name', font='30', bg=input_color).grid(row=2, column=0, padx=15)
                s = select product_id from product ;.format()
                status, error_msg, data = MySQL_Interface.Execute_Select(s)
                list111 = data
                pro_id1 = ttk.Combobox(p1, value=list111, state='readonly', justify="left", font='30')
                pro_id1.grid(row=1, column=1)
                new_pro_name1 = Entry(p1, width=35)
                new_pro_name1.grid(row=2, column=1)

                def submit111():
                    pro_id11 = pro_id1.get()
                    new_pro_name11 = new_pro_name1.get()
                    s = update product set product_name='{}' where product_id={};.format(new_pro_name11,
                                                                                               (pro_id11))
                    o = [s]
                    sta = True
                    if new_pro_name11 == "":
                        sta = False
                        messagebox.showwarning('Warning!', "Required field is empty")
                    if sta != False:
                        status, error_msg = MySQL_Interface.Execute_IUD(o)
                        messagebox.showinfo("Succes", "Changed succesfully!")
                        p1.withdraw()
                        sale_pro.deiconify()

                sub1 = Button(p1, text='SUBMIT', borderwidth=5, font='bold 12', command=submit111).place(x=150, y=130)
                #            back1=Button(p,text='BACK',borderwidth=5,font='bold 15',command=submit11).place(x=10,y=130)

                p1.mainloop()

            w = 450
            h = 400
            ws = sale_pro.winfo_screenwidth()
            hs = sale_pro.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            sale_pro.geometry('%dx%d+%d+%d' % (w, h, x, y))
            sale_pro.config(bg=input_color)
            sale_pro.resizable(0, 0)
            upd = Label(sale_pro, text=" UPDATE PRODUCT", bg=input_color, font='boldUnderline 20').pack(padx=30, pady=20)
            pro_name = Button(sale_pro, text="PRODUCT_NAME ", bg=input_color, font='bold 15', width=20, command=pro1_namee).pack(
                padx=30, pady=20)
            qty_stk = Button(sale_pro, text="QUANTITY_IN_STOCK", bg=input_color, font='bold 15', width=20).pack(
                padx=30, pady=20)
            pro_rate = Button(sale_pro, text="PRODUCT_RATE ", bg=input_color, font='bold 15', width=20).pack(padx=30,
                                                                                                                       pady=20)

            back = Button(sale_pro, text="BACK", bg=input_color, font='bold 15', command=back12).place(x=200, y=350)

            sale_pro.mainloop()
            print("what problem")
    def u():
        mswin.withdraw()
        sale_pro=Tk()

        def back12():
            sale_pro.withdraw()
            mswin.deiconify()
        w = 450
        h = 400
        ws = sale_pro.winfo_screenwidth()
        hs = sale_pro.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        sale_pro.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sale_pro.config(bg=input_color)
        sale_pro.resizable(0, 0)
        upd = Label(sale_pro, text=" UPDATE PRODUCT", bg=input_color, font='boldUnderline 20').pack(padx=30, pady=20)
        pro_name = Button(sale_pro, text="PRODUCT_NAME ", bg=input_color, font='bold 15', width=20
                         ).pack(
            padx=30, pady=20)
        qty_stk = Button(sale_pro, text="QUANTITY_IN_STOCK", bg=input_color, font='bold 15', width=20).pack(
            padx=30, pady=20)
        pro_rate = Button(sale_pro, text="PRODUCT_RATE ", bg=input_color, font='bold 15', width=20).pack(padx=30,
                                                                                                         pady=20)

        back = Button(sale_pro, text="BACK", bg=input_color, font='bold 15', command=back12).place(x=200, y=350)

        sale_pro.mainloop()'''
    def diplay_sales():
        import tkinter as tk
        from tkinter import ttk
        from tkinter.messagebox import showinfo
        import MySQL_Interface
        roo21t = tk.Toplevel()
        roo21t.title('ORDER TABLE')

        def on_closing1q6():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                roo21t.withdraw()
                mswin.deiconify()

        roo21t.protocol("WM_DELETE_WINDOW", on_closing1q6)
        h = 240
        w = 620
        ws = roo21t.winfo_screenwidth()
        hs = roo21t.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        roo21t.geometry('%dx%d+%d+%d' % (w, h, x, y))
        roo21t.resizable(0, 0)

        # define columns
        columns = ('order_number', 'Customer_name', 'Date_purchased')

        tree = ttk.Treeview(roo21t, columns=columns, show='headings')

        # define headings
        tree.heading('order_number', text='ORDER NO')
        tree.heading('Customer_name', text='CUSTOMER NAME')
        tree.heading('Date_purchased', text='DATE')

        s10 = '''SELECT * FROM inventory.order;'''
        status, error_msg, data10 = MySQL_Interface.Execute_Select(s10)
        for contact in data10:
            tree.insert('', tk.END, values=contact)

        def item_selected(event):
            roo21t.withdraw()
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                s11 = f'''SELECT * FROM inventory.order_item where order_number='{record[0]}';;'''
                status, error_msg, data11 = MySQL_Interface.Execute_Select(s11)
                root1W = tk.Tk()
                root1W.title(f'ORDER NO: {record[0]}')
                h = 340
                w = 1220
                ws = root1W.winfo_screenwidth()
                hs = root1W.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                root1W.geometry('%dx%d+%d+%d' % (w, h, x, y))
                root1W.resizable(0, 0)

                # define columns
                columns = ('order_number', 'Item_number', 'Product_id', 'Quantity_purchased', 'Rate', 'Value')

                tree1W = ttk.Treeview(root1W, columns=columns, show='headings')

                # define headings
                tree1W.heading('order_number', text='ORDER NO')
                tree1W.heading('Item_number', text='ITEM NO')
                tree1W.heading('Product_id', text='PRODUCT ID')
                tree1W.heading('Rate', text='RATE')
                tree1W.heading('Value', text='VALUE')

                for contact in data11:
                    tree1W.insert('', tk.END, values=contact)
                tree1W.grid(row=0, column=0, sticky='nsew')

                # add a scrollbar
                scrollbar1W = ttk.Scrollbar(root1W, orient=tk.VERTICAL, command=tree1W.yview)
                tree1W.configure(yscroll=scrollbar1W.set)
                scrollbar1W.grid(row=0, column=1, sticky='ns')

                # run the app

                def on_closing():
                    root1W.withdraw()
                    roo21t.deiconify()

                root1W.protocol("WM_DELETE_WINDOW", on_closing)
                root1W.mainloop()

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(roo21t, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # run the app
        roo21t.mainloop()
    def searchee():
        mswin.withdraw()
        search_tk1 = Tk()
        w = 480
        h = 130
        ws = search_tk1.winfo_screenwidth()
        hs = search_tk1.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        search_tk1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        search_tk1.config(bg=input_color)
        search_tk1.resizable(0, 0)

        def on_closing12():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                search_tk1.withdraw()
                mswin.deiconify()

        search_tk1.protocol("WM_DELETE_WINDOW", on_closing12)

        product_ide = Label(search_tk1, text='CUSTOMER NAME', font='40', bg=input_color).grid(row=0, column=0, pady=30,
                                                                                             padx=15)
        dvs = '''SELECT Customer_name,order_number FROM inventory.order ;'''.format()
        status, error_msg, data = MySQL_Interface.Execute_Select(dvs)
        dvs1 = '''SELECT Customer_name FROM inventory.order ;'''.format()
        status, error_msg, listv21 = MySQL_Interface.Execute_Select(dvs1)
        fp9s = {}
        for i in data:
            fp9s[i[0]] = i[1]
        pro111_id21 = ttk.Combobox(search_tk1, value=listv21, justify="left", font='30')
        pro111_id21.grid(row=0, column=1)

        def submit56278():
            pro11121_id2 = pro111_id21.get()
            if pro11121_id2 == '':
                messagebox.showerror("Error", "No Data!!")
            else:
                search_tk1.withdraw()
                s = '''select * from order_item where order_number = '{}';'''.format(fp9s[(pro11121_id2)])
                status, error_msg, l123f = MySQL_Interface.Execute_Select(s)
                roo212t = tk.Tk()
                roo212t.focus_force()
                roo212t.title(pro11121_id2)
                h = 240
                w = 1220
                ws = roo212t.winfo_screenwidth()
                hs = roo212t.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                roo212t.geometry('%dx%d+%d+%d' % (w, h, x, y))
                roo212t.resizable(0, 0)

                def on_closing1():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        roo212t.withdraw()
                        mswin.deiconify()

                roo212t.protocol("WM_DELETE_WINDOW", on_closing1)
                # define columns
                columns = ('order_number', 'Item_number', 'Product_id', 'Quantity_purchased', 'Rate', 'Value')

                tree1W1 = ttk.Treeview(roo212t, columns=columns, show='headings')
                tree1W1.grid(row=0, column=0, sticky='nsew')
                # define headings
                tree1W1.heading('order_number', text='ORDER NO')
                tree1W1.heading('Item_number', text='ITEM NO')
                tree1W1.heading('Product_id', text='PRODUCT ID')
                tree1W1.heading('Rate', text='RATE')
                tree1W1.heading('Value', text='VALUE')

                for contact in l123f:
                    tree1W1.insert('', tk.END, values=contact)
                scrollbar = ttk.Scrollbar(roo212t, orient=tk.VERTICAL, command=tree1W1.yview)
                tree1W1.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')

        submit4256 = Button(search_tk1, text="SUBMIT", font="5", bg=input_color, width=10, command=submit56278).place(
                x=200, y=80)
        search_tk1.mainloop()


    def Maintain_sales():
        def backee():
            print("me")
            mswin.withdraw()
            menuwin.deiconify()
        global mswin
        menuwin.withdraw()
        mswin=Toplevel()

        def on_closing1q9():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                mswin.withdraw()
                menuwin.deiconify()

        mswin.protocol("WM_DELETE_WINDOW", on_closing1q9)
        w = 400
        h = 450
        ws = mswin.winfo_screenwidth()
        hs = mswin.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        mswin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        mswin.config(bg=input_color)
        mswin.resizable(0, 0)
        title = Label(mswin, text="MAINTAIN SALES",font="Helvectica 14", bg=input_color,pady=20).pack()
        b1=Button(mswin,text="ADD ORDER",font="30",bg=input_color,width=25,command=add_sale).pack(pady=(40,0))
   #     b2=Button(mswin,text="MODIFY ORDER",font=" 30",bg=input_color,width=25,command=u).pack(pady=(20,0))
     #   b3=Button(mswin,text="DELETE ORDER",font="30",bg=input_color,width=25).pack(pady=(20,0))
        b4=Button(mswin,text="DISPLAY ALL ORDER",font="30",bg=input_color,width=25,command=diplay_sales).pack(pady=(40,0))
        b5=Button(mswin,text="SEARCH ORDER",font="30",bg=input_color,width=25,command=searchee).pack(pady=(40,0))
        b6=Button(mswin,text="BACK",font="5",bg=input_color,width=10,command=backee).place(x=140,y=400)
#        b7=Button(mswin,text="EXIT",font="5",bg=input_color,width=10).place(x=290,y=395)

        mswin.mainloop()

    B()
sum()

