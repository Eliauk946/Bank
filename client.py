import random
import hashlib
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as m_box
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='zhn0946.', database="banksystem", )
cursor = conn.cursor()

# 初始窗口设置
win = Tk()
win.geometry("800x500")
win.title("欢迎来到银行系统")


# 创建一个账户
def create():
    win_create = Toplevel(win)
    win_create.geometry("490x390")
    win_create.title("创建账户")

    create_frame = LabelFrame(win_create, text='创建账户', fg="red", bd=5, height=15,
                              font=("Helvetica", 40, "bold"))
    create_frame.grid(row=5, column=2, pady=2)

    Label(create_frame, text='设置专属ID：').grid(row=2, column=1)
    Label(create_frame, text='姓名 : ').grid(row=3, column=1)
    Label(create_frame, text='出生日期: ').grid(row=4, column=1)
    Label(create_frame, text='住址 : ').grid(row=5, column=1)
    Label(create_frame, text='电话号码 : ').grid(row=6, column=1)
    Label(create_frame, text='Email : ').grid(row=7, column=1)
    # Label(create_frame, text='操作 : ').grid(row=9, column=1)
    Label(create_frame, text='性别 : ').grid(row=8, column=1)
    # Label(create_frame, text='设置密码: ').grid(row=11, column=1)
    # actype = StringVar()
    # Radiobutton(create_frame, text="Saving", variable=actype, value="SAVING").grid(row=9, column=2, sticky="w")
    # Radiobutton(create_frame, text="Current", variable=actype, value="CURRENT").grid(row=9, columnspan=3)

    cus_id = IntVar()
    a1 = Entry(create_frame, width=40, textvariable=cus_id)
    a1.grid(row=2, column=2, sticky="w")

    cus_name = StringVar()
    a2 = Entry(create_frame, width=40, textvariable=cus_name)
    a2.grid(row=3, column=2, sticky="w")

    cus_birth = StringVar()
    a3 = Entry(create_frame, width=40, textvariable=cus_birth)
    a3.grid(row=4, column=2, sticky="w")

    cus_add = StringVar()
    a4 = Entry(create_frame, width=40, textvariable=cus_add)
    a4.grid(row=5, column=2, sticky="w")

    cus_phone = StringVar()
    a5 = Entry(create_frame, width=40, textvariable=cus_phone)
    a5.grid(row=6, column=2, sticky="w")

    cus_em = StringVar()
    a6 = Entry(create_frame, width=40, textvariable=cus_em)
    a6.grid(row=7, column=2, sticky="w")

    gender = StringVar()
    options = ttk.Combobox(create_frame, width=10, textvariable=gender)
    options['values'] = ("男", "女")
    options.grid(row=8, column=2, sticky="w")
    options.current(0)

    def sub():
        cursor.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s)",
                       (cus_id.get(), cus_name.get(), cus_birth.get(), cus_add.get(), cus_phone.get(), cus_em.get(),
                        gender.get()))
        conn.commit()
        m_box.showinfo('创建成功！', "用户创建成功！接下来请您办理自己的银行卡！")
        win_create.destroy()

    Button(create_frame, text="提交", command=sub).grid(row=12, column=1, padx=10)
    Button(create_frame, text='退出', command=lambda: win_create.destroy()).grid(row=12, column=2, padx=10)


# 办理银行卡
def create_card():
    win_create_card = Toplevel(win)
    win_create_card.geometry("500x390")
    win_create_card.title("办理银行卡")
    card_frame = LabelFrame(win_create_card, text='办理银行卡', fg="red", bd=5, height=15,
                            font=("Helvetica", 40, "bold"))
    card_frame.grid(row=5, column=2, pady=2)

    # 办理银行卡窗口
    Label(card_frame, text='专属ID：').grid(row=2, column=1)
    cus_id = IntVar()
    Entry(card_frame, width=40, textvariable=cus_id).grid(row=2, column=2)

    Label(card_frame, text='卡号：').grid(row=3, column=1)
    pin = IntVar()
    Entry(card_frame, width=40, textvariable=pin).grid(row=3, column=2)

    Label(card_frame, text='存款: ').grid(row=4, column=1)
    deposit = StringVar()
    Entry(card_frame, width=40, textvariable=deposit).grid(row=4, column=2)

    Label(card_frame, text='卡类型: ').grid(row=5, column=1)
    cardtype = StringVar()
    option = ttk.Combobox(card_frame, width=15, textvariable=cardtype)
    option['values'] = ("储蓄卡", "信用卡")
    option.grid(row=5, column=2, sticky="w")
    option.current(0)

    Label(card_frame, text='密码 : ').grid(row=6, column=1)
    secur = StringVar()
    Entry(card_frame, width=40, textvariable=secur, show='*').grid(row=6, column=2)

    Label(card_frame, text='选择银行 : ').grid(row=7, column=1)
    banktype = StringVar()
    option1 = ttk.Combobox(card_frame, width=15, textvariable=banktype)
    option1['values'] = ("中国银行", "中国工商银行", "中国农业银行", "中国建设银行")
    option1.grid(row=7, column=2, sticky="w")
    option1.current(0)

    # 创建银行卡
    def cr():
        cursor.execute("select * from customer where customer_id=%s", (cus_id.get()))
        a = cursor.fetchone()
        if a is None:
            m_box.showwarning('错误！', '没有您的注册记录，请先创建用户！')
            win_create_card.destroy()
        else:
            if int(deposit.get()) < 10:
                m_box.showwarning('错误！', '存款数必须大于10元！')
            else:
                if str(cardtype.get()) == '储蓄卡':
                    cursor.execute("insert into card (pincode,deposit,cardtype,security,customer_id,bank_name) "
                                   "values(%s,%s,%s,hex(AES_ENCRYPT(%s,'key')),%s,%s)",
                                   (pin.get(), deposit.get(), cardtype.get(),
                                    secur.get(), cus_id.get(), banktype.get()))
                    conn.commit()
                    m_box.showinfo('创建成功！', "创建成功！请一定记住卡号和密码！")
                    win_create_card.destroy()
                else:
                    credit = "500"
                    cursor.execute("insert into card (pincode,deposit,cardtype,security,customer_id,bank_name,credit) "
                                   "values(%s,%s,%s,hex(AES_ENCRYPT(%s,'key')),%s,%s,%s)",
                                   (pin.get(), deposit.get(), cardtype.get(), secur.get(),
                                    cus_id.get(), banktype.get(), credit))
                    conn.commit()
                    m_box.showinfo('创建成功！', "请一定记住卡号和密码！若要贷款请移步管理员处！")
                    win_create_card.destroy()

    Button(card_frame, text="提交", command=cr).grid(row=8, column=1, padx=10)
    Button(card_frame, text='退出', command=lambda: win_create_card.destroy()).grid(row=8, column=2, padx=10)


# 登陆界面
def login():
    win_uslogin = Toplevel(win)
    win_uslogin.geometry("410x120")
    win_uslogin.title("客户登陆")

    login_frame = LabelFrame(win_uslogin, text="欢迎登陆 ", fg='red', font=("halvatica", 20, "bold"))
    login_frame.grid(row=3, column=2)
    Label(login_frame, text="您的卡号 : ").grid(row=1, column=0)
    Label(login_frame, text="密码 : ").grid(row=2, column=0)

    ac_var = IntVar()  # 将值转换为int型
    key_a = StringVar()  # 将值转换为string

    # Entry函数用于输入单行文本
    Entry(login_frame, width=30, textvariable=ac_var).grid(row=1, column=1)
    Entry(login_frame, width=30, textvariable=key_a, show='*').grid(row=2, column=1)

    def validate():
        acc = ac_var.get()
        pswd = key_a.get()
        pswd = str(pswd)

        query = "select * from card where pincode=%s and AES_DECRYPT(unhex(security),'key')=%s "
        val = (acc, pswd)
        cursor.execute(query, val)
        a = cursor.fetchone()  # fetchone()函数返回单个元祖

        if a is None:
            m_box.showwarning('title', '请检查输入的卡号或密码是否正确！')
            win_uslogin.destroy()
            login()
            start()
        else:
            # Toplevel 子窗口
            win_uslogin.destroy()
            win_information = Toplevel(win)
            win_information.geometry("800x600")
            win_information.title("个人信息")

            detail = LabelFrame(win_information, text="您的个人信息以及此卡信息如下：",
                                font=("halvatica", 30, "bold"))
            detail.grid(row=2, columnspan=2, padx=140, pady=140)

            print('客户登陆成功')
            data = ["顾客ID      -	",
                    "姓名        -	", "生日        -	", "地址        -	",
                    "电话        -	", "Email        -	",
                    "性别        -	", "卡号        -  ", "余额        -  ", "卡类型        -", "开卡银行        -  ",
                    "信用值       - "]

            for j in range(len(data)):
                Label(detail, text=data[j], fg="red", font=("Times New Roman", 12)).grid(row=j + 3, column=0,
                                                                                         sticky='w')

            cursor.execute("select * from customer where customer_id=%s", a[4])
            n = cursor.fetchone()

            for k in range(len(n)):
                Label(detail, text=n[k], fg='black', font=("Times New Roman", 12)).grid(row=k + 3, column=1,
                                                                                        sticky='w')

            for i in range(len(n), len(n) + 3):
                Label(detail, text=a[i - 7], fg='black', font=("Times New Roman", 12)).grid(row=i + 3,
                                                                                            column=1,
                                                                                            sticky='w')

            # cursor.execute("select bank_name from card where pincode=%s",(acc))
            # b=cursor.fetchone()
            Label(detail, text=a[5], fg='black', font=("Times New Roman", 12)).grid(row=13, column=1, sticky='w')
            Label(detail, text=a[6], fg='black', font=("Times New Roman", 12)).grid(row=14, column=1, sticky='w')

            # 获取余额
            surplus = a[1]
            pin_co = a[0]
            banktype = a[5]
            cardtype = a[2]

            # 存款窗口
            def dep():
                transaction = Toplevel(win)
                win_information.destroy()
                transaction.geometry("700x600")

                data = StringVar()
                Label(transaction, text="请输入您要存款的金额： ",
                      font=("halvatica", 30, "bold"), fg="red").pack(pady=100)
                Entry(transaction, width=30, textvariable=data).pack()

                def Deposit():
                    try:
                        dat = float(data.get())
                        bal = float(a[1])
                        amount = bal + dat
                        amount = str(amount)
                        q3 = "UPDATE card set deposit=%s where pincode=%s"
                        q4 = (amount, acc,)
                        cursor.execute(q3, q4)
                        conn.commit()
                        m_box.showinfo("Transaction", "您的余额已经更新！", parent=transaction)
                        validate()
                        transaction.destroy()
                    except:
                        m_box.showwarning('错误！', '只能填写数字！', parent=transaction)
                        print("存款失败")

                Button(transaction, text="提交", width=10, height=2, command=Deposit).pack()

            # 取款窗口
            def wd():
                transaction = Toplevel(win)
                win_information.destroy()
                transaction.geometry("700x600")

                data = StringVar()
                Label(transaction, text="请输入您想取出的金额： ", fg='red',
                      font=("halvatica", 30, "bold")).pack(pady=100)
                Entry(transaction, width=30, textvariable=data).pack()

                def Deposit():
                    try:
                        dat = float(data.get())
                        bal = float(a[1])
                        if a[2] == "储蓄卡":
                            amount = bal - dat
                            if amount < 0:
                                m_box.showwarning('余额不足', "您的余额数不足！",
                                                  parent=transaction)
                                transaction.destroy()
                                validate()
                            else:
                                balance = str(amount)
                                q3 = "UPDATE card set deposit=%s where pincode=%s"
                                q4 = (balance, acc,)
                                cursor.execute(q3, q4)
                                conn.commit()
                                m_box.showinfo("Transaction", "您的余额已经更新！", parent=transaction)
                                transaction.destroy()
                                validate()
                        else:
                            amount = bal - dat
                            if amount < 0:
                                credit = int(a[6])
                                if credit < 300:
                                    m_box.showwarning('error', '您的信用值不足300，无法办理透支和贷款！')
                                    transaction.destroy()
                                    validate()
                                else:
                                    credit_mo = credit * 10
                                    if amount + credit_mo >= 0:
                                        m_box.showwarning('错误', f"您的余额不足！已为您办理透支！请及时还款！可透支金额还剩 {amount + credit_mo}",
                                                          parent=transaction)
                                        balance = str(amount)
                                        q3 = "UPDATE card set deposit=%s where pincode=%s"
                                        q4 = (balance, acc,)
                                        cursor.execute(q3, q4)
                                        conn.commit()
                                        m_box.showinfo("Transaction", "您的余额已经更新！", parent=transaction)
                                        transaction.destroy()
                                        validate()
                                    else:
                                        m_box.showwarning('error', '您的透支余额不足！')
                                        transaction.destroy()
                                        validate()
                            else:
                                balance = str(amount)
                                q3 = "UPDATE card set deposit=%s where pincode=%s"
                                q4 = (balance, acc,)
                                cursor.execute(q3, q4)
                                conn.commit()
                                m_box.showinfo("Transaction", "您的余额已经更新！", parent=transaction)
                                transaction.destroy()
                                validate()

                    except:
                        m_box.showwarning('错误！', '只能填写数字', parent=transaction)
                        print("取款失败")

                Button(transaction, text="提交", width=10, height=2, command=Deposit).pack()

            # 转账窗口
            def transfer():
                transaction = Toplevel(win)
                win_information.destroy()
                transaction.geometry("430x120")
                transaction.title('转账界面')
                pin = IntVar()
                Label(transaction, text="请输入对方的卡号： ", fg='red',
                      font=("halvatica", 15, "bold")).grid(row=2, column=0)
                Entry(transaction, width=30, textvariable=pin).grid(row=2, column=1)

                money = StringVar()
                Label(transaction, text="请输入转账金额： ", fg='red',
                      font=("halvatica", 15, "bold")).grid(row=3, column=0)
                Entry(transaction, width=30, textvariable=money).grid(row=3, column=1)

                def tf():
                    q = "select * from card where pincode=%s"
                    pin0 = pin.get()
                    val0 = (pin0,)
                    cursor.execute(q, val0)
                    result = cursor.fetchone()
                    if result is None:
                        m_box.showwarning('错误', '查无此卡！')
                    else:
                        q_ = "UPDATE card set deposit=%s where pincode=%s"
                        money0 = money.get()

                        if cardtype == "储蓄卡":
                            # 判断余额和汇款金额
                            if float(money0) > float(surplus):
                                m_box.showwarning('错误', '余额不足！请先充值')
                            else:
                                if result[5] == banktype:
                                    money1 = float(result[1]) + float(money0) * 0.98
                                    m_box.showinfo("Transaction", f'收取2%的手续费用，您已成功转账  {float(money0) * 0.98}!',
                                                   parent=transaction)
                                else:
                                    money1 = float(result[1]) + float(money0) * 0.95
                                    m_box.showinfo("Transaction",
                                                   f'收取5%的跨行手续费用，您已成功转账  {float(money0) * 0.95}!',
                                                   parent=transaction)

                                money1 = str(money1)
                                val_ = (money1, pin0)
                                cursor.execute(q_, val_)  # 更新被转账人金额
                                conn.commit()

                                # 更新转账人金额
                                q_ud = "UPDATE card set deposit=%s where pincode=%s"
                                money_ud = float(surplus) - float(money0)
                                money_ud = str(money_ud)
                                pin_ud = pin_co
                                val_ud = (money_ud, pin_ud,)
                                cursor.execute(q_ud, val_ud)
                                conn.commit()

                                transaction.destroy()
                                validate()
                        else:
                            if result[5] == banktype:
                                money1 = float(result[1]) + float(money0) * 0.98
                                m_box.showinfo("Transaction", f'收取2%的手续费用，您已成功转账  {float(money0) * 0.98}!',
                                               parent=transaction)
                            else:
                                money1 = float(result[1]) + float(money0) * 0.95
                                m_box.showinfo("Transaction",
                                               f'收取5%的跨行手续费用，您已成功转账  {float(money0) * 0.95}!',
                                               parent=transaction)

                            money1 = str(money1)
                            val_ = (money1, pin0)
                            cursor.execute(q_, val_)  # 更新被转账人金额
                            conn.commit()

                            # 更新转账人金额
                            q_ud = "UPDATE card set deposit=%s where pincode=%s"
                            money_ud = float(surplus) - float(money0)
                            money_ud = str(money_ud)
                            pin_ud = pin_co
                            val_ud = (money_ud, pin_ud,)
                            cursor.execute(q_ud, val_ud)
                            conn.commit()

                            transaction.destroy()
                            validate()

                Button(transaction, text='提交', command=tf, font=("Times New Roman", 12), width=10, height=1).grid(
                    row=4, column=1)
                Button(transaction, text='退出', command=transaction.destroy, font=("Times New Roman", 12), width=10,
                       height=1).grid(row=5, column=1)

            Button(detail, text='退出账户', command=win.destroy, font=("Times New Roman", 12)).grid(
                row=15, column=4, sticky='w')
            Button(detail, text='存款', command=dep, font=("Times New Roman", 12)).grid(
                row=15, column=2, sticky='w')
            Button(detail, text='取款', command=wd, font=("Times New Roman", 12)).grid(
                row=15, column=1, sticky='e')
            Button(detail, text='转账', command=transfer, font=("Times New Roman", 12)).grid(
                row=15, column=3, sticky='e')

    Button(login_frame, text='登陆', command=validate, font=("Times New Roman", 12)).grid(row=7, column=1, sticky='e')


# 客户查询贷款情况
def loan_condition():
    win_loan = Toplevel(win)
    win_loan.geometry("400x170")
    win_loan.title("查询贷款登陆")

    login_frame = LabelFrame(win_loan, text="查询贷款 ", fg='red', font=("halvatica", 20, "bold"))
    login_frame.grid(row=3, column=2)
    Label(login_frame, text="您的卡号 : ").grid(row=1, column=0)
    Label(login_frame, text="密码 : ").grid(row=2, column=0)
    ac_var = IntVar()  # 将值转换为int型
    key_a = StringVar()  # 将值转换为string
    # Entry函数用于输入单行文本
    Entry(login_frame, width=30, textvariable=ac_var).grid(row=1, column=1)
    Entry(login_frame, width=30, textvariable=key_a, show='*').grid(row=2, column=1)

    def subm():
        cursor.execute("select * from card where pincode=%s and AES_DECRYPT(unhex(security),'key')=%s",
                       (ac_var.get(), str(key_a.get())))
        m = cursor.fetchone()

        if m is None:
            m_box.showwarning('error', "请检查输入是否正确")
        else:
            if m[2] == "储蓄卡":
                m_box.showwarning('error', '储蓄卡无贷款')
            else:
                win_loan_infor = Tk()
                win_loan_infor.geometry("650x550")
                win_loan_infor.title('贷款个人信息')
                win_loan.destroy()

                detail = LabelFrame(win_loan_infor, text="您的贷款信息如下：",
                                    font=("halvatica", 30, "bold"))
                detail.grid(row=1, columnspan=1, padx=140, pady=140)
                data = ["贷款编号      -	",
                        "贷款原因       -	", "贷款金额        -	", "贷款年数        -	",
                        "利息        -	", "每月偿还        -	",
                        "共偿还       -	", "办理此次业务的管理员ID        -  ", "贷款时间         -", "信用值       - "]

                for j in range(len(data)):
                    Label(detail, text=data[j], fg="red", font=("Times New Roman", 12)).grid(row=j + 3, column=0,
                                                                                             sticky='w')

                cursor.execute("select * from loan where pincode=%s", ac_var.get())
                n = cursor.fetchone()

                for k in range(len(n) - 2):
                    Label(detail, text=n[k], fg='black', font=("Times New Roman", 12)).grid(row=k + 3, column=1,
                                                                                            sticky='w')

                Label(detail, text=n[9], fg='black', font=("Times New Roman", 12)).grid(row=11, column=1, sticky='w')

                cursor.execute("select credit from card where pincode=%s", ac_var.get())
                cre = cursor.fetchone()
                Label(detail, text=cre[0], fg='black', font=("Times New Roman", 12)).grid(row=12, column=1,
                                                                                          sticky='w')

                def pay():
                    win_pay = tkinter.Toplevel()
                    win_pay.geometry("450x120")
                    win_pay.title('还款界面')
                    win_loan_infor.destroy()

                    Label(win_pay, text="待还款金额：", fg='red', font=("halvatica", 15, "bold")).grid(row=1, column=0)
                    Label(win_pay, text="还款金额：", fg='red', font=("halvatica", 15, "bold")).grid(row=2, column=0)

                    owemoney = abs(float(m[1]))
                    Label(win_pay, text=owemoney, fg='black', font=("halvatica", 15, "bold")).grid(row=1, column=1)
                    get_money = DoubleVar()
                    Entry(win_pay, width=30, textvariable=get_money).grid(row=2, column=1)

                    def payment():
                        try:
                            remain = float(get_money.get()) - owemoney
                            remain = str(remain)
                            cursor.execute("update card set deposit =%s where pincode=%s", (remain, ac_var.get()))
                            conn.commit()
                        except:
                            m_box.showwarning('error', '错误！')

                        cursor.execute("update loan set date2 = now() where loan_id=%s", n[0])
                        conn.commit()

                        new_credit = float(get_money.get()) * 0.0006 + float(cre[0])
                        new_credit = int(new_credit)
                        new_credit = str(new_credit)

                        cursor.execute("update card set credit=%s where pincode=%s", (new_credit, ac_var.get()))
                        m_box.showinfo("success", "还款成功！")
                        conn.commit()
                        win_pay.destroy()
                        subm()

                    Button(win_pay, text='还款', command=payment, width=15, height=2, font=("Times New Roman", 12)).grid(
                        row=3, column=1, sticky='w')

                Button(detail, text='还款', command=pay, font=("Times New Roman", 12)).grid(row=13, column=3, sticky='w')
                Button(detail, text='退出', command=win_loan_infor.destroy, font=("Times New Roman", 12)).grid(row=13,
                                                                                                             column=4,
                                                                                                             sticky='w')

    Button(login_frame, text='登陆', command=subm, font=("Times New Roman", 12)).grid(row=7, column=1, sticky='e')


# 销户操作
def delete():
    win_delete = Toplevel(win)
    win_delete.geometry("400x170")
    win_delete.title("注销银行卡")

    delete_frame = LabelFrame(win_delete, text="注销银行卡", fg='red', font=("halvatica", 20, "bold"))
    delete_frame.grid(row=3, column=2)
    Label(delete_frame, text="您的卡号 : ").grid(row=1, column=0)
    Label(delete_frame, text="密码 : ").grid(row=2, column=0)

    pin_var = IntVar()
    pasd_a = StringVar()  # 将值转换为string

    # Entry函数用于输入单行文本
    Entry(delete_frame, width=30, textvariable=pin_var).grid(row=1, column=1)
    Entry(delete_frame, width=30, textvariable=pasd_a, show='*').grid(row=2, column=1)

    def check():

        pin = pin_var.get()
        psd = pasd_a.get()
        psd = str(psd)

        query = "select * from card where pincode=%s and AES_DECRYPT(unhex(security),'key')=%s "
        val1 = (pin, psd)
        cursor.execute(query, val1)
        a = cursor.fetchone()

        if a is None:
            m_box.showwarning('错误！', '请确保输入的信息是正确的！')
        else:
            if a[1] == "0":
                cursor.execute('delete from card where pincode=%s', pin)
                conn.commit()
                m_box.showinfo("win", "注销成功！", parent=win)
                win_delete.destroy()
            else:
                m_box.showwarning('错误！', '您的余额并不为0，无法注销账户！')
                win_delete.destroy()

    Button(delete_frame, text='提交', command=check, font=("Times New Roman", 12)).grid(row=7, column=1, sticky='e')


# 主程序
def start():
    title1 = Label(win, text='欢迎来到银行系统！', fg="red", )
    title1.grid(row=1, column=1, padx=100)
    Label.config(title1, font=("Times New Roman", 30, "bold"))

    create_button = Button(win, text='创建个人账户', command=create, width=10, height=2,
                           font=("halvatica", 20, "bold"))
    create_button.grid(row=2, column=1, padx=5, pady=40)

    card_button = Button(win, text='办理银行卡', command=create_card, width=10, height=2, fg="black",
                         font=("halvatica", 20, "bold"))
    card_button.grid(row=2, column=2, padx=5, pady=40)

    login_button = Button(win, text='登陆', command=login, width=10, height=2, fg="black",
                          font=("halvatica", 20, "bold"))
    login_button.grid(row=3, column=1, padx=5, pady=40)

    loan_button = Button(win, text='查看贷款', command=loan_condition, width=10, height=2, fg="black",
                         font=("halvatica", 20, "bold"))
    loan_button.grid(row=4, column=1, padx=5, pady=40)

    delete_button = Button(win, text='注销银行卡', command=delete, width=10, height=2,
                           font=("halvatica", 20, "bold"))
    delete_button.grid(row=3, column=2, padx=5, pady=40)

    Button(win, text='退出系统', command=lambda: win.destroy(), width=10, height=2, font=("halvatica", 20, "bold")).grid(
        row=4, column=2, padx=5, pady=40)


start()
win.mainloop()
conn.commit()
conn.close()
