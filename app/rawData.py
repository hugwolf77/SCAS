# client app by pyside6
import sys
import os
# from datetime import datetime
# from pytz import timezone

import pandas as pd

# pyside6 window
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice 
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtUiTools import QUiLoader


class ETL(QWidget):
    __MAX_WIN = 1
    __INST_created = 0
    
    def __new__(cls):
        if (cls.__INST_created > cls.__MAX_WIN):
            raise ValueError("Cannot create more objects")
        cls.__INST_created += 1
        return super().__new__(cls)
    
    def __init__(self):
        super(ETL, self).__init__()
        self.window = self.SetupUI()
        self.file_navi = QFileDialog()
        self.window.setWindowTitle('TimeSeries-Seeker')

        # select data file
        self.window.Path_edit.returnPressed.connect(self.Input_path)   
        self.window.Path_btn.clicked.connect(self.file_exeplore)
        self.window.Load.clicked.connect(self.Load_data)
        self.select_data = ''

        # rawData
        self.rawData = pd.DataFrame()
        self.window.DataViewTable.itemClicked.connect(self.on_item_clicked)

        self.window.show()

    def SetupUI(self):
        ui_file_name = resource_path("./GUI/ui/rawData.ui")
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

    # get tableWidget column from clicked item
    def on_item_clicked(self, item):
        column = item.column()
        # 컬럼 헤더에 접근
        header = self.window.DataViewTable.horizontalHeaderItem(column)
        # label_text = header.sectionText(column)
        print(f"클릭된 열: {column}, 레이블 이름: {header.text()}")

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
        self.window.Path_edit.setText(self.select_data)
        self.window.select_path_print.setText(self.select_data)
        headerRow = self.window.Header_int.value()
        if self.window.Index_col.text() == '' : indexCol = None 
        else: indexCol = self.window.Index_col.text()

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

def RunETL():
    app = QApplication(sys.argv)
    view = ETL()
    sys.exit(app.exec())
   
if __name__ == "__main__":
    RunETL()