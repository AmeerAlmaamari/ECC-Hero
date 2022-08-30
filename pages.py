# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pages.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import start_pic

class move_widget(QtWidgets.QWidget):
        def __init__(self,parent=None):
                super(move_widget, self).__init__(parent)
                self.parent= parent
        def mousePressEvent(self, event):
                if event.button() == QtCore.Qt.LeftButton:
                        self.dragPosition = event.globalPos() - self.parent.frameGeometry().topLeft()
                        event.accept()
        def mouseMoveEvent(self, event):
                if event.buttons() == QtCore.Qt.LeftButton:
                        self.parent.move(event.globalPos() - self.dragPosition)
                        event.accept()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 645)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = move_widget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(99, 90, 801, 471))
        self.stackedWidget.setStyleSheet("border-radius:20px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.label_6 = QtWidgets.QLabel(self.start_page)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.start_page)
        self.label_7.setGeometry(QtCore.QRect(30, 190, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.start_page)
        self.label_8.setGeometry(QtCore.QRect(10, 440, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Unispace\";")
        self.label_8.setObjectName("label_8")
        self.duplicates_rem_button = QtWidgets.QPushButton(self.start_page)
        self.duplicates_rem_button.setGeometry(QtCore.QRect(440, 180, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.duplicates_rem_button.setFont(font)
        self.duplicates_rem_button.setStyleSheet("QPushButton#duplicates_rem_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#duplicates_rem_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#duplicates_rem_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.duplicates_rem_button.setObjectName("duplicates_rem_button")
        self.main_frame1 = QtWidgets.QLabel(self.start_page)
        self.main_frame1.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.main_frame1.setStyleSheet("border-image: url(:/images/3648482.png);\n"
"border-radius:20px;")
        self.main_frame1.setText("")
        self.main_frame1.setObjectName("main_frame1")
        self.files_encrypt_button = QtWidgets.QPushButton(self.start_page)
        self.files_encrypt_button.setGeometry(QtCore.QRect(440, 300, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.files_encrypt_button.setFont(font)
        self.files_encrypt_button.setStyleSheet("QPushButton#files_encrypt_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#files_encrypt_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#files_encrypt_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.files_encrypt_button.setObjectName("files_encrypt_button")
        self.label_12 = QtWidgets.QLabel(self.start_page)
        self.label_12.setGeometry(QtCore.QRect(30, 230, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.start_page)
        self.label_13.setGeometry(QtCore.QRect(30, 270, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_13.setObjectName("label_13")
        self.main_frame1.raise_()
        self.label_6.raise_()
        self.duplicates_rem_button.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.files_encrypt_button.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.stackedWidget.addWidget(self.start_page)
        self.folder_select_page = QtWidgets.QWidget()
        self.folder_select_page.setObjectName("folder_select_page")
        self.label_9 = QtWidgets.QLabel(self.folder_select_page)
        self.label_9.setGeometry(QtCore.QRect(430, 80, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_9.setObjectName("label_9")
        self.folder_browser_box = QtWidgets.QLineEdit(self.folder_select_page)
        self.folder_browser_box.setGeometry(QtCore.QRect(430, 160, 321, 31))
        self.folder_browser_box.setStyleSheet("border-radius:5px;")
        self.folder_browser_box.setObjectName("folder_browser_box")
        self.folder_browse_button = QtWidgets.QPushButton(self.folder_select_page)
        self.folder_browse_button.setGeometry(QtCore.QRect(520, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.folder_browse_button.setFont(font)
        self.folder_browse_button.setStyleSheet("QPushButton#folder_browse_button{ \n"
"font: 75 15pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#folder_browse_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#folder_browse_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.folder_browse_button.setObjectName("folder_browse_button")
        self.find_button = QtWidgets.QPushButton(self.folder_select_page)
        self.find_button.setGeometry(QtCore.QRect(390, 380, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton#find_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#find_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#find_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.find_button.setObjectName("find_button")
        self.main_frame2 = QtWidgets.QLabel(self.folder_select_page)
        self.main_frame2.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.main_frame2.setStyleSheet("border-image: url(:/images/3648482.png);\n"
"border-radius:20px;")
        self.main_frame2.setText("")
        self.main_frame2.setObjectName("main_frame2")
        self.folder_back_button = QtWidgets.QPushButton(self.folder_select_page)
        self.folder_back_button.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.folder_back_button.setFont(font)
        self.folder_back_button.setStyleSheet("QPushButton#folder_back_button{ \n"
"font: 75 11pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#folder_back_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#folder_back_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.folder_back_button.setObjectName("folder_back_button")
        self.main_frame2.raise_()
        self.label_9.raise_()
        self.folder_browse_button.raise_()
        self.folder_browser_box.raise_()
        self.find_button.raise_()
        self.folder_back_button.raise_()
        self.stackedWidget.addWidget(self.folder_select_page)
        self.duplicates_page = QtWidgets.QWidget()
        self.duplicates_page.setObjectName("duplicates_page")
        self.label_10 = QtWidgets.QLabel(self.duplicates_page)
        self.label_10.setGeometry(QtCore.QRect(460, 60, 191, 41))
        self.label_10.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 63 24pt \"Open Sans Semibold\";")
        self.label_10.setObjectName("label_10")
        self.files_num = QtWidgets.QLabel(self.duplicates_page)
        self.files_num.setGeometry(QtCore.QRect(620, 60, 151, 41))
        self.files_num.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 24pt \"Open Sans Semibold\";\n"
"background-color: rgb(0, 55, 81);")
        self.files_num.setObjectName("files_num")
        self.label_11 = QtWidgets.QLabel(self.duplicates_page)
        self.label_11.setGeometry(QtCore.QRect(550, 110, 101, 41))
        self.label_11.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 63 24pt \"Open Sans Semibold\";")
        self.label_11.setObjectName("label_11")
        self.delete_button = QtWidgets.QPushButton(self.duplicates_page)
        self.delete_button.setGeometry(QtCore.QRect(440, 210, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("QPushButton#delete_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#delete_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#delete_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.delete_button.setObjectName("delete_button")
        self.stats_button = QtWidgets.QPushButton(self.duplicates_page)
        self.stats_button.setGeometry(QtCore.QRect(490, 410, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.stats_button.setFont(font)
        self.stats_button.setStyleSheet("QPushButton#stats_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#stats_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#stats_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.stats_button.setObjectName("stats_button")
        self.main_frame3 = QtWidgets.QLabel(self.duplicates_page)
        self.main_frame3.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.main_frame3.setStyleSheet("border-image: url(:/images/3648482.png);\n"
"border-radius:20px;")
        self.main_frame3.setText("")
        self.main_frame3.setObjectName("main_frame3")
        self.dup_back_button = QtWidgets.QPushButton(self.duplicates_page)
        self.dup_back_button.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dup_back_button.setFont(font)
        self.dup_back_button.setStyleSheet("QPushButton#dup_back_button{ \n"
"font: 75 11pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#dup_back_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#dup_back_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.dup_back_button.setObjectName("dup_back_button")
        self.isolate_button = QtWidgets.QPushButton(self.duplicates_page)
        self.isolate_button.setGeometry(QtCore.QRect(440, 290, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.isolate_button.setFont(font)
        self.isolate_button.setStyleSheet("QPushButton#isolate_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#isolate_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#isolate_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.isolate_button.setObjectName("isolate_button")
        self.main_frame3.raise_()
        self.label_10.raise_()
        self.stats_button.raise_()
        self.files_num.raise_()
        self.delete_button.raise_()
        self.label_11.raise_()
        self.dup_back_button.raise_()
        self.isolate_button.raise_()
        self.stackedWidget.addWidget(self.duplicates_page)
        self.stats_page = QtWidgets.QWidget()
        self.stats_page.setObjectName("stats_page")
        self.main_frame4 = QtWidgets.QLabel(self.stats_page)
        self.main_frame4.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.main_frame4.setStyleSheet("border-image: url(:/images/images/page4_background.jpg);\n"
"border-radius:20px;")
        self.main_frame4.setText("")
        self.main_frame4.setObjectName("main_frame4")
        self.stats_back_button = QtWidgets.QPushButton(self.stats_page)
        self.stats_back_button.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.stats_back_button.setFont(font)
        self.stats_back_button.setStyleSheet("QPushButton#stats_back_button{ \n"
"font: 75 11pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#stats_back_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#stats_back_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.stats_back_button.setObjectName("stats_back_button")
        self.frame1 = QtWidgets.QFrame(self.stats_page)
        self.frame1.setGeometry(QtCore.QRect(10, 120, 250, 250))
        self.frame1.setMinimumSize(QtCore.QSize(250, 250))
        self.frame1.setMaximumSize(QtCore.QSize(250, 250))
        self.frame1.setStyleSheet("QFrame{\n"
" border:5px solid rgb(149,173,182);\n"
"border-radius: 125px}\n"
"\n"
"QFrame:hover{\n"
"border: 5px solid rgb(47,91,107);}")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.frame1_1 = QtWidgets.QFrame(self.frame1)
        self.frame1_1.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.frame1_1.setMinimumSize(QtCore.QSize(250, 250))
        self.frame1_1.setMaximumSize(QtCore.QSize(250, 250))
        self.frame1_1.setStyleSheet("QFrame{\n"
" border:5px solid rgb(149,173,182);\n"
"border-radius: 125px}\n"
"\n"
"QFrame:hover{\n"
"border: 5px solid rgb(47,91,107);}")
        self.frame1_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_1.setObjectName("frame1_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.num_files_lbl = QtWidgets.QLabel(self.frame1_1)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.num_files_lbl.setFont(font)
        self.num_files_lbl.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.num_files_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.num_files_lbl.setObjectName("num_files_lbl")
        self.verticalLayout.addWidget(self.num_files_lbl)
        self.num_duplicates = QtWidgets.QLabel(self.frame1_1)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(44)
        self.num_duplicates.setFont(font)
        self.num_duplicates.setStyleSheet("border:none;\n"
"color: rgb(149,173,182);")
        self.num_duplicates.setAlignment(QtCore.Qt.AlignCenter)
        self.num_duplicates.setObjectName("num_duplicates")
        self.verticalLayout.addWidget(self.num_duplicates)
        self.num_files_lbl_3 = QtWidgets.QLabel(self.frame1_1)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(13)
        self.num_files_lbl_3.setFont(font)
        self.num_files_lbl_3.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.num_files_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.num_files_lbl_3.setObjectName("num_files_lbl_3")
        self.verticalLayout.addWidget(self.num_files_lbl_3)
        self.frame1_2 = QtWidgets.QFrame(self.stats_page)
        self.frame1_2.setGeometry(QtCore.QRect(270, 120, 250, 250))
        self.frame1_2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame1_2.setMaximumSize(QtCore.QSize(250, 250))
        self.frame1_2.setStyleSheet("QFrame{\n"
" border:5px solid rgb(149,173,182);\n"
"border-radius: 125px}\n"
"\n"
"QFrame:hover{\n"
"border: 5px solid rgb(47,91,107);}")
        self.frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_2.setObjectName("frame1_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.saved_size_lbl = QtWidgets.QLabel(self.frame1_2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(13)
        self.saved_size_lbl.setFont(font)
        self.saved_size_lbl.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.saved_size_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_size_lbl.setObjectName("saved_size_lbl")
        self.verticalLayout_2.addWidget(self.saved_size_lbl)
        self.saved_size = QtWidgets.QLabel(self.frame1_2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(44)
        self.saved_size.setFont(font)
        self.saved_size.setStyleSheet("border:none;\n"
"color: rgb(149,173,182);")
        self.saved_size.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_size.setObjectName("saved_size")
        self.verticalLayout_2.addWidget(self.saved_size)
        self.mb_lbl = QtWidgets.QLabel(self.frame1_2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(13)
        self.mb_lbl.setFont(font)
        self.mb_lbl.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.mb_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.mb_lbl.setObjectName("mb_lbl")
        self.verticalLayout_2.addWidget(self.mb_lbl)
        self.frame1_3 = QtWidgets.QFrame(self.stats_page)
        self.frame1_3.setGeometry(QtCore.QRect(530, 120, 250, 250))
        self.frame1_3.setMinimumSize(QtCore.QSize(250, 250))
        self.frame1_3.setMaximumSize(QtCore.QSize(250, 250))
        self.frame1_3.setStyleSheet("QFrame{\n"
" border:5px solid rgb(149,173,182);\n"
"border-radius: 125px}\n"
"\n"
"QFrame:hover{\n"
"border: 5px solid rgb(47,91,107);}")
        self.frame1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_3.setObjectName("frame1_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.saved_size_lbl_2 = QtWidgets.QLabel(self.frame1_3)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(13)
        self.saved_size_lbl_2.setFont(font)
        self.saved_size_lbl_2.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.saved_size_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_size_lbl_2.setObjectName("saved_size_lbl_2")
        self.verticalLayout_3.addWidget(self.saved_size_lbl_2, 0, QtCore.Qt.AlignHCenter)
        self.removed_size = QtWidgets.QLabel(self.frame1_3)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(44)
        self.removed_size.setFont(font)
        self.removed_size.setStyleSheet("border:none;\n"
"color: rgb(149,173,182);")
        self.removed_size.setAlignment(QtCore.Qt.AlignCenter)
        self.removed_size.setObjectName("removed_size")
        self.verticalLayout_3.addWidget(self.removed_size)
        self.mb_lbl_2 = QtWidgets.QLabel(self.frame1_3)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(11)
        self.mb_lbl_2.setFont(font)
        self.mb_lbl_2.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.mb_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mb_lbl_2.setObjectName("mb_lbl_2")
        self.verticalLayout_3.addWidget(self.mb_lbl_2)
        self.stackedWidget.addWidget(self.stats_page)
        self.file_select_page = QtWidgets.QWidget()
        self.file_select_page.setObjectName("file_select_page")
        self.main_frame5 = QtWidgets.QLabel(self.file_select_page)

        

       
        self.main_frame5.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.main_frame5.setStyleSheet("border-image: url(:/images/3648482.png);\n"
"border-radius:20px;")
        self.main_frame5.setText("")
        self.main_frame5.setObjectName("main_frame5")
        self.file_brwose_button = QtWidgets.QPushButton(self.file_select_page)
        self.file_brwose_button.setGeometry(QtCore.QRect(520, 180, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.file_brwose_button.setFont(font)
        self.file_brwose_button.setStyleSheet("QPushButton#file_brwose_button{ \n"
"font: 75 15pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#file_brwose_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#file_brwose_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.file_brwose_button.setObjectName("file_brwose_button")
        self.label_14 = QtWidgets.QLabel(self.file_select_page)
        self.label_14.setGeometry(QtCore.QRect(450, 60, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Unispace\";")
        self.label_14.setObjectName("label_14")
        self.encrypt_button = QtWidgets.QPushButton(self.file_select_page)
        self.encrypt_button.setGeometry(QtCore.QRect(490, 310, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.encrypt_button.setFont(font)
        self.encrypt_button.setStyleSheet("QPushButton#encrypt_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(195,20,50), stop:1 rgba(74,15,47));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#encrypt_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(237,23,60), stop:1 rgba(98,22,63));\n"
"}\n"
"\n"
"QPushButton#encrypt_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(134,9,31);\n"
"}\n"
"")
        self.encrypt_button.setObjectName("encrypt_button")
        self.file_browser_box = QtWidgets.QLineEdit(self.file_select_page)
        self.file_browser_box.setGeometry(QtCore.QRect(430, 140, 321, 31))
        self.file_browser_box.setStyleSheet("border-radius:5px;")
        self.file_browser_box.setObjectName("file_browser_box")
        self.decrypt_button = QtWidgets.QPushButton(self.file_select_page)
        self.decrypt_button.setGeometry(QtCore.QRect(490, 390, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        self.main_frame1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.duplicates_rem_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.files_encrypt_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))

        self.folder_browse_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.find_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.main_frame2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))

        self.delete_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.isolate_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.main_frame3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.stats_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))

        self.main_frame4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))

        self.file_brwose_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.encrypt_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.decrypt_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.main_frame5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))

        self.decrypt_button.setFont(font)
        self.decrypt_button.setStyleSheet("QPushButton#decrypt_button{ \n"
"font: 75 20pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(52,232,158), stop:1 rgba(15,52,67));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#decrypt_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(56,241,165), stop:1 rgba(21,74,96));\n"
"}\n"
"\n"
"QPushButton#decrypt_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(41,174,119);\n"
"}\n"
"")
        self.decrypt_button.setObjectName("decrypt_button")
        self.file_back_button = QtWidgets.QPushButton(self.file_select_page)
        self.file_back_button.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.file_back_button.setFont(font)
        self.file_back_button.setStyleSheet("QPushButton#file_back_button{ \n"
"font: 75 11pt \"Unispace\";\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#file_back_button:hover{ \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"QPushButton#file_back_button:pressed{\n"
"  padding-left:5px;\n"
"   padding-top:5px;\n"
"   background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")


        self.file_back_button.setObjectName("file_back_button")
        self.stackedWidget.addWidget(self.file_select_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "H"))
        self.label_7.setText(_translate("MainWindow", "ECC"))
        self.label_8.setText(_translate("MainWindow", "Developed by:Ameer Almaamari"))
        self.duplicates_rem_button.setText(_translate("MainWindow", "Duplicates Remover"))
        self.files_encrypt_button.setText(_translate("MainWindow", "Files Encryption"))
        self.label_12.setText(_translate("MainWindow", "R"))
        self.label_13.setText(_translate("MainWindow", "O"))
        self.label_9.setText(_translate("MainWindow", "Select a folder"))
        self.folder_browse_button.setText(_translate("MainWindow", "Browse"))
        self.find_button.setText(_translate("MainWindow", "Find Duplicates"))
        self.folder_back_button.setText(_translate("MainWindow", "Back"))
        self.label_10.setText(_translate("MainWindow", "There are"))
        self.files_num.setText(_translate("MainWindow", "  ####"))
        self.label_11.setText(_translate("MainWindow", "Files !"))
        self.delete_button.setText(_translate("MainWindow", "Delete Duplicates"))
        self.stats_button.setText(_translate("MainWindow", "View Stats"))
        self.dup_back_button.setText(_translate("MainWindow", "Back"))
        self.isolate_button.setText(_translate("MainWindow", "Isolate Duplicates"))
        self.stats_back_button.setText(_translate("MainWindow", "Back"))
        self.num_files_lbl.setText(_translate("MainWindow", "NUMBER OF DUPLICATES"))
        self.num_duplicates.setText(_translate("MainWindow", "25"))
        self.num_files_lbl_3.setText(_translate("MainWindow", "DUPLICATES"))
        self.saved_size_lbl.setText(_translate("MainWindow", "SAVED SIZE"))
        self.saved_size.setText(_translate("MainWindow", "25"))
        self.mb_lbl.setText(_translate("MainWindow", "M B"))
        self.saved_size_lbl_2.setText(_translate("MainWindow", "REMOVED"))
        self.removed_size.setText(_translate("MainWindow", "25%"))
        self.mb_lbl_2.setText(_translate("MainWindow", "From orignal size"))
        self.file_brwose_button.setText(_translate("MainWindow", "Browse"))
        self.label_14.setText(_translate("MainWindow", "Select a file"))
        self.encrypt_button.setText(_translate("MainWindow", "ENCRYPT"))
        self.decrypt_button.setText(_translate("MainWindow", "DECRYPT"))
        self.file_back_button.setText(_translate("MainWindow", "Back"))


