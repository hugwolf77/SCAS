
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
import numpy as np
np.printoptions(linewidth=np.inf)
import pandas as pd

# pyside6 window
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice 
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtUiTools import QUiLoader
# ui_from
from app.ui.FAtool import Ui_MainWindow

# factor analysis lib
from app.utils.FA import EFA_tool

class seekerEFA(QMainWindow, Ui_MainWindow):
    __MAX_WIN = 1
    __INST_created = 0
    
    def __new__(cls):
        if (cls.__INST_created > cls.__MAX_WIN):
            raise ValueError("Cannot create more objects")
        cls.__INST_created += 1
        return super().__new__(cls)
        
    def __init__(self):
        super(seekerEFA, self).__init__()
        self.window= self.SetupUI()
        self.window.setWindowTitle('[TimeSeries-Seeker] Exporator-Factor-Analsys')
        self.file_navi=QFileDialog
        self.EFA_tool=EFA_tool

        # select data file
        self.rawData = pd.DataFrame()
        self.window.path_btn.clicked.connect(self.file_exeplore)
        self.window.path_edit.returnPressed.connect(self.Input_path)   
        self.window.load.clicked.connect(self.Load_data)
        self.select_data = ''

        # factor fitting btn
        self.window.fitting_btn.clicked.connect(self.FactorAly)
        self.window.show_result.clicked.connect(self.ShowResult)
        self.window.clear_faout_btn.clicked.connect(self.clear_out)

        self.window.show()

    ### Data load - file path
    @QtCore.Slot()
    def file_exeplore(self):
        self.select_data = self.file_navi.getOpenFileName(None, "Select File")[0]
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

        self.rawData = self.rawData.set_index('date')
        # print(self.rawData)

    #### FAtool
    @QtCore.Slot()
    def FactorAly(self):
        self.index = self.rawData.index
        self.columns = self.rawData.columns 

        print(self.rawData.shape)

        FA = EFA_tool(self.rawData, scale=True, drop_Na=False)
        if self.window.rotation_comboBox.currentText().split(sep=' ')[0] == 'None': rotation_set = None 
        else: rotation_set = self.window.rotation_comboBox.currentText().split(sep=' ')[0]

        self.fa, self.fa_result = FA.faAnly(
                n_factors=self.window.fa_num_spin.value(),
                rotation= rotation_set,
                method= self.window.fitting_comboBox.currentText().split(sep=' ')[0],
                smc=self.window.use_smc_ckbox.isChecked(),
                is_corr_matrix=self.window.is_corr_mat_ckbox.isChecked(),
                bounds=tuple((self.window.Lower_bound.value(),self.window.Upper_bound.value())),
                impute=self.window.impute_comboBox.currentText(),
                svd_method=self.window.fitting_comboBox_2.currentText().split(sep=' ')[0],
                rotation_kwargs=None
                )
        # print(f"fitting result : {self.fa_result},  Type: {type(self.fa_result)}")
        self.window.result_out.setAcceptRichText(True)
        self.window.result_out.setOpenExternalLinks(False)
        self.window.result_out.append(str(self.fa_result))

    @QtCore.Slot()
    def ShowResult(self):
        if (self.fa != None) and (self.fa_result != None):
            if self.window.fa_loading_ckbox.isChecked():
                self.window.result_out.append('\n')
                self.window.result_out.append(f"{'-'*(55-(len(self.window.fa_loading_ckbox.text()))//2)}{self.window.fa_loading_ckbox.text()}{'-'*(55-(len(self.window.fa_loading_ckbox.text()))//2)}")
                self.window.result_out.append('\n')
                self.window.result_out.append(str(pd.DataFrame(np.round(self.fa_result.loadings_,3), index=self.rawData.columns)))
            if self.window.fa_comm_ckbox.isChecked():
                self.window.result_out.append('\n')
                self.window.result_out.append(f"{'-'*(55-(len(self.window.fa_comm_ckbox.text()))//2)}{self.window.fa_comm_ckbox.text()}{'-'*(55-(len(self.window.fa_comm_ckbox.text()))//2)}")
                self.window.result_out.append('\n')
                self.window.result_out.append(str(self.fa_result.get_communalities()))
            if self.window.fa_eigenv_ckbox.isChecked():
                self.window.result_out.append('\n')
                self.window.result_out.append(f"{'-'*(55-(len(self.window.fa_eigenv_ckbox.text()))//2)}{self.window.fa_eigenv_ckbox.text()}{'-'*(55-(len(self.window.fa_eigenv_ckbox.text()))//2)}")
                self.window.result_out.append('\n')
                self.window.result_out.append(str(self.fa_result.get_eigenvalues()))
            if self.window.fa_var_ckbox.isChecked():
                self.window.result_out.append('\n')
                self.window.result_out.append(f"{'-'*(55-(len(self.window.fa_var_ckbox.text()))//2)}{self.window.fa_var_ckbox.text()}{'-'*(55-(len(self.window.fa_var_ckbox.text()))//2)}")
                self.window.result_out.append('\n')
                self.window.result_out.append(str(self.fa_result.get_factor_variance()))
            if self.window.fa_unique_ckbox.isChecked():
                self.window.result_out.append('\n')
                self.window.result_out.append(f"{'-'*(55-(len(self.window.fa_unique_ckbox.text()))//2)}{self.window.fa_unique_ckbox.text()}{'-'*(55-(len(self.window.fa_unique_ckbox.text()))//2)}")
                self.window.result_out.append('\n')
                self.window.result_out.append(str(self.fa_result.get_uniquenesses()))

        else:
            self.window.result_out.append('You must first perform a factor analysis.')
    
    ### clear result out
    @QtCore.Slot()
    def clear_out(self):
        self.window.result_out.clear()

    #### init
    def SetupUI(self):
        ui_file_name = resource_path("app/ui/FAtool.ui")
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