import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QToolBar,QDirModel,QTreeView,QFileSystemModel,QGroupBox,QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt,QDir
from PyQt5.QtWidgets import QApplication,QPushButton, QWidget, QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout,QTextBrowser,QToolBar,QMenuBar,QAction


class Ui_MainWindow(object):
    def setupUi(self,windget):
        windget.resize(850, 700)
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.h4_layout = QHBoxLayout()
        self.h5_layout = QHBoxLayout()
        self.h6_layout = QHBoxLayout()
        self.h7_layout = QHBoxLayout()
        self.h8_layout = QHBoxLayout()
        self.h9_layout = QHBoxLayout()
        self.h10_layout = QHBoxLayout()
        self.h11_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.statusbar = QtWidgets.QStatusBar()
        self.toolbar = QToolBar()
        self.menubar = QMenuBar()
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(240, 240, 240)}")
        self.menubar.setFixedSize(870,22)
        self.menubar.setMaximumSize(9999,9999)
        self.h4_layout.addWidget(self.menubar)
        self.h5_layout.addWidget(self.toolbar)


        self.file_Menu = self.menubar.addMenu("文件")

        self.file_compare = QAction(QIcon('exit.png'), '&对比')
        self.file_compare.setShortcut('Shift+F10')
        self.file_compare.setStatusTip('对比文件')
        self.file_Menu.addAction(self.file_compare)

        self.file_save = QAction(QIcon('exit.png'), '&保存')
        self.file_save.setShortcut('Ctrl+s')
        self.file_save.setStatusTip('保存备案比对结果')
        self.file_Menu.addAction(self.file_save)

        self.file_open = QAction(QIcon('exit.png'), '&打开')
        self.file_open.setShortcut('')
        self.file_open.setStatusTip('打开备案比对结果')
        self.file_Menu.addAction(self.file_open)



        self.select_Menu = self.menubar.addMenu("选择")

        self.select_backup = QAction(QIcon('exit.png'), '&备案文件')
        self.select_backup.setShortcut('')
        self.select_backup.setStatusTip('选择备案文件')
        self.select_Menu.addAction(self.select_backup)

        self.select_source = QAction(QIcon('exit.png'), '&待对比文件')
        self.select_source.setShortcut('')
        self.select_source.setStatusTip('选择待对比文件')
        self.select_Menu.addAction(self.select_source)








        self.record_Menu = self.menubar.addMenu("对比记录")






        self.win_Menu = self.menubar.addMenu("窗口")

        self.win_max = QAction(QIcon('exit.png'), '&窗口最大化')
        self.win_max.setShortcut('')
        self.win_max.setStatusTip('最大化窗口')
        self.win_Menu.addAction(self.win_max)

        self.win_min = QAction(QIcon('exit.png'), '&窗口最小化')
        self.win_min.setShortcut('')
        self.win_min.setStatusTip('最小化窗口')
        self.win_Menu.addAction(self.win_min)



        self.user_Menu = self.menubar.addMenu("用户")

        self.user_out = QAction(QIcon('exit.png'), '&用户信息')
        self.user_out.setShortcut('')
        self.user_out.setStatusTip('注销用户')
        self.user_Menu.addAction(self.user_out)

    #     self.user_out.triggered.connect(self.sign_out)
    #
    # def sign_out(self):
    #     self.close()
    #     dialog = logindialog()
    #     if dialog.exec_() == QDialog.Accepted:
    #         the_window = Main()
    #         self.windowList.append(the_window)  # 这句一定要写，不然无法重新登录
    #         the_window.show()









        self.quit_Menu = self.menubar.addMenu("退出")

        self.quit_app = QAction(QIcon('exit.png'), '&退出')
        self.quit_app.setShortcut('Ctrl+Q')
        self.quit_app.setStatusTip('退出')
        self.quit_Menu.addAction(self.quit_app)

        self.help_Menu = self.menubar.addMenu("帮助")
        self.help_app = QAction(QIcon('exit.png'), '&帮助')
        self.help_app.setShortcut('')
        self.help_app.setStatusTip('帮助信息')
        self.help_Menu.addAction(self.help_app)



        self.groupbox_1 = QGroupBox('备案文件')  # 1
        # self.groupbox_1.setMaximumSize(9999,9999)
        self.groupbox_2 = QGroupBox('待对比文件')
        # self.groupbox_2.setMaximumSize(9999,9999)
        self.groupbox_3 = QGroupBox('比对结果')
        self.groupbox_4 = QGroupBox()
        self.groupbox_4.setLayout(self.h5_layout)
        self.h11_layout.addWidget(self.groupbox_4)
        self.toolbutton = QtWidgets.QToolButton()
        self.toolbar.setMovable(False)
        self.toolbutton.setAutoRaise(True)
        self.toolbutton.setIcon(QIcon('素材/开始.png'))
        self.toolbutton.setText("开始")
        self.toolbutton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.toolbutton2 = QtWidgets.QToolButton()
        # self.toolbutton2.setCheckable(False)
        self.toolbutton2.setAutoRaise(True)
        self.toolbutton2.setIcon(QIcon('素材/文档.png'))
        self.toolbutton2.setText("保存")
        self.toolbutton2.setToolTip("保存比对结果")
        # 在工具栏ToolBar里同时添加图标和文字，并设置图标和文字的相对位置；若没有下面的一行或多行代码，则只显示图标或文字。
        self.toolbutton2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.toolbutton3 = QtWidgets.QToolButton()
        # self.toolbutton3.setCheckable(False)
        self.toolbutton3.setAutoRaise(True)
        self.toolbutton3.setIcon(QIcon('素材/关闭.png'))
        self.toolbutton3.setText("退出")
        self.toolbutton3.setToolTip("退出")
        # 在工具栏ToolBar里同时添加图标和文字，并设置图标和文字的相对位置；若没有下面的一行或多行代码，则只显示图标或文字。
        self.toolbutton3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        self.toolbutton4 = QtWidgets.QToolButton()
        # self.toolbutton3.setCheckable(False)
        self.toolbutton4.setAutoRaise(True)
        self.toolbutton4.setIcon(QIcon('素材/下载.png'))
        self.toolbutton4.setText("下载备案")
        self.toolbutton4.setToolTip("下载备案文件")
        # 在工具栏ToolBar里同时添加图标和文字，并设置图标和文字的相对位置；若没有下面的一行或多行代码，则只显示图标或文字。
        self.toolbutton4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        self.toolbutton5 = QtWidgets.QToolButton()
        # self.toolbutton3.setCheckable(False)
        self.toolbutton5.setAutoRaise(True)
        self.toolbutton5.setIcon(QIcon('素材/上传.png'))
        self.toolbutton5.setText("上传结果")
        self.toolbutton5.setToolTip("上传代码比对结果")
        # 在工具栏ToolBar里同时添加图标和文字，并设置图标和文字的相对位置；若没有下面的一行或多行代码，则只显示图标或文字。
        self.toolbutton5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        self.toolbar.addWidget(self.toolbutton)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.toolbutton4)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.comboBox)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.toolbutton2)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.toolbutton5)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.toolbutton3)






        self.backup_label = QtWidgets.QLabel()
        self.backup_label.setFixedSize(375, 25)
        self.backup_label.setFont(QFont("Roman times", 11,))
        self.backup_label.setText("请选择合适的备案文件")

        self.backup_button = QtWidgets.QPushButton()
        self.backup_button.setFixedSize(30, 30)
        self.backup_button.setIcon(QIcon("素材/文件夹.png"))

        self.source_label = QtWidgets.QLabel()
        self.source_label.setFixedSize(375, 25)
        self.source_label.setFont(QFont("Roman times", 11, ))
        self.source_label.setText("请选择合适的待比对文件")

        self.source_button = QtWidgets.QPushButton()
        self.source_button.setFixedSize(30, 30)
        self.source_button.setIcon(QIcon("素材/文件夹.png"))

        self.h6_layout.addWidget(self.backup_label)
        self.h6_layout.addWidget(self.backup_button)
        self.h6_layout.addWidget(self.source_label)
        self.h6_layout.addWidget(self.source_button)


        self.backup_win = QtWidgets.QWidget()
        self.backup_win.setFixedSize(420, 300)
        # self.backup_win.resize(500, 300)
        # self.backup_win.setMaximumSize(9999,9999)
        # self.backup_win.resize(420,300)

        self.source_win = QtWidgets.QWidget()
        self.source_win.setFixedSize(420, 300)
        # self.source_win.setMaximumSize(9999,9999)

        self.h1_layout.addWidget(self.backup_win)
        self.groupbox_1.setLayout(self.h1_layout)
        self.h2_layout.addWidget(self.source_win)
        self.groupbox_2.setLayout(self.h2_layout)


        self.backup_model = QFileSystemModel()

        self.backup_tree = QTreeView(self.backup_win)

        self.backup_model.setReadOnly(True)
        self.backup_tree.setGeometry(0, 0, 400, 290)

        self.source_model = QFileSystemModel()

        self.source_tree = QTreeView(self.source_win)

        self.source_model.setReadOnly(True)
        self.source_tree.setGeometry(0, 0, 400, 290)

        self.textBrowser = QtWidgets.QTextBrowser()

        self.textBrowser.setFixedSize(800, 250)
        self.textBrowser.setMaximumSize(9999,9999)
        self.h7_layout.addWidget(self.textBrowser)
        self.groupbox_3.setLayout(self.h7_layout)
        self.pbar = QtWidgets.QProgressBar()
        self.pbar.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.h9_layout.addWidget(self.pbar)
        # self.statusbar = QtWidgets.QStatusBar()
        self.h10_layout.addWidget(self.statusbar)


        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)
        # self.h3_layout.setSpacing(0)
        self.h8_layout.addWidget(self.groupbox_3)
        self.all_v_layout.addLayout(self.h4_layout)
        self.all_v_layout.addLayout(self.h11_layout)
        self.all_v_layout.addLayout(self.h6_layout)
        self.all_v_layout.addLayout(self.h3_layout)
        self.all_v_layout.addLayout(self.h8_layout)
        self.all_v_layout.addLayout(self.h9_layout)
        self.all_v_layout.addLayout(self.h10_layout)
        windget.setLayout(self.all_v_layout)
        self.retranslateUi(windget)



    def retranslateUi(self, windget):
        _translate = QtCore.QCoreApplication.translate
        windget.setWindowTitle(_translate("MainWindow", "电表代码对比软件"))
        windget.setWindowIcon(QIcon('素材/电网.ico'))
        self.comboBox.setItemText(0, _translate("MainWindow", "直接对比方式"))
        self.comboBox.setItemText(1, _translate("MainWindow", "数字签名对比方式"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Ui_MainWindow()
    demo.setupUi()
    demo.show()
    sys.exit(app.exec_())
