from PyQt5 import QtCore, QtWidgets
import sys

from main import Ui_DecFuzzer as main_Ui
from readme import Ui_DecFuzzer as readme_Ui
from run_window import Ui_DecFuzzer as run_Ui
from reproduce_window import Ui_DecFuzzer as reproduce_Ui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import subprocess
import os


# 主窗口
class MainWindow(QtWidgets.QWidget, main_Ui):
    switch_window1 = QtCore.pyqtSignal()    # 跳转信号
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goRun)
        self.pushButton_2.clicked.connect(self.goReproduce)
        self.pushButton_3.clicked.connect(self.goReadme)

    def goRun(self):
        self.switch_window1.emit()
    def goReproduce(self):
        self.switch_window2.emit()
    def goReadme(self):
        self.switch_window3.emit()



# run 窗口
class RunWindow(QtWidgets.QWidget, run_Ui):
    back_MainWindow = QtCore.pyqtSignal()
    def __init__(self):
        super(RunWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.goMain)
        self.pushButton_4.clicked.connect(self.stopPy_run)
        self.pushButton_5.clicked.connect(self.runPy_run)

        self.cmd_thread = Cmder("")
        self.cmd_thread.log.connect(self.run_log)

    def goMain(self):
        self.back_MainWindow.emit()

    def runPy_run(self):
        cmd = f'python3 run.py'
        #cmd = f'python3 test_print.py'
        self.run_log(cmd+'\n')
        self.cmd_thread.cmd = cmd
        self.cmd_thread.start()

    def stopPy_run(self):
        child = subprocess.Popen(["pgrep", "-f", "python3 run.py"], stdout=subprocess.PIPE, shell=False)
        pids = str(child.communicate()[0], encoding='utf-8')

        if not pids:
            self.run_log("no target pid to kill, please check")

        for pid in pids.split('\n')[:-1]:
            os.system("kill -9 " + pid)
        # os.system("kill -9 " + pids)
        # 杀死进程
        print("stopPy_run")

    def run_log(self, string):
        self.textBrowser.insertPlainText(string)
        textCursor = self.textBrowser.textCursor()
        # 滚动到底部
        textCursor.movePosition(textCursor.End)
        # 设置光标到text中去
        self.textBrowser.setTextCursor(textCursor)



# reproduce 窗口
class ReproduceWindow(QtWidgets.QWidget, reproduce_Ui):
    back_MainWindow = QtCore.pyqtSignal()
    def __init__(self):
        super(ReproduceWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.goMain)
        self.pushButton_4.clicked.connect(self.stopPy_reproduce)
        self.pushButton_5.clicked.connect(self.runPy_reproduce)

        self.pushButton.clicked.connect(self.setFileDir)
        self.pushButton_2.clicked.connect(self.setEmi_dir)

        self.cmd_thread = Cmder("")
        self.cmd_thread.log.connect(self.reproduce_log)

    def goMain(self):
        self.back_MainWindow.emit()

    # 选择 file_dir
    def setFileDir(self):
        outputPath = QFileDialog.getExistingDirectory(self, 'Select Path', '.')
        self.lineEdit_2.setText(outputPath)

    # 选择 emi_dir
    def setEmi_dir(self):
        emiPath = QFileDialog.getExistingDirectory(self, 'Select Path', '.')
        self.lineEdit_3.setText(emiPath)

    def runPy_reproduce(self):
        decompilers = self.comboBox.currentText()
        if decompilers == "Other":
            decompilers = self.lineEdit.text()

        file_dir = self.lineEdit_2.text()
        emi_dir = self.lineEdit_3.text()

        is_EMI = ''
        if self.checkBox.isChecked():
            is_EMI = '--EMI'

        if emi_dir != '':
            cmd = f'python3 ./reproduce.py --decompiler {decompilers} --files_dir {file_dir} --emi_dir {emi_dir} {is_EMI}'
        else:
            cmd = f'python3 ./reproduce.py --decompiler {decompilers} --files_dir {file_dir}'

        # cmd = f"ping www.baidu.com"
        self.reproduce_log(cmd+'\n')
        self.cmd_thread.cmd = cmd
        self.cmd_thread.start()

    def stopPy_reproduce(self):
        # 杀死进程
        child = subprocess.Popen(["pgrep", "-f", "python3 ./reproduce.py"], stdout=subprocess.PIPE, shell=False)
        pids = str(child.communicate()[0], encoding='utf-8')
        if not pids:
            self.reproduce_log("no target pid to kill, please check")
        os.system("kill -9 " + pids)
        print("stopPy_reproduce")

    def reproduce_log(self, string):
        self.textBrowser.insertPlainText(string)
        textCursor = self.textBrowser.textCursor()
        # 滚动到底部
        textCursor.movePosition(textCursor.End)
        # 设置光标到text中去
        self.textBrowser.setTextCursor(textCursor)

# readme 窗口
class ReadmeWindow(QtWidgets.QWidget, readme_Ui):
    back_MainWindow = QtCore.pyqtSignal()
    def __init__(self):
        super(ReadmeWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.goMain)
    def goMain(self):
        self.back_MainWindow.emit()

# 利用一个控制器来控制界面跳转
class Controller():
    def __init__(self):
        pass

    # 跳转到 main
    def show_main(self):
        self.main = MainWindow()
        self.run = RunWindow()
        self.reproduce = ReproduceWindow()
        self.readme = ReadmeWindow()

        self.main.switch_window1.connect(self.show_run)
        self.main.switch_window2.connect(self.show_reproduce)
        self.main.switch_window3.connect(self.show_readme)
        self.main.show()
        self.run.close()
        self.readme.close()
        self.reproduce.close()

    def show_run(self):
        self.run.back_MainWindow.connect(self.show_main)
        self.main.close()
        self.run.show()

    def show_reproduce(self):
        self.reproduce.back_MainWindow.connect(self.show_main)
        self.main.close()
        self.reproduce.show()

    def show_readme(self):
        self.readme.back_MainWindow.connect(self.show_main)
        self.main.close()
        self.readme.show()


class Cmder(QThread):
    log = pyqtSignal(str)

    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd

    def run(self):
        try:
            p = subprocess.Popen(
                #self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
                self.cmd, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT
            )
            for line in iter(p.stdout.readline, b""):
                try:
                    line = line.decode("utf-8")
                except:
                    line = line.decode("gbk")
                self.log.emit(line)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())
