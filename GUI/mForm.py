# client app by pyside6
import sys
import os
from datetime import datetime
from pytz import timezone
from DB.dataloader import dataloader

# pyside6 window
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice 
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtUiTools import QUiLoader


class mForm(QWidget):
    __MAX_WIN = 1
    __INST_created = 0
    
    def __new__(cls):
        if (cls.__INST_created > cls.__MAX_WIN):
            raise ValueError("Cannot create more objects")
        cls.__INST_created += 1
        return super().__new__(cls)
    
    def __init__(self):
        super(mForm, self).__init__()
        self.window = self.SetupUI()
        self.file_navi = QFileDialog()
        self.window.setWindowTitle('TimeSeries-Seeker')

        # select data
        self.window.Path_edit.returnPressed.connect(self.Input_path)   
        self.window.Path_btn.clicked.connect(self.file_exeplore)
        self.window.Load.clicked.connect(self.Load_data)
        self.select_data = ''

        self.window.show()

    def SetupUI(self):
        ui_file_name = resource_path("./GUI/ui/main.ui")
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        window =loader.load(ui_file)
        ui_file.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)
        return window 

    @QtCore.Slot()
    def Input_path(self):
        edit_path = self.window.Path_edit.text()
        print(f"Enter Path: {edit_path}")
        self.window.Path_edit.setText(edit_path)

    @QtCore.Slot()
    def file_exeplore(self):
        self.select_data = self.file_navi.getOpenFileName(None, "Select File")[0]
        self.window.Path_edit.setText(self.select_data)
        self.window.select_path_print.setText(self.select_data)

    @QtCore.Slot()
    def Load_data(self):
        self.window.path_edit.setText(self.select_data)
        self.window.edit_path_print.setText(self.select_data)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def appRun():
    app = QApplication(sys.argv)
    view = mForm()
    sys.exit(app.exec())
   
if __name__ == "__main__":
    appRun()