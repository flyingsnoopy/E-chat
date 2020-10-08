import pickle
import poplib
import smtplib
import sys
import tkinter as tk
from email.header import Header
from email.mime.text import MIMEText
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header
from PyQt5.QtWidgets import *
from addfriend import Ui_addfriendDialog
from chat import Ui_chatMainWindow
from login import Ui_LoginDialog

user = []
friend = {}


def mirror(dictionary):
    back = {}
    for i in dictionary:
        back[dictionary[i]] = i
    return back


def login():
    global user
    try:
        friend_file = open('friend.dat', 'rb+')
        friend_file.close()
    except:
        friend_file = open('friend.dat', 'wb+')
        pickle.dump(friend, friend_file)
        friend_file.close()

    def loginpushbutton_funtion():
        global user
        # 定义登录按钮函数
        username = login_dialog.usernamelineEdit.text()  # 将usernamelineEdit内赋值到username，输入的是用户邮件
        password = login_dialog.passwordlineEdit.text()  # 将passwordlineEdit内赋值倒password
        try:
            namelist = username.split('@')
            mail_host = "smtp." + namelist[1]  # 通过用户邮件来获得smtp服务器
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(username, password)
            user = [username, password, mail_host]
            user_file = open('user.dat', 'wb+')
            pickle.dump(user, user_file)
            user_file.close()
            login_main.close()
        except:
            # 仅仅是个提示语句

            msgbox_window = tk.Tk()
            msgbox_window.title("错误")
            msgbox_window.geometry("200x100")

            l = tk.Label(msgbox_window, text='错误的用户名或密码')
            l.pack()

            def close():
                msgbox_window.destroy()

            b = tk.Button(msgbox_window, text='OK', command=close)
            b.pack()
            msgbox_window.mainloop()

    login_app = QApplication(sys.argv)
    login_main = QDialog()
    login_dialog = Ui_LoginDialog()
    login_dialog.setupUi(login_main)
    login_main.show()
    login_dialog.loginpushButton.clicked.connect(lambda: loginpushbutton_funtion())
    login_app.exec_()


def addfriend():
    global friend

    def appendButton_funtion():
        global friend
        friendname = addfrined_dialog.friendnamelineEdit.text()
        friendaddress = addfrined_dialog.friendaddresslineEdit.text()
        friend[friendname] = friendaddress
        friend_file = open('friend.dat', 'wb+')
        pickle.dump(friend, friend_file)
        friend_file.close()

    addfriend_app = QApplication(sys.argv)
    addfriend_main = QDialog()
    addfrined_dialog = Ui_addfriendDialog()
    addfrined_dialog.setupUi(addfriend_main)
    addfriend_main.show()
    addfrined_dialog.appearButton.clicked.connect(lambda: appendButton_funtion())
    addfriend_app.exec_()


def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            return '%sText: %s' % ('  ' * indent, content + '...')
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def chat(address):
    global user, friend
    friend_mirror = mirror(friend)
    chat_list = []
    username = user[0]
    password = user[1]
    pop_list = username.split('@')
    pop_host = 'pop3.' + pop_list[1]

    server = poplib.POP3(pop_host)
    server.user(username)
    server.pass_(password)
    def receive():
        resp, mails, octets = server.list()
        index = len(mails)
        resp, lines, octets = server.retr(index)
        msg_content = '\r\n'.join(lines)
        msg = Parser().parsestr(msg_content)

        value = msg.get('From', '')
        hdr, addr = parseaddr(value)
        name = decode_str(hdr)
        value = u'%s <%s>' % (name, addr)
        if addr == address:
            if (msg.is_multipart()):
                parts = msg.get_payload()
                for n, part in enumerate(parts):
                    message=print_info(part, 2)
                    chat_mainWindow.chattextBrowser.append(friend_mirror[address])
                    chat_mainWindow.chattextBrowser.append(message)

    def send():

        msg = chat_mainWindow.inputtextEdit.toPlainText()
        receiver = [address]
        print(user)
        username = user[0]
        password = user[1]
        mail_host = user[2]
        friend_name = friend_mirror[address]

        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(username, 'utf-8')
        message["To"] = Header('测试', 'utf-8')

        subject = 'E-chat'
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(username, password)
        smtpObj.sendmail(username, receiver, message.as_string())
        chat_mainWindow.chattextBrowser.append(username)
        chat_mainWindow.chattextBrowser.append(msg)

    chat_app = QApplication(sys.argv)
    chat_main = QMainWindow()
    chat_mainWindow = Ui_chatMainWindow()
    chat_mainWindow.setupUi(chat_main)
    chat_mainWindow.sendpushButton.clicked.connect(lambda: send())
    chat_main.show()
    chat_app.exec_()


login()
friend_file = open('friend.dat', 'rb+')
friend = pickle.load(friend_file)
main = tk.Tk()
main.title("E-Chat")
for i in friend.keys():
    friend_button = []
    friend_button.append(tk.Button(text=i, width=20, command=lambda: chat(friend[i])))
    for j in friend_button:
        j.pack()
addfriend_button = tk.Button(text='添加好友', command=addfriend, width=20)
addfriend_button.pack()
main.mainloop()
