from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

con = pymysql.connect(host='localhost', user='root', password='zhn0946.', database="banksystem", )
cur = con.cursor()

# 管理员登陆
win_malogin = Tk()
win_malogin.geometry("380x120")
win_malogin.title("管理员登陆界面")
manager_frame = LabelFrame(win_malogin, text="管理员登陆", fg='red', font=("halvatica", 20, "bold"))
manager_frame.grid(row=6, column=1)
Label(manager_frame, text="管理员ID : ").grid(row=1, column=0)
Label(manager_frame, text="密码 : ").grid(row=2, column=0)

num = IntVar()
ps = StringVar()


def manager_loan():
    manager_num = Entry(manager_frame, width=30, textvariable=num).grid(row=1, column=1)
    pss = Entry(manager_frame, textvariable=ps, show='*', width=30).grid(row=2, column=1)

    # 连接数据库 查看管理员id与密码是否正确
    def check():
        # 输入框中的密码=pswd
        id = num.get()
        pswd = ps.get()
        pswd = str(pswd)
        try:
            query_manager = 'select * from manager where manager_id=%s'  # 在数据库中查询manager_id
            val = (id,)
            cur.execute(query_manager, val)
            b = cur.fetchone()
            # 查看id对应的密码是否与输入的相同
            if b[1] == pswd:
                print('管理员成功登陆！')
                mana_op()
                win_malogin.destroy()
            else:
                messagebox.showwarning('title', '密码错误！请重新输入！')

        except:
            messagebox.showwarning('title', '出错！请检查输入是否正确！')

    Button(manager_frame, text='提交', command=check, font=("Times New Roman", 12)).grid(row=7, column=1, sticky='e')


class Loan:

    def __init__(self, root):
        self.root = root
        self.root.title("贷款管理")
        self.root.geometry("1370x720")
        title = Label(self.root, text="贷款管理界面", font=("times new romman", 40, 'bold'), bd=10,
                      relief=GROOVE, bg='pink', fg='black')
        title.pack(side=TOP, fill=X)

        cur.execute("Select customer.name from loan,"
                    "customer,card  where customer.customer_id=card.customer_id and card.pincode=loan.pincode")
        self.name = cur.fetchone()

        self.loanId = StringVar()
        self.reason = StringVar()
        self.amount = StringVar()
        self.year = StringVar()
        self.rate = StringVar()
        self.pin = StringVar()
        self.mpay = StringVar()
        self.tpay = StringVar()
        self.cpay = StringVar()

        # 左侧输入信息
        Detail_F = Frame(self.root, bd=4, relief=RIDGE, )
        Detail_F.place(x=10, y=90, width=400, height=620)

        lbl_id = Label(Detail_F, text="贷款编号", font=("times new romman", 18, 'bold'))
        lbl_id.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        txt_id = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,
                       textvariable=self.loanId)
        txt_id.grid(row=0, column=1, pady=10, sticky="w")

        lbl_pin = Label(Detail_F, text="卡号", font=("times new romman", 18, 'bold'))
        lbl_pin.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_pin = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.pin)
        txt_pin.grid(row=1, column=1, pady=10, sticky="w")

        lbl_aa = Label(Detail_F, text="贷款原因", font=("times new romman", 18, 'bold'))
        lbl_aa.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_aa = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,
                       textvariable=self.reason)
        txt_aa.grid(row=2, column=1, pady=10, sticky="w")

        lbl_amount = Label(Detail_F, text="贷款金额", font=("times new romman", 18, 'bold'))
        lbl_amount.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_amount = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,
                           textvariable=self.amount)
        txt_amount.grid(row=3, column=1, pady=10, sticky="w")

        lbl_time = Label(Detail_F, text="年数", font=("times new romman", 18, 'bold'))
        lbl_time.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_time = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,
                         textvariable=self.year)
        txt_time.grid(row=4, column=1, pady=10, sticky="w")

        lbl_rate = Label(Detail_F, text="比率", font=("times new romman", 18, 'bold'))
        lbl_rate.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_rate = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, state=DISABLED,
                         textvariable=self.rate)
        txt_rate.grid(row=5, column=1, pady=10, sticky="w")

        lbl_Mp = Label(Detail_F, text="每月应偿还", font=("times new romman", 18, 'bold'))
        lbl_Mp.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Mp = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, state=DISABLED,
                       textvariable=self.mpay)
        txt_Mp.grid(row=6, column=1, pady=10, sticky="w")

        lbl_tp = Label(Detail_F, text="总共应偿还", font=("times new romman", 18, 'bold'))
        lbl_tp.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_tp = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, state=DISABLED,
                       textvariable=self.tpay)
        txt_tp.grid(row=7, column=1, pady=10, sticky="w")

        # 显示可贷金额
        lbl_cp = Label(Detail_F, text="可贷金额", font=("times new romman", 18, 'bold'))
        lbl_cp.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        txt_cp = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, state=DISABLED,
                       textvariable=self.cpay)
        txt_cp.grid(row=9, column=1, pady=10, sticky="w")

        # 右侧实时显示记录
        recordFrame = Frame(self.root, bd=5, relief=RIDGE)
        recordFrame.place(x=425, y=100, width=930, height=530)

        yscroll = Scrollbar(recordFrame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(recordFrame, columns=(
            "loan_id", "name", "pincode", "reason", "amount", "years", "rate", "Mpayment", "Tpayment", "date")
                                           , yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.employee_table.yview)

        self.employee_table.heading("loan_id", text="贷款号")
        self.employee_table.heading("name", text="姓名")
        self.employee_table.heading("pincode", text="卡号")
        self.employee_table.heading("reason", text="贷款原因")
        self.employee_table.heading("amount", text="贷款金额")
        self.employee_table.heading("years", text="年数")
        self.employee_table.heading("rate", text="比率")
        self.employee_table.heading("Mpayment", text="月偿还")
        self.employee_table.heading("Tpayment", text="共偿还")
        self.employee_table.heading("date", text="日期")

        self.employee_table['show'] = 'headings'

        self.employee_table.column("loan_id", width=50)
        self.employee_table.column("name", width=60)
        self.employee_table.column("pincode", width=60)
        self.employee_table.column("reason", width=50)
        self.employee_table.column("amount", width=70)
        self.employee_table.column("years", width=45)
        self.employee_table.column("rate", width=50)
        self.employee_table.column("Mpayment", width=70)
        self.employee_table.column("Tpayment", width=80)
        self.employee_table.column("date", width=120)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.fatch_data()
        #  self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)

        # 按键设置
        btnFrame = Frame(self.root, bd=5, relief=RIDGE)
        btnFrame.place(x=425, y=630, width=930, height=80)

        btn1 = Button(btnFrame, text='增加记录', font='arial 18 bold', bg='lime', fg='crimson', width=9,
                      command=self.add_record)
        btn1.grid(row=0, column=1, padx=10, pady=10)

        btn3 = Button(btnFrame, text='删除记录', font='arial 18 bold', bg='lime', fg='crimson', width=9,
                      command=self.delete)
        btn3.grid(row=0, column=2, padx=8, pady=10)

        btn4 = Button(btnFrame, text='重置', font='arial 18 bold', bg='lime', fg='crimson', width=9,
                      command=self.reset)
        btn4.grid(row=0, column=3, padx=8, pady=10)

        btn5 = Button(btnFrame, text='退出', font='arial 18 bold', bg='lime', fg='crimson', width=9,
                      command=self.exit)
        btn5.grid(row=0, column=4, padx=7, pady=10)

    def total(self):

        n = int(self.year.get())
        # 根据年份判断比率
        if n >= 5:
            if n <= 20:
                self.rate.set(0.049)
            else:
                self.rate.set(0.079)
        else:
            self.rate.set(0.02)
        # 计算月供和总供
        p = float(self.amount.get())
        r = float(self.rate.get())
        t = (p * r * n * 12) / 100
        m = (p + t) / (n * 12)
        self.mpay.set(str(round(m, 2)))
        self.tpay.set(str(t + p))

    # 在右边显示记录
    def fatch_data(self):
        cur.execute("Select loan_id,customer.name,loan.pincode,reason,amount,years,rate,Mpayment,Tpayment,date from "
                    "loan,customer,card  where customer.customer_id=card.customer_id and card.pincode=loan.pincode")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())

            for row in rows:
                self.employee_table.insert('', END, values=row)
        con.commit()

    # 增加一条记录
    def add_record(self):

        cur.execute("Select * from loan where loan_id=%s", self.loanId.get())
        rows = cur.fetchone()
        if rows is None:
            self.total()
            cur.execute("Select * from card where pincode=%s", self.pin.get())
            result_p = cur.fetchone()

            if result_p[2] == "信用卡":
                depo = float(result_p[1])
                value = depo - float(self.tpay.get())
                value = str(value)

                cc = float(result_p[6]) * 500
                self.cpay.set(str(cc))
                if float(self.amount.get()) <= cc:
                    # 更新card余额和信用值 设定信用值=原本信用值-贷款金额*0.0005
                    credit = float(result_p[6]) - float(self.tpay.get()) * 0.0005
                    credit = int(credit)
                    credit = str(credit)
                    cur.execute("update card set deposit=%s,credit=%s  where pincode=%s",
                                (value, credit, self.pin.get()))
                    con.commit()

                    cur.execute("insert into loan values(%s,%s,%s,%s,%s,%s,%s,%s,%s,now(),null)", (
                        self.loanId.get(),
                        self.reason.get(),
                        self.amount.get(),
                        self.year.get(),
                        self.rate.get(),
                        self.mpay.get(),
                        self.tpay.get(),
                        num.get(),
                        self.pin.get()))
                    con.commit()
                    self.fatch_data()
                else:
                    messagebox.showwarning('error', '超出可贷款金额！')



    def delete(self):
        # 找到card中余额大于0 且办理了贷款的信用卡
        cur.execute("select loan.loan_id from card,loan where card.pincode=loan.pincode and card.deposit>=0")
        re = cur.fetchall()

        for i in range(len(re)):
            cur.execute("delete from loan where loan.loan_id=%s ", re[i])
            con.commit()

        self.fatch_data()
        self.reset()

    # 重置
    def reset(self):
        self.loanId.set('')
        self.pin.set('')
        self.reason.set('')
        self.amount.set('')
        self.year.set('')
        self.rate.set('')
        self.mpay.set('')
        self.tpay.set('')

    def exit(self):
        self.root.destroy()


def select1():
    win_select = Tk()
    win_select.geometry("820x740")
    win_select.title("查询客户信息")
    a = Label(win_select, text="查询界面", font=("times new romman", 40, 'bold'), bd=10,
              relief=GROOVE, bg='pink', fg='black')
    a.pack(side=TOP, fill=X)

    conframe = Frame(win_select, bd=4, relief=RIDGE)
    conframe.place(x=10, y=90, width=800, height=60)

    # 选择查询条件种类
    oper = StringVar()
    options = ttk.Combobox(conframe, width=10, textvariable=oper)
    options['values'] = ("姓名", "卡号", "个人ID", "电话号码")
    options.place(width=100, height=50)
    options.current(0)

    # 查询条件输入
    select_con = StringVar()
    c = Entry(conframe, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE, textvariable=select_con)
    c.place(x=120, width=550, height=50)

    # 下侧显示记录
    recordframe = Frame(win_select, bd=5, relief=RIDGE)
    recordframe.place(x=10, y=160, width=800, height=550)
    ysc = Scrollbar(recordframe, orient=VERTICAL)
    cus_information = ttk.Treeview(recordframe, columns=(
        "customer_id", "name", "pincode", "deposit", "bank_name", "credit",))
    ysc.pack(side=RIGHT, fill=Y)
    ysc.config(command=cus_information.yview)
    cus_information.heading("customer_id", text="用户个人ID")
    cus_information.heading("name", text="姓名")
    cus_information.heading("pincode", text="卡号")
    cus_information.heading("deposit", text="卡内余额")
    cus_information.heading("bank_name", text="银行")
    cus_information.heading("credit", text="信用")

    cus_information['show'] = 'headings'

    cus_information.column("customer_id", width=100)
    cus_information.column("name", width=100)
    cus_information.column("pincode", width=100)
    cus_information.column("deposit", width=120)
    cus_information.column("bank_name", width=100)
    cus_information.column("credit", width=100)
    cus_information.pack(fill=BOTH, expand=1)

    # 记录显示
    def show():
        global result
        chooose_condition = oper.get()

        if chooose_condition == "姓名":
            cur.execute(
                "select distinct customer.customer_id,customer.name,card.pincode,card.deposit,card.bank_name,"
                "card.credit from customer,card where customer.customer_id=card.customer_id  and "
                " customer.name like '%%%s%%'  "
                % select_con.get())
            result = cur.fetchall()

        if chooose_condition == "卡号":
            select_con0 = int(select_con.get())
            cur.execute(
                "select distinct customer.customer_id,customer.name,card.pincode,card.deposit,card.bank_name,"
                "card.credit from customer,card where customer.customer_id=card.customer_id and "
                "  card.pincode like '%%%s%%' "
                % select_con0)
            result = cur.fetchall()

        if chooose_condition == "个人ID":
            select_con1 = int(select_con.get())
            cur.execute(
                "select distinct customer.customer_id,customer.name,card.pincode,card.deposit,card.bank_name,"
                "card.credit from customer,card where customer.customer_id=card.customer_id  and "
                "customer.customer_id like '%%%s%%' "
                % select_con1)
            result = cur.fetchall()

        if chooose_condition == "电话号码":
            select_con2 = int(select_con.get())
            cur.execute(
                "select distinct customer.customer_id,customer.name,card.pincode,card.deposit,card.bank_name,"
                "card.credit from customer,card,loan where customer.customer_id=card.customer_id and "
                " customer.mobile like '%%%s%%'  "
                % select_con2)
            result = cur.fetchall()

        if len(result) != 0:
            cus_information.delete(*cus_information.get_children())

            for res in result:
                cus_information.insert('', END, values=res)
        con.commit()

    select_button = Button(conframe, text='查询', font='arial 18 bold', bg='lime', command=show)
    select_button.place(x=700, width=70)


def mana_op():
    def obj():
        win_loan = Tk()
        obj = Loan(root=win_loan)

    win_managerchoose = Tk()
    win_managerchoose.geometry("450x430")
    win_managerchoose.title("管理员操作界面")
    title1 = Label(win_managerchoose, text='管理员，你好！', fg="black")
    title1.grid(row=1, column=1, padx=100)
    Label.config(title1, font=("Times New Roman", 30, "bold"))

    loan_button = Button(win_managerchoose, text='办理贷款', command=obj, width=15, height=2, fg="black",
                         font=("halvatica", 20, "bold"))
    loan_button.grid(row=3, column=1, padx=5, pady=40)

    select_button = Button(win_managerchoose, text='查询操作', command=select1, width=15, height=2, fg="black",
                           font=("halvatica", 20, "bold"))
    select_button.grid(row=5, column=1, padx=5, pady=40)


manager_loan()
win_malogin.mainloop()
