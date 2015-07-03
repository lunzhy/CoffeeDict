#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from gui.ui_main import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()