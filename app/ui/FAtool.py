# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FAtool.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle('[TimeSeries-Seeker] Exporator-Factor-Analsys')
        MainWindow.setEnabled(True)
        MainWindow.resize(1085, 872)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RawDataLoad = QGroupBox(self.centralwidget)
        self.RawDataLoad.setObjectName(u"RawDataLoad")
        self.RawDataLoad.setGeometry(QRect(620, 10, 449, 139))
        self.path_print = QLabel(self.RawDataLoad)
        self.path_print.setObjectName(u"path_print")
        self.path_print.setGeometry(QRect(10, 30, 341, 31))
        self.path_print.setFrameShape(QFrame.Shape.Box)
        self.path_print.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.path_btn = QPushButton(self.RawDataLoad)
        self.path_btn.setObjectName(u"path_btn")
        self.path_btn.setGeometry(QRect(360, 30, 81, 31))
        self.path_edit = QLineEdit(self.RawDataLoad)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setGeometry(QRect(10, 70, 341, 31))
        self.path_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load = QPushButton(self.RawDataLoad)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(360, 70, 81, 31))
        self.header_row = QSpinBox(self.RawDataLoad)
        self.header_row.setObjectName(u"header_row")
        self.header_row.setGeometry(QRect(120, 110, 50, 20))
        font = QFont()
        font.setPointSize(11)
        self.header_row.setFont(font)
        self.header_row.setFrame(True)
        self.headerRow_label = QLabel(self.RawDataLoad)
        self.headerRow_label.setObjectName(u"headerRow_label")
        self.headerRow_label.setGeometry(QRect(20, 110, 91, 17))
        self.headerRow_label.setFont(font)
        self.indexCol_label = QLabel(self.RawDataLoad)
        self.indexCol_label.setObjectName(u"indexCol_label")
        self.indexCol_label.setGeometry(QRect(180, 110, 101, 17))
        self.indexCol_label.setFont(font)
        self.indexCol_edit = QLineEdit(self.RawDataLoad)
        self.indexCol_edit.setObjectName(u"indexCol_edit")
        self.indexCol_edit.setGeometry(QRect(280, 110, 161, 20))
        self.indexCol_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.factorAnalysis = QGroupBox(self.centralwidget)
        self.factorAnalysis.setObjectName(u"factorAnalysis")
        self.factorAnalysis.setGeometry(QRect(620, 160, 451, 321))
        self.path_btn_2 = QPushButton(self.factorAnalysis)
        self.path_btn_2.setObjectName(u"path_btn_2")
        self.path_btn_2.setGeometry(QRect(20, 280, 411, 31))
        self.faNum_label = QLabel(self.factorAnalysis)
        self.faNum_label.setObjectName(u"faNum_label")
        self.faNum_label.setGeometry(QRect(20, 30, 101, 21))
        self.rotation_label = QLabel(self.factorAnalysis)
        self.rotation_label.setObjectName(u"rotation_label")
        self.rotation_label.setGeometry(QRect(160, 30, 121, 17))
        self.rotation_comboBox = QComboBox(self.factorAnalysis)
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.addItem("")
        self.rotation_comboBox.setObjectName(u"rotation_comboBox")
        self.rotation_comboBox.setGeometry(QRect(160, 50, 271, 31))
        self.fa_num_spin = QSpinBox(self.factorAnalysis)
        self.fa_num_spin.setObjectName(u"fa_num_spin")
        self.fa_num_spin.setGeometry(QRect(20, 50, 121, 31))
        self.fa_num_spin.setMinimum(0)
        self.fa_num_spin.setValue(0)
        self.fitting_comboBox = QComboBox(self.factorAnalysis)
        self.fitting_comboBox.addItem("")
        self.fitting_comboBox.addItem("")
        self.fitting_comboBox.addItem("")
        self.fitting_comboBox.setObjectName(u"fitting_comboBox")
        self.fitting_comboBox.setGeometry(QRect(160, 110, 271, 31))
        self.fitting_label = QLabel(self.factorAnalysis)
        self.fitting_label.setObjectName(u"fitting_label")
        self.fitting_label.setGeometry(QRect(160, 90, 121, 17))
        self.use_smc_ckbox = QCheckBox(self.factorAnalysis)
        self.use_smc_ckbox.setObjectName(u"use_smc_ckbox")
        self.use_smc_ckbox.setGeometry(QRect(180, 220, 91, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.use_smc_ckbox.setFont(font1)
        self.is_corr_mat_ckbox = QCheckBox(self.factorAnalysis)
        self.is_corr_mat_ckbox.setObjectName(u"is_corr_mat_ckbox")
        self.is_corr_mat_ckbox.setGeometry(QRect(280, 220, 131, 31))
        self.is_corr_mat_ckbox.setFont(font1)
        self.impute_comboBox = QComboBox(self.factorAnalysis)
        self.impute_comboBox.addItem("")
        self.impute_comboBox.addItem("")
        self.impute_comboBox.addItem("")
        self.impute_comboBox.setObjectName(u"impute_comboBox")
        self.impute_comboBox.setGeometry(QRect(20, 110, 121, 31))
        self.impute_label = QLabel(self.factorAnalysis)
        self.impute_label.setObjectName(u"impute_label")
        self.impute_label.setGeometry(QRect(20, 90, 121, 17))
        self.fitting_comboBox_2 = QComboBox(self.factorAnalysis)
        self.fitting_comboBox_2.addItem("")
        self.fitting_comboBox_2.addItem("")
        self.fitting_comboBox_2.setObjectName(u"fitting_comboBox_2")
        self.fitting_comboBox_2.setGeometry(QRect(20, 160, 411, 31))
        self.fitting_label_2 = QLabel(self.factorAnalysis)
        self.fitting_label_2.setObjectName(u"fitting_label_2")
        self.fitting_label_2.setGeometry(QRect(20, 140, 411, 17))
        font2 = QFont()
        font2.setPointSize(10)
        self.fitting_label_2.setFont(font2)
        self.Upper_bound = QDoubleSpinBox(self.factorAnalysis)
        self.Upper_bound.setObjectName(u"Upper_bound")
        self.Upper_bound.setGeometry(QRect(80, 220, 81, 21))
        self.Lower_bound = QDoubleSpinBox(self.factorAnalysis)
        self.Lower_bound.setObjectName(u"Lower_bound")
        self.Lower_bound.setGeometry(QRect(80, 250, 81, 21))
        self.Lower_bound.setDecimals(3)
        self.Lower_bound.setMinimum(0.005000000000000)
        self.Lower_bound.setMaximum(1.000000000000000)
        self.Lower_bound.setSingleStep(0.005000000000000)
        self.Lower_bound.setValue(0.005000000000000)
        self.bound_label = QLabel(self.factorAnalysis)
        self.bound_label.setObjectName(u"bound_label")
        self.bound_label.setGeometry(QRect(20, 200, 67, 17))
        font3 = QFont()
        font3.setPointSize(12)
        self.bound_label.setFont(font3)
        self.upper_label = QLabel(self.factorAnalysis)
        self.upper_label.setObjectName(u"upper_label")
        self.upper_label.setGeometry(QRect(30, 220, 51, 17))
        self.upper_label.setFont(font)
        self.lower_label = QLabel(self.factorAnalysis)
        self.lower_label.setObjectName(u"lower_label")
        self.lower_label.setGeometry(QRect(30, 250, 51, 17))
        self.lower_label.setFont(font)
        self.otherOP_label = QLabel(self.factorAnalysis)
        self.otherOP_label.setObjectName(u"otherOP_label")
        self.otherOP_label.setGeometry(QRect(170, 200, 161, 17))
        self.otherOP_label.setFont(font3)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(620, 490, 451, 321))
        self.fa_loading_ckbox = QCheckBox(self.groupBox)
        self.fa_loading_ckbox.setObjectName(u"fa_loading_ckbox")
        self.fa_loading_ckbox.setGeometry(QRect(20, 50, 91, 31))
        self.fa_loading_ckbox.setFont(font1)
        self.result_output_label = QLabel(self.groupBox)
        self.result_output_label.setObjectName(u"result_output_label")
        self.result_output_label.setGeometry(QRect(10, 30, 161, 17))
        self.result_output_label.setFont(font1)
        self.fa_comm_ckbox = QCheckBox(self.groupBox)
        self.fa_comm_ckbox.setObjectName(u"fa_comm_ckbox")
        self.fa_comm_ckbox.setGeometry(QRect(130, 50, 141, 31))
        self.fa_comm_ckbox.setFont(font1)
        self.fa_eigenv_ckbox = QCheckBox(self.groupBox)
        self.fa_eigenv_ckbox.setObjectName(u"fa_eigenv_ckbox")
        self.fa_eigenv_ckbox.setGeometry(QRect(280, 50, 141, 31))
        self.fa_eigenv_ckbox.setFont(font1)
        self.fa_var_ckbox = QCheckBox(self.groupBox)
        self.fa_var_ckbox.setObjectName(u"fa_var_ckbox")
        self.fa_var_ckbox.setGeometry(QRect(20, 90, 141, 31))
        self.fa_var_ckbox.setFont(font1)
        self.fa_unique_ckbox = QCheckBox(self.groupBox)
        self.fa_unique_ckbox.setObjectName(u"fa_unique_ckbox")
        self.fa_unique_ckbox.setGeometry(QRect(160, 90, 141, 31))
        self.fa_unique_ckbox.setFont(font1)
        self.suffi_label = QLabel(self.groupBox)
        self.suffi_label.setObjectName(u"suffi_label")
        self.suffi_label.setGeometry(QRect(10, 130, 171, 31))
        self.suffi_label.setFont(font1)
        self.suffi_do_btn = QPushButton(self.groupBox)
        self.suffi_do_btn.setObjectName(u"suffi_do_btn")
        self.suffi_do_btn.setGeometry(QRect(280, 130, 151, 31))
        self.suffi_obs_num_spin = QSpinBox(self.groupBox)
        self.suffi_obs_num_spin.setObjectName(u"suffi_obs_num_spin")
        self.suffi_obs_num_spin.setGeometry(QRect(180, 130, 81, 31))
        self.suffi_obs_num_spin.setMinimum(0)
        self.suffi_obs_num_spin.setValue(0)
        self.suffi_do_btn_2 = QPushButton(self.groupBox)
        self.suffi_do_btn_2.setObjectName(u"suffi_do_btn_2")
        self.suffi_do_btn_2.setGeometry(QRect(290, 280, 151, 31))
        self.suffi_label_2 = QLabel(self.groupBox)
        self.suffi_label_2.setObjectName(u"suffi_label_2")
        self.suffi_label_2.setGeometry(QRect(10, 170, 271, 31))
        self.suffi_label_2.setFont(font3)
        self.path_btn_3 = QPushButton(self.groupBox)
        self.path_btn_3.setObjectName(u"path_btn_3")
        self.path_btn_3.setGeometry(QRect(360, 200, 81, 31))
        self.path_print_2 = QLabel(self.groupBox)
        self.path_print_2.setObjectName(u"path_print_2")
        self.path_print_2.setGeometry(QRect(10, 200, 341, 31))
        self.path_print_2.setFrameShape(QFrame.Shape.Box)
        self.path_print_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.path_edit_2 = QLineEdit(self.groupBox)
        self.path_edit_2.setObjectName(u"path_edit_2")
        self.path_edit_2.setGeometry(QRect(10, 237, 341, 31))
        self.path_edit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load_2 = QPushButton(self.groupBox)
        self.load_2.setObjectName(u"load_2")
        self.load_2.setGeometry(QRect(360, 237, 81, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 601, 811))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DataFrameView = QGroupBox(self.widget)
        self.DataFrameView.setObjectName(u"DataFrameView")
        self.DataViewTable = QTableWidget(self.DataFrameView)
        self.DataViewTable.setObjectName(u"DataViewTable")
        self.DataViewTable.setGeometry(QRect(10, 30, 581, 321))
        self.result = QGroupBox(self.DataFrameView)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(0, 350, 599, 331))
        self.result_out = QTextBrowser(self.result)
        self.result_out.setObjectName(u"result_out")
        self.result_out.setGeometry(QRect(10, 30, 581, 291))
        self.groupBox_2 = QGroupBox(self.DataFrameView)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 680, 581, 121))

        self.verticalLayout.addWidget(self.DataFrameView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1085, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RawDataLoad.setTitle(QCoreApplication.translate("MainWindow", u" Data Load", None))
        self.path_print.setText(QCoreApplication.translate("MainWindow", u"Select file path", None))
        self.path_btn.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.path_edit.setText(QCoreApplication.translate("MainWindow", u"Input data file path edit", None))
        self.load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.headerRow_label.setText(QCoreApplication.translate("MainWindow", u"Header Row", None))
        self.indexCol_label.setText(QCoreApplication.translate("MainWindow", u"Index column", None))
        self.indexCol_edit.setText("")
        self.factorAnalysis.setTitle(QCoreApplication.translate("MainWindow", u" Exploratory Factor Analysis", None))
        self.path_btn_2.setText(QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.faNum_label.setText(QCoreApplication.translate("MainWindow", u"Factor Number", None))
        self.rotation_label.setText(QCoreApplication.translate("MainWindow", u"Rotation Method", None))
        self.rotation_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.rotation_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"varimax (orthogonal rotation)", None))
        self.rotation_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"promax (oblique rotation)", None))
        self.rotation_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"oblimin (oblique rotation)", None))
        self.rotation_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"oblimax (orthogonal rotation)", None))
        self.rotation_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"quartimin (oblique rotation)", None))
        self.rotation_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"quartimax (orthogonal rotation)", None))
        self.rotation_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"equamax (orthogonal rotation)", None))

        self.fitting_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Minimal Residual Method (MINRES)", None))
        self.fitting_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Maximum Likehood Estimate (MLE)", None))
        self.fitting_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Principal Component Analysis (PCA)", None))

        self.fitting_label.setText(QCoreApplication.translate("MainWindow", u"Fitting Method", None))
        self.use_smc_ckbox.setText(QCoreApplication.translate("MainWindow", u"use_smc", None))
        self.is_corr_mat_ckbox.setText(QCoreApplication.translate("MainWindow", u"is_corr_matrix", None))
        self.impute_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"median", None))
        self.impute_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"mean", None))
        self.impute_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"drop", None))

        self.impute_label.setText(QCoreApplication.translate("MainWindow", u"miss data impute", None))
        self.fitting_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"randomized (faster randomized SVD from scikit-learn)", None))
        self.fitting_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"lapack (standard SVD from scipy)", None))

        self.fitting_label_2.setText(QCoreApplication.translate("MainWindow", u"If the fitting method is PCA, select the decomposition method", None))
        self.bound_label.setText(QCoreApplication.translate("MainWindow", u"Bound", None))
        self.upper_label.setText(QCoreApplication.translate("MainWindow", u"Upper ", None))
        self.lower_label.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.otherOP_label.setText(QCoreApplication.translate("MainWindow", u"other options", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Result Output", None))
        self.fa_loading_ckbox.setText(QCoreApplication.translate("MainWindow", u"Loadings", None))
        self.result_output_label.setText(QCoreApplication.translate("MainWindow", u"Fitting Result Output", None))
        self.fa_comm_ckbox.setText(QCoreApplication.translate("MainWindow", u"Communalities", None))
        self.fa_eigenv_ckbox.setText(QCoreApplication.translate("MainWindow", u"Eigenvalues", None))
        self.fa_var_ckbox.setText(QCoreApplication.translate("MainWindow", u"factor variance", None))
        self.fa_unique_ckbox.setText(QCoreApplication.translate("MainWindow", u"uniquenesses", None))
        self.suffi_label.setText(QCoreApplication.translate("MainWindow", u"Sufficiency :  obs num", None))
        self.suffi_do_btn.setText(QCoreApplication.translate("MainWindow", u"Do", None))
        self.suffi_do_btn_2.setText(QCoreApplication.translate("MainWindow", u"Transform", None))
        self.suffi_label_2.setText(QCoreApplication.translate("MainWindow", u"Get factor scores for a new data set", None))
        self.path_btn_3.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.path_print_2.setText(QCoreApplication.translate("MainWindow", u"Select file path", None))
        self.path_edit_2.setText(QCoreApplication.translate("MainWindow", u"Input data file path", None))
        self.load_2.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.DataFrameView.setTitle(QCoreApplication.translate("MainWindow", u"  Data Frame View", None))
        self.result.setTitle(QCoreApplication.translate("MainWindow", u"  Result View", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

