from PyQt5 import QtCore, QtGui, QtWidgets
from 主界面设计 import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os, os.path
import rsaCompare, diffCompare

class Main(QWidget, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 对比结果的不同文件的记录和数目的计数目
        self.inequality_filenums = 0
        self.inequality_filename = []

        self.ui.toolbutton.clicked.connect(self.start_compare)
        self.ui.toolbutton3.clicked.connect(self.close)
        self.ui.toolbutton2.clicked.connect(self.save_result)
        self.ui.toolbutton4.clicked.connect(self.download)
        self.ui.backup_button.clicked.connect(self.loadBackupCode)
        self.ui.source_button.clicked.connect(self.loadSourceCode)

        self.ui.file_compare.triggered.connect(self.start_compare)
        self.ui.file_save.triggered.connect(self.save_result)
        self.ui.select_backup.triggered.connect(self.loadBackupCode)
        self.ui.select_source.triggered.connect(self.loadSourceCode)

        self.ui.win_max.triggered.connect(self.showMaximized)
        self.ui.win_min.triggered.connect(self.showMinimized)
        # self.ui.user_out.triggered.connect(self.sign_out)
        self.ui.quit_app.triggered.connect(self.close)
        self.ui.help_app.triggered.connect(self.help)

    def download(self):
        text, ok = QInputDialog.getText(self, '请输入', '输入备案文件序列号：')
        if ok:
            string = str(text)
            print(string)


    def help(self):
        QMessageBox.information(self, "帮助", "电表代码比对软件版本：V1.0\n研发单位：武汉大学网络安全学院\n电话:13638639533{0}(刘金硕教授)；",
                                QMessageBox.Yes, QMessageBox.Yes)


    # def sign_out(self):
    #     self.close()
    #     dialog = logindialog()
    #     if dialog.exec_() == QDialog.Accepted:
    #         the_window = Main()
    #         self.windowList.append(the_window)  # 这句一定要写，不然无法重新登录
    #         the_window.show()


    #保存比对结果

    def save_result(self):
        StrText = self.ui.textBrowser.toPlainText()
        qS = str(StrText)
        if qS == '':
            QMessageBox.warning(self, "Warning", "请先生成比对结果再保存",
                                QMessageBox.Yes, QMessageBox.Yes)
        else:
            filename = QFileDialog.getSaveFileName(self,"文件保存","/","All Files (*);;Text Files(*.txt)")
            if filename[0]:
                print("1")
                with open(filename[0], 'w') as f:
                    f.write(qS)
                QMessageBox.information(self, "比对结果保存成功", "比对结果已经成功保存到指定目录",
                                    QMessageBox.Yes, QMessageBox.Yes)


    # 重写关闭函数
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '关闭程序',
                                               "关闭程序可能导致正在进行的操作终止，请确认\n是否退出并关闭程序？",
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 获取目标文件夹的所有文件
    def find_file(self, file_path):
        all_file_list = list()
        num = len(file_path)
        for root, subdirs, files in os.walk(file_path):
            for filepath in files:
                all_file_list.append(os.path.join(root, filepath)[num::])
        return all_file_list


    # 备案导入按键的槽函数
    def loadBackupCode(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        dlg.setFilter(QDir.Files)
        self.backup_selectfile = dlg.selectedFiles()
        if dlg.exec_():
            self.ui.backup_model.setRootPath(QDir.rootPath())
            self.ui.backup_tree.setModel(self.ui.backup_model)
            filenames = dlg.selectedFiles()
            filenames1 = filenames[0].replace('/', '\\')
            index = self.ui.backup_model.index(filenames[0])
            self.ui.backup_tree.setRootIndex(index)
            self.ui.backup_label.setText(filenames[0])
            self.BackupCode = filenames1
            self.file_list = self.find_file(filenames[0])

    # 待对比文件导入的槽函数
    def loadSourceCode(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            self.ui.source_model.setRootPath(QDir.rootPath())
            self.ui.source_tree.setModel(self.ui.source_model)
            filenames = dlg.selectedFiles()

            filenames1 = filenames[0].replace('/','\\')

            index = self.ui.source_model.index(filenames[0])
            self.ui.source_tree.setRootIndex(index)
            self.ui.source_label.setText(filenames[0])
            self.SourceCode = filenames1

        # 保存登录信息
    def save_record(self):


        settings = QSettings("record.ini", QSettings.IniFormat)
        settings.setValue("backup", self.ui.backup_label.text())
        settings.setValue("source", self.ui.source_label.text())
        the_backup = settings.value("backup")
        the_source = settings.value("source")
        self.ui.record_Menu.addMenu(the_backup + "  ||  " + the_source)
        # self.new_record = QAction(the_backup + "  ||  " + the_source)
        # self.ui.record_Menu.addAction(self.new_record)
        # i = 1
        # # new_record = "new_record" + str(i)
        # locals()['new_record' + str(i)] = QAction(the_backup + "  ||  " + the_source)
        # print(locals()['new_record' + str(i)])
        # self.ui.record_Menu.addAction(locals()['new_record' + str(i)])
        # i = i +1




    # 代码对比的槽函数
    def start_compare(self):
        self.ui.textBrowser.clear()
        if self.ui.backup_label.text() == "请选择合适的备案文件" and self.ui.source_label.text() == "请选择合适的待比对文件":
            QMessageBox.warning(self, "Warning", "您未选择备案文件和待比对文件",
                                QMessageBox.Yes ,QMessageBox.Yes)
        elif self.ui.backup_label.text() == "请选择合适的备案文件" and self.ui.source_label.text() != "请选择合适的待比对文件":
            QMessageBox.warning(self, "Warning", "您未选择备案文件",
                                QMessageBox.Yes, QMessageBox.Yes)
        elif self.ui.backup_label.text() != "请选择合适的备案文件" and self.ui.source_label.text() == "请选择合适的待比对文件":
            QMessageBox.warning(self, "Warning", "您未选择待比对文件",
                                QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.save_record()
            self.compare_thraed = compare_Thread(self.file_list,self.BackupCode,self.SourceCode,self.ui)
            self.compare_thraed.text_signal.connect(self.text_show)
            self.compare_thraed.pbar_signal.connect(self.pbar_show)
            self.compare_thraed.start()

    def text_show(self,astr):
        test_str1 = "不一致"
        test_str2 = "缺少文件"
        if test_str1 in astr or test_str2 in astr:
            self.inequality_filenums += 1
            self.inequality_filename.append(astr)
            self.ui.textBrowser.append("\n")
            cursor = self.ui.textBrowser.textCursor()
            cursor.insertHtml(
                '''<p><span style="color: red;">{}</span>'''.format(astr))
        else:
            self.ui.textBrowser.append("\n")
            cursor = self.ui.textBrowser.textCursor()
            cursor.insertHtml(
                '''<p><span style="color: bule;">{}</span>'''.format(astr))
            # self.ui.textBrowser.append(astr)

    def pbar_show(self,i):
        self.ui.pbar.setValue(i)
        if i == 100:
            files_num = len(self.file_list)
            QMessageBox.information(self, "电表代码比对完成", "您选择的备案文件与待对比文件已经对比完成.\n进行比对的文件一共{0}个。\n其中有{1}个文件是不一致或者缺少的。\n不一致的文件为为{2}".format(files_num,self.inequality_filenums,self.inequality_filename),
                                    QMessageBox.Yes, QMessageBox.Yes)


class compare_Thread(QThread):
    text_signal = pyqtSignal(str)
    pbar_signal = pyqtSignal(int)

    def __init__(self,file_list,Backup,Source,ui):
        super().__init__()
        self.file_list = file_list
        self.Backup_code = Backup
        self.Source_code = Source
        self.ui = ui

    def run(self):
        self.pbar_len = len(self.file_list)
        pbar_sum = 0
        if self.ui.comboBox.currentIndex() == 1:
            self.ui.textBrowser.append("==============================================================数字签名比对结果==============================================================")
            for file in self.file_list:
                if os.path.exists(self.Source_code + file):
                    result = rsaCompare.compare(self.Backup_code + file, self.Source_code + file)
                    self.text_signal.emit(result)
                    self.text_signal.emit("---" * 45)
                    pbar_sum += 1
                    pbar_value = (pbar_sum/self.pbar_len )*100
                    self.pbar_signal.emit(pbar_value)

                else:
                    result = "待比对目录" + "   " + self.Source_code + "   " + "缺少文件" + "   " + file
                    self.text_signal.emit(result)
                    self.text_signal.emit("---" * 45)
                    pbar_sum += 1
                    pbar_value = (pbar_sum / self.pbar_len ) * 100
                    self.pbar_signal.emit(pbar_value)

        else:
            self.ui.textBrowser.append("==============================================================直接比对结果==============================================================")
            for file in self.file_list:
                if os.path.exists(self.Source_code + file):
                    result = diffCompare.compare(self.Backup_code + file, self.Source_code + file)
                    self.text_signal.emit(result)
                    self.text_signal.emit("---"*45)
                    pbar_sum += 1
                    pbar_value = (pbar_sum / self.pbar_len ) * 100
                    self.pbar_signal.emit(pbar_value)
                else:
                    result = "待比对目录" + "   " + self.Source_code + "   " + "缺少文件" + "   " + file
                    self.text_signal.emit(result)
                    self.text_signal.emit("---" * 45)
                    pbar_sum += 1
                    pbar_value = (pbar_sum / self.pbar_len ) * 100
                    self.pbar_signal.emit(pbar_value)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
