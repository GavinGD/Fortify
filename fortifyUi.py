# Form implementation generated from reading ui file 'fortify.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 708)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tableBtnLayout = QtWidgets.QHBoxLayout()
        self.tableBtnLayout.setObjectName("tableBtnLayout")
        self.filterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.filterBtn.setObjectName("filterBtn")
        self.tableBtnLayout.addWidget(self.filterBtn)
        self.natBtn = QtWidgets.QPushButton(self.centralwidget)
        self.natBtn.setObjectName("natBtn")
        self.tableBtnLayout.addWidget(self.natBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.tableBtnLayout.addItem(spacerItem)
        self.verticalLayout_16.addLayout(self.tableBtnLayout)
        self.tablesLayout = QtWidgets.QVBoxLayout()
        self.tablesLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.tablesLayout.setObjectName("tablesLayout")
        self.inputLayout = QtWidgets.QVBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.inputLblLayout = QtWidgets.QHBoxLayout()
        self.inputLblLayout.setObjectName("inputLblLayout")
        self.inputLbl = QtWidgets.QLabel(self.centralwidget)
        self.inputLbl.setObjectName("inputLbl")
        self.inputLblLayout.addWidget(self.inputLbl)
        self.inputPolicyLbl = QtWidgets.QLabel(self.centralwidget)
        self.inputPolicyLbl.setObjectName("inputPolicyLbl")
        self.inputLblLayout.addWidget(self.inputPolicyLbl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.inputLblLayout.addItem(spacerItem1)
        self.addRuleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addRuleBtn.setObjectName("addRuleBtn")
        self.inputLblLayout.addWidget(self.addRuleBtn)
        self.inputLayout.addLayout(self.inputLblLayout)
        self.inputTable = QtWidgets.QTableWidget(self.centralwidget)
        self.inputTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.inputTable.setObjectName("inputTable")
        self.inputTable.setColumnCount(7)
        self.inputTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputTable.setHorizontalHeaderItem(6, item)
        self.inputTable.horizontalHeader().setSortIndicatorShown(False)
        self.inputTable.horizontalHeader().setStretchLastSection(False)
        self.inputLayout.addWidget(self.inputTable)
        self.tablesLayout.addLayout(self.inputLayout)
        self.forwardLayout = QtWidgets.QVBoxLayout()
        self.forwardLayout.setObjectName("forwardLayout")
        self.forwardLblLayout = QtWidgets.QHBoxLayout()
        self.forwardLblLayout.setObjectName("forwardLblLayout")
        self.forwardLbl = QtWidgets.QLabel(self.centralwidget)
        self.forwardLbl.setObjectName("forwardLbl")
        self.forwardLblLayout.addWidget(self.forwardLbl)
        self.forwardPolicyLbl = QtWidgets.QLabel(self.centralwidget)
        self.forwardPolicyLbl.setObjectName("forwardPolicyLbl")
        self.forwardLblLayout.addWidget(self.forwardPolicyLbl)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.forwardLblLayout.addItem(spacerItem2)
        self.forwardLayout.addLayout(self.forwardLblLayout)
        self.forwardTable = QtWidgets.QTableWidget(self.centralwidget)
        self.forwardTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.forwardTable.setObjectName("forwardTable")
        self.forwardTable.setColumnCount(7)
        self.forwardTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.forwardTable.setHorizontalHeaderItem(6, item)
        self.forwardLayout.addWidget(self.forwardTable)
        self.tablesLayout.addLayout(self.forwardLayout)
        self.outputLayout = QtWidgets.QVBoxLayout()
        self.outputLayout.setObjectName("outputLayout")
        self.outputLblLayout = QtWidgets.QHBoxLayout()
        self.outputLblLayout.setObjectName("outputLblLayout")
        self.outputLbl = QtWidgets.QLabel(self.centralwidget)
        self.outputLbl.setObjectName("outputLbl")
        self.outputLblLayout.addWidget(self.outputLbl)
        self.outputPolicyLbl = QtWidgets.QLabel(self.centralwidget)
        self.outputPolicyLbl.setObjectName("outputPolicyLbl")
        self.outputLblLayout.addWidget(self.outputPolicyLbl)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.outputLblLayout.addItem(spacerItem3)
        self.outputLayout.addLayout(self.outputLblLayout)
        self.outputTable = QtWidgets.QTableWidget(self.centralwidget)
        self.outputTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.outputTable.setObjectName("outputTable")
        self.outputTable.setColumnCount(7)
        self.outputTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(6, item)
        self.outputLayout.addWidget(self.outputTable)
        self.tablesLayout.addLayout(self.outputLayout)
        self.verticalLayout_16.addLayout(self.tablesLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 29))
        self.menubar.setObjectName("menubar")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLight_Mode = QtGui.QAction(MainWindow)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.actionDark_Mode = QtGui.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.menuTheme.addSeparator()
        self.menuTheme.addAction(self.actionLight_Mode)
        self.menuTheme.addAction(self.actionDark_Mode)
        self.menuTheme.addSeparator()
        self.menuTheme.addSeparator()
        self.menubar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fortify"))
        self.filterBtn.setText(_translate("MainWindow", "Filter"))
        self.natBtn.setText(_translate("MainWindow", "NAT"))
        self.inputLbl.setText(_translate("MainWindow", "INPUT"))
        self.inputPolicyLbl.setText(_translate("MainWindow", "(Policy ACCEPT)"))
        self.addRuleBtn.setText(_translate("MainWindow", "Add Rule"))
        item = self.inputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.inputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.inputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.inputTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.inputTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SPort"))
        item = self.inputTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DPort"))
        item = self.inputTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "State"))
        self.forwardLbl.setText(_translate("MainWindow", "FORWARD"))
        self.forwardPolicyLbl.setText(_translate("MainWindow", "(Policy ACCEPT)"))
        item = self.forwardTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.forwardTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.forwardTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.forwardTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.forwardTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SPort"))
        item = self.forwardTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DPort"))
        item = self.forwardTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "State"))
        self.outputLbl.setText(_translate("MainWindow", "OUTPUT"))
        self.outputPolicyLbl.setText(_translate("MainWindow", "(Policy ACCEPT)"))
        item = self.outputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.outputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.outputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.outputTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.outputTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SPort"))
        item = self.outputTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DPort"))
        item = self.outputTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "State"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionLight_Mode.setText(_translate("MainWindow", "Light Mode"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))