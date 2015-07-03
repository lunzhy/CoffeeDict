#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from coffeedict.main_window import MainWindow
# from pyshanbay.config import ShanbayConfig, DebugLog
# from pyshanbay.utils import *
import ctypes


if __name__ == '__main__':

    myappid = 'CoffeDict'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtGui.QApplication(sys.argv)

    main_form = MainWindow()
    main_form.show()
    sys.exit(app.exec_())
