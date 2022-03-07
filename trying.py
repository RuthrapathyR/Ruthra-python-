from tkinter import *
import random
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import ttk
import MySQL_Interface  # first line of your code
from tkinter import messagebox
import MySQL_Interface
from datetime import date
import tkinter as tk
from PIL import Image
from PIL import ImageTk

snp9 = 1
contactsp9 = []
pic = []
po = 0

kug = ''
def trying(item7):
    sp91 = '''SELECT product_name,Quantity_in_stock FROM inventory.product;'''
    status, error_msg, data = MySQL_Interface.Execute_Select(sp91)
    fp9 = {}
    for i in data:
        fp9[i[0]] = i[1]
    print(fp9)
    sdp9 = '''SELECT product_name,product_id FROM inventory.product;'''
    statusp9, error_msgp9, datap9 = MySQL_Interface.Execute_Select(sdp9)
    fdp9 = {}
    for i in datap9:
        fdp9[i[0]] = i[1]
    print(fdp9)
    sqp9 = '''SELECT product_name,Quantity_in_stock FROM inventory.product;'''
    status, error_msg, data = MySQL_Interface.Execute_Select(sqp9)
    fqp9 = {}
    for i in data:
        fqp9[i[0]] = i[1]
    sssp9 = '''SELECT product_name,rate FROM inventory.product;'''
    status, error_msg, data = MySQL_Interface.Execute_Select(sssp9)
    rutp9 = {}
    for i in data:
        rutp9[i[0]] = i[1]
    ikalp9 = rutp9.keys()
    potatop9 = []
    for t in ikalp9:
        potatop9.append(t)

    rootp9 = Toplevel()
    rootp9.title("bill slip")
    # root.geometry('1366x708')
    h = 620
    w = 1363
    ws = rootp9.winfo_screenwidth()
    hs = rootp9.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    rootp9.geometry('%dx%d+%d+%d' % (w, h, x, y))
    rootp9.resizable(0, 0)
    bg_color = '#4D0039'
    bg1_color = '#EC6710'
    rootp9.config(bg=bg1_color)
    # ======================variable=================
    c_namep9 = StringVar()
    c_phonep9 = StringVar()
    itemp9 = StringVar()
    Ratep9 = IntVar()
    quantityp9 = IntVar()
    bill_nop9 = StringVar()
    xp9 = random.randint(1000, 9999)
    bill_nop9.set(str(x))

    global lp9
    lp9 = []

    # =========================Functions================================

    def gbillp9():
        usufp9 = []
        wp9 = 1
        for line in treep9.get_children():
            usufp9.append(treep9.item(line)["values"])
        for icep9 in usufp9:
            print(icep9)
            gp9 = item7
            print('p',int(fdp9[icep9[0]]))
            sfgp9 = '''insert into inventory.order_item(order_number, Item_number, Product_id, Quantity_purchased, Rate, Value)
            values('{}',{},{},{},{},{})'''.format(gp9, wp9, int(fdp9[icep9[0]]), int(icep9[2]), float(icep9[1]),
                                                  float(icep9[3]))
            ahg = '''update product set quantity_in_stock = quantity_in_stock - {} where product_id = {};'''.format(
                int(icep9[2]), int(fdp9[icep9[0]]))

            l4 = [sfgp9]
            l4.append(ahg)
            status, error_msg = MySQL_Interface.Execute_IUD(l4)
            if status == False:
                print(error_msg)
            else:
                messagebox.showinfo("SUCCESS", "YOUR ORDER ENTERED SUCCESSFULLY")
            wp9 = wp9 + 1

    def exit():
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            rootp9.destroy()

    '''title=Label(root,pady=2,text="Billing Software",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
    title.pack(fill=X)
    '''
    # =================Product Frames=================

    F2 = LabelFrame(rootp9, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold', bg=bg_color)
    F2.place(x=5, y=10, width=550, height=600)

    itmp9 = Label(F2, text='Product Name', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=0, column=0, padx=0, pady=20)

    wp92 = ''

    def price_setp9(event):
        xp9 = str(itm_txtp9.get())
        print(xp9)
        wp92 = rutp9[xp9]
        print(wp92)
        rate_txtp9.config(state=NORMAL)
        rate_txtp9.delete(0, END)
        rate_txtp9.insert(0, wp92)
        rate_txtp9.config(state=DISABLED)
        if n_txtp9.get() == '':
            pass
        else:
            r_txtp91 = Label(F2, width=23, text=rupees + str(int(n_txtp9.get()) * float(wp92)), font='arial 15 bold',
                             justify="left")
            r_txtp91.grid(row=3, column=1, padx=5, pady=20)

    def price_stp9():
        x4 = str(itm_txtp9.get())
        wp93 = rutp9[x4]
        rate_txtp9.config(state=NORMAL)
        rate_txtp9.delete(0, END)
        rate_txtp9.insert(0, wp93)
        rate_txtp9.config(state=DISABLED)
        if n_txtp9.get() == '':
            pass
        else:
            r_txtp92 = Label(F2, width=23, text=rupees + str(int(n_txtp9.get()) * float(wp93)), font='arial 15 bold',
                             justify="left")
            r_txtp92.grid(row=3, column=1, padx=5, pady=20)

    itm_txtp9 = ttk.Combobox(F2, value=potatop9, width=22, font='arial 15 bold')
    # itm_txt.set('rice ponni 25kg')

    # itm_txt.bind('<<ComboboxSelected>>', rate_set)
    itm_txtp9.bind('<<ComboboxSelected>>', price_setp9)
    rate_txtp9 = Entry(F2, width=23, font='arial 15 bold', bd=7, state=DISABLED, disabledforeground='black',
                       disabledbackground="white")

    itm_txtp9.grid(row=0, column=1, padx=10, pady=20)

    rate_txtp9.grid(row=1, column=1, padx=5, pady=20)

    ratep9 = Label(F2, text='Product Rate', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=1, column=0, padx=0, pady=20)
    # here to text
    # rate_txt = Label(F2, width=25,textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=5,pady=20)

    np9 = Label(F2, text='Product Quantity', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=2, column=0, padx=0, pady=20)
    var_ph11p91 = StringVar()
    # to enter  number of quantity
    n_txtp9 = Entry(F2, width=25, textvariable=var_ph11p91, font='arial 15 bold', relief=SUNKEN, bd=7)
    # here
    rupees = u"\u20B9"

    max_len = 10
    r1_txtp9 = Label(F2, width=23, text=rupees, font='arial 15 bold', justify="left")
    r1_txtp9.grid(row=3, column=1, padx=5, pady=20)

    print(var_ph11p91.get())
    print("hi")
    def on_writep9(*args):
        global kug
        sp9 = var_ph11p91.get()
        print("s",sp9)
        thambi = (str(itm_txtp9.get()))
        sss = f'''SELECT Quantity_in_stock FROM inventory.product where product_name='{thambi}';'''
        #   print(sss)
        status, error_msg, data = MySQL_Interface.Execute_Select(sss)
        #  print(data)
        datum = []
        for i in data:
            a = i.pop()
            datum.append(a)
        #  print(int(datum[0]))
        if sp9.isdigit() and len(sp9) <= max_len and rate_txtp9.get() != '':
            rate_11txtp9 = float(rate_txtp9.get())
            kug = str(int(sp9) * rate_11txtp9)
            print('kug',kug)
            r_txtp94 = Label(F2, width=23, text=rupees + str(int(sp9) * rate_11txtp9), font='arial 15 bold',
                             justify="left")
            r_txtp94.grid(row=3, column=1, padx=5, pady=20)
        if sp9 == '':
            r_txtp96 = Label(F2, width=23, text=rupees, font='arial 15 bold', justify="left")
            r_txtp96.grid(row=3, column=1, padx=5, pady=20)
        #   if s=='9':
        #   r1_txt = Label(F2, width=23, text=rupees , font='arial 15 bold', justify="left")
        #   r1_txt.grid(row=3, column=1, padx=5, pady=20)
        # wan to do this
        '''
        2
        '''
        if len(sp9) > max_len:
            var_ph11p91.set(sp9[:max_len])
        if sp9 != "":
            if int(sp9) > fp9[thambi]:
                #     print("here it executes the logic")  # here1

                #      var_ph11.set(str(fp9[thambi]-1))
                n_txtp9.delete(0, END)
                n_txtp9.insert(0, str(fp9[thambi] - 1))

                if fp9[thambi] == 0:
                    r_txwt = Label(F2, width=23, text=rupees + (0 * rate_11txtp9), font='arial 15 bold', justify="left")
                    r_txwt.grid(row=3, column=1, padx=5, pady=20)
                else:
                    r_txt = Label(F2, width=23, text=rupees + str(abs((fp9[thambi]) - 1) * rate_11txtp9),
                                  font='arial 15 bold',
                                  justify="left")
                    r_txt.grid(row=3, column=1, padx=5, pady=20)
                messagebox.showwarning("Warning", "Required Product is Out Of Stock")

    def callback(it):
        if it.isdigit() or it == '':
            return True
        else:
            return False

    regp9 = F2.register(callback)
    var_ph11p91.trace_variable("w", on_writep9)
    n_txtp9.focus()
    n_txtp9.config(validate="all", validatecommand=(regp9, '%P'))
    n_txtp9.grid(row=2, column=1, padx=5, pady=20)

    rp95 = Label(F2, text='Total Cost', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=3, column=0, padx=0, pady=20)

    # price_st()
    # ========================Bill area================
    F3 = LabelFrame(rootp9, bd=10, relief=GROOVE, text='Bill Box', font=('times new romon', 15, 'bold'), fg='gold',
                    bg=bg_color)
    F3.place(x=562, y=10, width=790, height=600)

    rgf = 0

    # tre view sn
    '''F31 = LabelFrame(root, bd=10, relief=GROOVE, text='Bill Box', font=('times new romon', 15, 'bold'), fg='gold',
                    bg=bg_color)
    F31.place(x=545, y=90, width=30, height=600)
    '''  # define columns
    columnsp9 = ('product_name', 'product_rate', 'product_quantity', 'value')
    colp9 = ('serial_no',)
    treep9 = ttk.Treeview(F3, columns=columnsp9, show='headings')
    tree1p9 = ttk.Treeview(F3, columns=colp9, show='headings')
    sn = 0
    # define headings
    tree1p9.column("serial_no", width=26)
    treep9.column("product_name", width=220)
    treep9.column("product_rate", width=120)
    treep9.column("product_quantity", width=130)
    treep9.column("value", width=100)

    treep9.heading('product_name', text='NAME')
    tree1p9.heading('serial_no', text='S NO:')
    '''tree.tag_configure('oddrow', background='orange')
    tree.tag_configure('evenrow', background='purple')'''
    treep9.heading('product_rate', text='RATE')
    treep9.heading('product_quantity', text='QUANTITY')
    treep9.heading('value', text='VALUE')
    treep9.configure(height=60)
    scrollbarp9 = ttk.Scrollbar(rootp9, orient=VERTICAL, command=treep9.yview)
    treep9.configure(yscroll=scrollbarp9.set)

    def additm():
        global snp9, contactsp9, f, pic, sp9, po, rgf,kug,contactsp9
        u = []

        for line in treep9.get_children():
            u.append(treep9.item(line)["values"])

        # print(u)
        # print('f dict',f)
        treep9.pack()
        tree1p9.pack()
        tree1p9.place(x=6, y=5, width=36, height=600)
        treep9.place(x=42, y=5, width=730, height=600)
        thambi = (str(itm_txtp9.get()))
        if str(itm_txtp9.get()) == '' or rutp9[str(itm_txtp9.get())] == '' or str(n_txtp9.get()) == '' or str(
                kug) == '' or str(
                n_txtp9.get()) == '0':
            print('yes')
            print(itm_txtp9.get())
            print(rutp9[str(itm_txtp9.get())])
            print(n_txtp9.get())
            print(kug)
            print('n_txtp9',n_txtp9.get())
            messagebox.showwarning('WARNING', "All Fields Are Mandatory")

        else:
            try:
                l.pack_forget()
            except:
                pass

            if int(n_txtp9.get()) >= fp9[thambi]:
                if sp9 != "":
                    if fp9[thambi] > 0:
                        #     print("l",fp9[thambi])
                        #   print('s',int((var_ph11.get())))
                        if int((var_ph11p91.get())) > int(fp9[thambi]):
                            n_txtp9.delete(0, END)
                            n_txtp9.insert(0, str(fp9[thambi]))
                            rate_11txtp95 = float(rate_txtp9.get())
                            #       print(rate_11txt)
                            if fp9[thambi] == 0:
                                r_txwtp5 = Label(F2, width=23, text=rupees + (0 * rate_11txtp95), font='arial 15 bold',
                                                 justify="left")
                                r_txwtp5.grid(row=3, column=1, padx=5, pady=20)
                            else:
                                r_txtp7 = Label(F2, width=23, text=rupees + str(((fp9[thambi]) - 1) * rate_11txtp95),
                                                font='arial 15 bold',
                                                justify="left")
                                r_txtp7.grid(row=3, column=1, padx=5, pady=20)
                            messagebox.showwarning("Warning", "Required Product is Out Of Stock")
                    else:
                        messagebox.showwarning("Warning", "Required Product is Out Of Stock")
            else:
                thambi1 = (str(itm_txtp9.get()))
            print('p',contactsp9)
            try:
                contactsp9.clear()
                contactsp9.append((str(itm_txtp9.get()), rutp9[str(itm_txtp9.get())], str(n_txtp9.get()), str(kug)))
                pic.append((str(itm_txtp9.get()), rutp9[str(itm_txtp9.get())], str(n_txtp9.get()), str(kug)))

            except KeyError:
                pass

            try:
                for i in u:
                    print(i)
                    if i[0] == thambi1:
                        i[2] = i[2] + int(n_txtp9.get())
                        i[3] = float(i[3]) * (i[2])
                        po = True
                if po == True:
                    treep9.delete(*treep9.get_children())
                    for contact in u:
                        treep9.insert('', END, values=contact)
                        thambi = u[0][0]
                        print(thambi)
                    po = False
                else:
                    for contact in contactsp9:
                        sn = len(u) + 1
                        treep9.insert('', END, values=(contact))
                        tree1p9.insert('', END, values=([sn]))
            except UnboundLocalError:
                pass
        # print('f first ',f)
        u1 = []
        for line in treep9.get_children():
            u1.append(treep9.item(line)["values"])
        try:
            fp9[thambi1] = fp9[thambi1] - int(n_txtp9.get())
        except UnboundLocalError:
            pass
        for i in fp9:
            if fp9[i] <= 0:
                fp9[i] = 0

    #   print("first",f)
    # print("f in add_tiem",f)
    # print("pic",pic)
    def edit1():
        ud = []
        for line in treep9.get_children():
            ud.append(treep9.item(line)["values"])
        if ud == []:
            messagebox.showwarning("OOPS", "NO DATA TO EDIT")
        else:
            global f, editonly, pic
            columnsp7 = ('product_name', 'product_rate', 'product_quantity', 'value')
            tree2p7 = ttk.Treeview(F3, columns=columnsp7, show='headings')
            # define headings
            tree2p7.column("product_name", width=220)
            tree2p7.column("product_rate", width=120)
            tree2p7.column("product_quantity", width=130)
            tree2p7.column("value", width=100)

            tree2p7.heading('product_name', text='NAME')
            '''tree.tag_configure('oddrow', background='orange')
            tree.tag_configure('evenrow', background='purple')'''
            tree2p7.heading('product_rate', text='RATE')
            tree2p7.heading('product_quantity', text='QUANTITY')
            tree2p7.heading('value', text='VALUE')
            tree2p7.configure(height=60)
            scrollbarp7 = ttk.Scrollbar(rootp9, orient=VERTICAL, command=tree2p7.yview)
            tree2p7.configure(yscroll=scrollbarp7.set)
            scrollbarp7.grid(row=0, column=1, sticky='ns')
            sn = 0
            tree2p7.grid(row=0, column=1, sticky='nsew')
            tree1p9.grid(row=0, column=0, sticky='nsew')
            tree1p9.place(x=6, y=5, width=36, height=600)
            tree2p7.place(x=42, y=5, width=730, height=600)
            u = []
            for line in treep9.get_children():
                u.append(treep9.item(line)["values"])
            for contact in u:
                tree2p7.insert('', END, values=contact)
            F4 = LabelFrame(rootp9, fg=bg_color, bg=bg_color)
            F4.place(x=5, y=380, width=550, height=230)
            sn = 0
            editonly = True

            def edit2():
                global sn, thambi, sister, pic
                # Get selected item to Edit
                if str(itm_txtp9.get()) == '' or rutp9[str(itm_txtp9.get())] == '' or str(n_txtp9.get()) == '' or str(
                        kug) == '' or str(
                        n_txtp9.get()) == '0':
                    messagebox.showwarning('WARNING', "All Fields Are Mandatory")
                else:

                    fp9[thambi] = fqp9[thambi] - int(n_txtp9.get())
                    selected_item = tree2p7.selection()[0]
                    # contacts = [(str(itm_txt.get()), rut[str(itm_txt.get())], str(n_txt.get()), str(kug))]
                    tree2p7.item(selected_item, text="blub", values=(
                    (str(itm_txtp9.get()), rutp9[str(itm_txtp9.get())], str(n_txtp9.get()), str(kug))))

            #   print(f)

            def item_selected(event):
                global f, thambi, sister
                for selected_item in tree2p7.selection():
                    sister = int(n_txtp9.get())
                    thambi = (str(itm_txtp9.get()))
                    item = tree2p7.item(selected_item)
                    #   print("item",item)
                    record = item['values']
                    #  print("record", record)
                    itm_txtp9.set(record[0])
                    rate_txtp9.config(state=NORMAL)
                    rate_txtp9.delete(0, END)
                    rate_txtp9.insert(0, record[1])
                    rate_txtp9.config(state=DISABLED)
                    # here we

                    sn = '''SELECT product_name,Quantity_in_stock FROM inventory.product;'''
                    status, error_msg, data = MySQL_Interface.Execute_Select(sn)
                    fr = {}
                    for i in data:
                        fr[i[0]] = i[1]
                    fp9[thambi] = fr[thambi]
                    n_txtp9.delete(0, END)
                    n_txtp9.insert(0, record[2])

            tree2p7.bind('<<TreeviewSelect>>', item_selected)

            def back1x():
                F5 = LabelFrame(rootp9, fg=bg_color, bg=bg_color)
                F5.place(x=5, y=380, width=550, height=230)
                treep9.delete(*treep9.get_children())
                u = []
                for line in tree2p7.get_children():
                    u.append(tree2p7.item(line)["values"])
                tree2p7.destroy()
                for contact in u:
                    treep9.insert('', END, values=contact)
                treep9.grid(row=0, column=1, sticky='nsew')
                treep9.place(x=42, y=5, width=730, height=600)
                bttn1p9 = Button(F5, text='Add item', font='arial 15 bold', command=additm, bg='lime', width=15)
                bttn1p9.grid(row=4, column=0, padx=10, pady=30)
                bttn21p9 = Button(F5, text='Generate Bill', font='arial 15 bold', command=gbillp9, bg='lime',
                                  width=15)
                bttn21p9.grid(row=4, column=1, padx=10, pady=30)
                bttn3p9 = Button(F5, text='Edit', font='arial 15 bold', padx=5, pady=10, command=edit1, bg='lime',
                                 width=15)
                bttn3p9.grid(row=5, column=0, padx=10, pady=30)
                bttn4p9 = Button(F5, text='Exit', font='arial 15 bold', padx=5, pady=10, command=exit, bg='lime',
                                 width=15)
                bttn4p9.grid(row=5, column=1, padx=(45, 0), pady=30)

            btn5p9 = Button(F4, text='EDIT', font='arial 15 bold', command=edit2, padx=5, pady=10, bg='lime', width=15)
            btn5p9.grid(row=4, column=0, padx=(10, 90), pady=100)
            btn6p9 = Button(F4, text='BACK', font='arial 15 bold', command=back1x, padx=5, pady=10, bg='lime', width=15)
            btn6p9.grid(row=4, column=1, padx=10, pady=30)
            btn1p9.pack_forget()

    # =========================Buttons======================
    btn1p9 = Button(F2, text='Add item', font='arial 15 bold', command=additm, padx=5, pady=10, bg='lime', width=15)
    btn1p9.grid(row=4, column=0, padx=10, pady=30)
    btn2p9 = Button(F2, text='Generate Bill', font='arial 15 bold', command=gbillp9, padx=5, pady=10, bg='lime',
                    width=15)
    btn2p9.grid(row=4, column=1, padx=(45, 0), pady=30)
    btn3p9 = Button(F2, text='Edit', font='arial 15 bold', padx=5, pady=10, command=edit1, bg='lime', width=15)
    btn3p9.grid(row=5, column=0, padx=10, pady=30)
    btn4p9 = Button(F2, text='Exit', font='arial 15 bold', padx=5, pady=10, command=exit, bg='lime', width=15,
                    borderwidth=0)
    btn4p9.grid(row=5, column=1, padx=(45, 0), pady=30)

    rootp9.mainloop()