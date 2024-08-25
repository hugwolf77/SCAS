
'''
    Factor Analysis

    라이브러리 factor-analyzer = "0.5.1"  사용하여
    데이터의 요인분석을 진행하는 폼을 작성

    2024.08.22
'''

import sys
import os
# from datetime import datetime
# from pytz import timezone

import pandas as pd
# normal distribution test
from scipy.stats import shapiro, kstest
from statsmodels.stats.diagnostic import kstest_normal
from scipy.stats import probplot

# bartlett's, KMO test for equel distribution
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# foctor analysis
from factor_analyzer.factor_analyzer import FactorAnalyzer
from statsmodels.multivariate.factor import Factor

# pyside6 window
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice 
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtUiTools import QUiLoader

from GUI.ui.FAtool import Ui_MainWindow

class seekerEFA(QMainWindow):
    __MAX_WIN = 1
    __INST_created = 0
    
    def __new__(cls):
        if (cls.__INST_created > cls.__MAX_WIN):
            raise ValueError("Cannot create more objects")
        cls.__INST_created += 1
        return super().__new__(cls)
        
    def __init__(self):
        super(seekerEFA, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.file_navi=QFileDialog

        # select data file
        self.window.path_btn.clicked.connect(self.file_exeplore)
        self.window.path_edit.returnPressed.connect(self.Input_path)   
        self.window.load.clicked.connect(self.Load_data)
        self.select_data = ''
        self.show()

    @QtCore.Slot()
    def file_exeplore(self):
        self.window.select_data = self.file_navi.getOpenFileName(None, "Select File")[0]
        self.window.path_edit.setText(self.select_data)
        self.window.path_print.setText(self.select_data)

    @QtCore.Slot()
    def Input_path(self):
        edit_path = self.window.path_edit.text()
        print(f"Enter Path: {edit_path}")
        self.window.path_edit.setText(edit_path)

    @QtCore.Slot()
    def Load_data(self):
        self.window.path_edit.setText(self.select_data)
        self.window.path_print.setText(self.select_data)
        headerRow = self.window.header_row.value()
        if self.window.indexCol_edit.text() == '' : indexCol = None 
        else: indexCol = self.window.indexCol_edit.text()

        if os.path.splitext(self.select_data)[1] == '.csv':
            self.rawData = pd.read_csv(self.select_data, header=headerRow, index_col=indexCol)
        elif os.path.splitext(self.select_data)[1] == '.xlsx':
            self.rawData =  pd.read_excel(self.select_data, header=headerRow, index_col=indexCol)

        self.rawData = self.rawData.reset_index()
        # self.rawData['date'] = pd.to_datetime(self.rawData[indexCol])
        rowCount, colCount = self.rawData.shape[0], self.rawData.shape[1]
        # print(indexCol)
        # print(rowCount,colCount)
        # print(self.rawData.index)

        # view widget table form setting
        self.window.DataViewTable.setColumnCount(colCount)
        self.window.DataViewTable.setHorizontalHeaderLabels(self.rawData.columns)
        self.window.DataViewTable.setRowCount(rowCount)

        # view widget table data setting
        for r in range(rowCount):
            for c in range(colCount):
                self.window.DataViewTable.setItem(r,c, QTableWidgetItem(str(self.rawData.iloc[r,c])))

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def RunEFA():
    app = QApplication(sys.argv)
    view = seekerEFA()
    sys.exit(app.exec())

if __name__ == "__main__":
    RunEFA()