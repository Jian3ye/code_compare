import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
from 主界面 import Main
import sqlite3


class MainWindow(QMainWindow):
    windowList = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('电表代码比对软件')
        self.setWindowIcon(QIcon('素材/电网.ico'))
        self.resize(600,600)


    # # 动作一：注销
    # def on_printAction1_triggered(self):
    #     self.close()
    #     dialog = logindialog()
    #     if  dialog.exec_()==QDialog.Accepted:
    #         the_window = MainWindow()
    #         self.windowList.append(the_window)    #这句一定要写，不然无法重新登录
    #         the_window.show()




class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('电表代码对比软件登录界面')
        self.setWindowIcon(QIcon('素材/电网.ico'))
        self.resize(500,400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        ###### 设置界面控件
        self.frame = QFrame(self)
        self.lab = QLabel(self.frame)
        self.lab.setGeometry(0,0,500,200)
        self.lab.setPixmap(QPixmap('素材/登陆背景图.png'))
        self.lab1 = QLabel(self.frame)
        self.lab1.setText("电表代码对比系统")
        self.lab1.setStyleSheet("color:#FFFFFF")
        self.lab1.setFont(QFont("Roman times", 20, QFont.Bold))
        self.lab1.setGeometry(40,50,230,30)
        self.username_label = QLabel("用户名:",self.frame)
        self.username_label.setGeometry(140,215,50,20)
        self.lineEdit_account = QLineEdit(self.frame)
        self.lineEdit_account.setGeometry(190,210,160,28)
        self.lineEdit_account.setPlaceholderText("请输入账号")

        self.password_label = QLabel("密   码:",self.frame)
        self.password_label.setGeometry(140,253,50,20)
        self.lineEdit_password = QLineEdit(self.frame)
        self.lineEdit_password.setGeometry(190,248,160,28)
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.checkBox_remeberpassword = QCheckBox(self.frame)
        self.checkBox_remeberpassword.setGeometry(190,285,80,20)
        self.checkBox_remeberpassword.setText("记住密码")

        self.checkBox_autologin = QCheckBox(self.frame)
        self.checkBox_autologin.setGeometry(275,285,80,20)
        self.checkBox_autologin.setText("自动登录")

        self.pushButton_enter = QPushButton(self.frame)
        self.pushButton_enter.setGeometry(190,310,60,30)
        self.pushButton_enter.setText("确定")
        self.pushButton_enter.setStyleSheet("QPushButton{background-color:#5abf9a;border:1px;border-radius: 2px;color:#FFFFFF;font-size:15px;height:10px}"
                                  "QPushButton:hover{background-color:#333333;}")

        self.pushButton_quit = QPushButton(self.frame)
        self.pushButton_quit.setGeometry(280,310,60,30)
        self.pushButton_quit.setText("取消")
        self.pushButton_quit.setStyleSheet("QPushButton{background-color:#5abf9a;border:1px;border-radius: 2px;color:#FFFFFF;font-size:15px;height:10px}"
                                  "QPushButton:hover{background-color:#333333;}")

        self.timelabel = QLabel(self.frame)
        self.username_label = QLabel(self.frame)
        # self.timelabel.setStyleSheet("color:#000000")
        self.timelabel.setGeometry(250,380,250,20)
        self.username_label.setGeometry(0, 380, 250, 20)
        self.username_label.setStyleSheet("QLabel{background-color:#FCFCFC;}")



        self.timelabel.setStyleSheet("QLabel{background-color:#FCFCFC;}")
        # self.timelabel.setStyleSheet("QLabel{background-color:#000000;}")

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()


        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)


        ####初始化登录信息
        self.init_login_info()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.text1 = self.lineEdit_account.text()
        self.username_label.setText("  您好： " + self.text1)
        self.timelabel.setText(text)
        self.timelabel.setAlignment(Qt.AlignRight)
        # self.timelabel.setStyleSheet("QLabel{color:#FFFFFF}")
        self.timelabel.setFont(QFont("Roman times", 12,))



    def on_pushButton_enter_clicked(self):
        # 账号判断
        if self.lineEdit_account.text() == "" and self.lineEdit_password.text() == "":
            QMessageBox.warning(self, "Warning", "请输入您的账号和密码",
                                QMessageBox.Yes, QMessageBox.Yes)
        elif self.lineEdit_account.text() == "" and self.lineEdit_password.text() != "":
            QMessageBox.warning(self, "Warning", "请输入您的密码",
                                QMessageBox.Yes, QMessageBox.Yes)
        elif self.lineEdit_account.text() != "" and self.lineEdit_password.text() == "":
            QMessageBox.warning(self, "Warning", "请输入您的账号",
                                QMessageBox.Yes, QMessageBox.Yes)
        else:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            account = self.lineEdit_account.text()
            results = cursor.execute('select name from user where id=?', (account,))
            text = results.fetchall()
            if text[0][0] == self.lineEdit_password.text():
                self.save_login_info()
                self.accept()
            else:
                QMessageBox.warning(self, "您输入的账号或密码有误", "请确认您的用户名或者密码是否正确。",
                                    QMessageBox.Yes, QMessageBox.Yes)



    # 保存登录信息
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.setValue("account",self.lineEdit_account.text())
        settings.setValue("password", self.lineEdit_password.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())



    # 初始化登录信息
    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        the_account =settings.value("account")
        the_password = settings.value("password")
        the_remeberpassword = settings.value("remeberpassword")
        the_autologin = settings.value("autologin")
        ########
        self.lineEdit_account.setText(the_account)
        if the_remeberpassword=="true" or  the_remeberpassword==True:
            self.checkBox_remeberpassword.setChecked(True)
            self.lineEdit_password.setText(the_password)

        if the_autologin=="true" or  the_autologin==True:
            self.checkBox_autologin.setChecked(True)

        if the_autologin == "true":   #防止注销时，自动登录
            threading.Timer(1, self.on_pushButton_enter_clicked).start()
            #self.on_pushButton_enter_clicked()

################################################
#######程序入门
################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if  dialog.exec_()==QDialog.Accepted:
        the_window = Main()
        the_window.show()
        the_window.ui.statusbar.showMessage("  您好： " + dialog.text1)
        sys.exit(app.exec_())
