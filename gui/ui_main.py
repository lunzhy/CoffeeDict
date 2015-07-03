#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_dev.ui'
#
# Created: Fri Jul  3 15:16:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(873, 612)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.edit_word = QtGui.QLineEdit(self.centralwidget)
        self.edit_word.setGeometry(QtCore.QRect(20, 30, 161, 20))
        self.edit_word.setObjectName(_fromUtf8("edit_word"))
        self.list_words = QtGui.QListWidget(self.centralwidget)
        self.list_words.setGeometry(QtCore.QRect(20, 60, 161, 192))
        self.list_words.setObjectName(_fromUtf8("list_words"))
        self.edit_tag = QtGui.QLineEdit(self.centralwidget)
        self.edit_tag.setGeometry(QtCore.QRect(20, 350, 151, 20))
        self.edit_tag.setObjectName(_fromUtf8("edit_tag"))
        self.cbb_hits = QtGui.QComboBox(self.centralwidget)
        self.cbb_hits.setGeometry(QtCore.QRect(20, 510, 111, 22))
        self.cbb_hits.setObjectName(_fromUtf8("cbb_hits"))
        self.btn_hits = QtGui.QPushButton(self.centralwidget)
        self.btn_hits.setGeometry(QtCore.QRect(140, 510, 75, 23))
        self.btn_hits.setObjectName(_fromUtf8("btn_hits"))
        self.label_word_info = QtGui.QLabel(self.centralwidget)
        self.label_word_info.setGeometry(QtCore.QRect(250, 30, 54, 12))
        self.label_word_info.setObjectName(_fromUtf8("label_word_info"))
        self.txt_notes = QtGui.QTextBrowser(self.centralwidget)
        self.txt_notes.setGeometry(QtCore.QRect(260, 70, 471, 181))
        self.txt_notes.setObjectName(_fromUtf8("txt_notes"))
        self.txt_defination = QtGui.QTextBrowser(self.centralwidget)
        self.txt_defination.setGeometry(QtCore.QRect(260, 340, 471, 151))
        self.txt_defination.setObjectName(_fromUtf8("txt_defination"))
        self.btn_word_add = QtGui.QPushButton(self.centralwidget)
        self.btn_word_add.setGeometry(QtCore.QRect(260, 510, 75, 23))
        self.btn_word_add.setObjectName(_fromUtf8("btn_word_add"))
        self.btn_word_del = QtGui.QPushButton(self.centralwidget)
        self.btn_word_del.setGeometry(QtCore.QRect(350, 510, 75, 23))
        self.btn_word_del.setObjectName(_fromUtf8("btn_word_del"))
        self.label_tags_cnt = QtGui.QLabel(self.centralwidget)
        self.label_tags_cnt.setGeometry(QtCore.QRect(750, 50, 54, 12))
        self.label_tags_cnt.setObjectName(_fromUtf8("label_tags_cnt"))
        self.list_word_tags = QtGui.QListWidget(self.centralwidget)
        self.list_word_tags.setGeometry(QtCore.QRect(750, 90, 71, 121))
        self.list_word_tags.setObjectName(_fromUtf8("list_word_tags"))
        self.list_all_tags = QtGui.QListWidget(self.centralwidget)
        self.list_all_tags.setGeometry(QtCore.QRect(20, 380, 151, 121))
        self.list_all_tags.setObjectName(_fromUtf8("list_all_tags"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_hits.setText(_translate("MainWindow", "PushButton", None))
        self.label_word_info.setText(_translate("MainWindow", "TextLabel", None))
        self.btn_word_add.setText(_translate("MainWindow", "PushButton", None))
        self.btn_word_del.setText(_translate("MainWindow", "PushButton", None))
        self.label_tags_cnt.setText(_translate("MainWindow", "TextLabel", None))

