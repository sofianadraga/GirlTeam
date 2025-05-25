from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1917, 960)
        MainMenu.setMinimumSize(QtCore.QSize(1800, 900))
        MainMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainMenu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, \n"
"    stop:0 rgba(57, 0, 95, 255), \n"
"    stop:0.427447 rgba(29, 43, 92, 235), \n"
"    stop:1 rgba(109, 55, 116, 255));")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 1921, 991))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(-5, 0, 291, 981))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 0, 1701, 981))
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setToolTipDuration(2500)
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, \n"
"    stop:0 rgba(100, 50, 150, 200), \n"
"    stop:0.427447 rgba(80, 100, 180, 200), \n"
"    stop:1 rgba(160, 100, 180, 220));\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.GameOfLife = QtWidgets.QWidget()
        self.GameOfLife.setObjectName("GameOfLife")
        self.b_deleteOrigImage0 = QtWidgets.QPushButton(self.GameOfLife)
        self.b_deleteOrigImage0.setGeometry(QtCore.QRect(740, 10, 31, 28))
        self.b_deleteOrigImage0.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteOrigImage0.setObjectName("b_deleteOrigImage0")
        self.b_AddOrigImage0 = QtWidgets.QPushButton(self.GameOfLife)
        self.b_AddOrigImage0.setGeometry(QtCore.QRect(690, 10, 31, 28))
        self.b_AddOrigImage0.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_AddOrigImage0.setObjectName("b_AddOrigImage0")
        self.b_deleteProcImage0 = QtWidgets.QPushButton(self.GameOfLife)
        self.b_deleteProcImage0.setGeometry(QtCore.QRect(1520, 10, 31, 28))
        self.b_deleteProcImage0.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteProcImage0.setObjectName("b_deleteProcImage0")
        self.b_SaveProcImage0 = QtWidgets.QPushButton(self.GameOfLife)
        self.b_SaveProcImage0.setGeometry(QtCore.QRect(1470, 10, 31, 28))
        self.b_SaveProcImage0.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_SaveProcImage0.setObjectName("b_SaveProcImage0")
        self.l_OrigImage = QtWidgets.QLabel(self.GameOfLife)
        self.l_OrigImage.setGeometry(QtCore.QRect(30, 40, 741, 551))
        self.l_OrigImage.setStyleSheet("background:white;")
        self.l_OrigImage.setText("")
        self.l_OrigImage.setObjectName("l_OrigImage")
        self.L_ProcImage = QtWidgets.QLabel(self.GameOfLife)
        self.L_ProcImage.setGeometry(QtCore.QRect(810, 40, 741, 551))
        self.L_ProcImage.setStyleSheet("background:white;")
        self.L_ProcImage.setText("")
        self.L_ProcImage.setObjectName("L_ProcImage")
        self.w_GameOfLife = QtWidgets.QWidget(self.GameOfLife)
        self.w_GameOfLife.setGeometry(QtCore.QRect(30, 610, 741, 241))
        self.w_GameOfLife.setStyleSheet("border: 2px solid rgba(235, 225, 225, 0.9);")
        self.w_GameOfLife.setObjectName("w_GameOfLife")
        self.b_processImageGOF = QtWidgets.QPushButton(self.w_GameOfLife)
        self.b_processImageGOF.setGeometry(QtCore.QRect(540, 80, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_processImageGOF.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_processImageGOF.setFont(font)
        self.b_processImageGOF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_processImageGOF.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_processImageGOF.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"    text-decoration: underline;\n"
"}")
        self.b_processImageGOF.setObjectName("b_processImageGOF")
        self.layoutWidget = QtWidgets.QWidget(self.w_GameOfLife)
        self.layoutWidget.setGeometry(QtCore.QRect(37, 41, 461, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(6, 0, 6, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.colorButton_0_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_0.setMouseTracking(True)
        self.colorButton_0_0.setToolTipDuration(2500)
        self.colorButton_0_0.setAutoFillBackground(False)
        self.colorButton_0_0.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_0.setText("")
        self.colorButton_0_0.setCheckable(True)
        self.colorButton_0_0.setChecked(False)
        self.colorButton_0_0.setObjectName("colorButton_0_0")
        self.gridLayout.addWidget(self.colorButton_0_0, 0, 0, 1, 1)
        self.colorButton_0_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_1.setMouseTracking(True)
        self.colorButton_0_1.setToolTipDuration(2500)
        self.colorButton_0_1.setAutoFillBackground(False)
        self.colorButton_0_1.setStyleSheet("QPushButton {\n"
"    background-color: #364135;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_1.setText("")
        self.colorButton_0_1.setCheckable(True)
        self.colorButton_0_1.setChecked(False)
        self.colorButton_0_1.setObjectName("colorButton_0_1")
        self.gridLayout.addWidget(self.colorButton_0_1, 0, 1, 1, 1)
        self.colorButton_0_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_4.setMouseTracking(True)
        self.colorButton_0_4.setToolTipDuration(2500)
        self.colorButton_0_4.setAutoFillBackground(False)
        self.colorButton_0_4.setStyleSheet("QPushButton {\n"
"    background-color: #9B111E;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_4.setText("")
        self.colorButton_0_4.setCheckable(True)
        self.colorButton_0_4.setChecked(False)
        self.colorButton_0_4.setObjectName("colorButton_0_4")
        self.gridLayout.addWidget(self.colorButton_0_4, 0, 4, 1, 1)
        self.colorButton_0_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_5.setMouseTracking(True)
        self.colorButton_0_5.setToolTipDuration(2500)
        self.colorButton_0_5.setAutoFillBackground(False)
        self.colorButton_0_5.setStyleSheet("QPushButton {\n"
"    background-color: #FFA500;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_5.setText("")
        self.colorButton_0_5.setCheckable(True)
        self.colorButton_0_5.setChecked(False)
        self.colorButton_0_5.setObjectName("colorButton_0_5")
        self.gridLayout.addWidget(self.colorButton_0_5, 0, 5, 1, 1)
        self.colorButton_0_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_6.setMouseTracking(True)
        self.colorButton_0_6.setToolTipDuration(2500)
        self.colorButton_0_6.setAutoFillBackground(False)
        self.colorButton_0_6.setStyleSheet("QPushButton {\n"
"    background-color: #FFC0CB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_6.setText("")
        self.colorButton_0_6.setCheckable(True)
        self.colorButton_0_6.setChecked(False)
        self.colorButton_0_6.setObjectName("colorButton_0_6")
        self.gridLayout.addWidget(self.colorButton_0_6, 0, 6, 1, 1)
        self.colorButton_0_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_7.setMouseTracking(True)
        self.colorButton_0_7.setToolTipDuration(2500)
        self.colorButton_0_7.setAutoFillBackground(False)
        self.colorButton_0_7.setStyleSheet("QPushButton {\n"
"    background-color: #7FFFD4;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_7.setText("")
        self.colorButton_0_7.setCheckable(True)
        self.colorButton_0_7.setChecked(False)
        self.colorButton_0_7.setObjectName("colorButton_0_7")
        self.gridLayout.addWidget(self.colorButton_0_7, 0, 7, 1, 1)
        self.colorButton_0_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_8.setMouseTracking(True)
        self.colorButton_0_8.setToolTipDuration(2500)
        self.colorButton_0_8.setAutoFillBackground(False)
        self.colorButton_0_8.setStyleSheet("QPushButton {\n"
"    background-color: #90EE90;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_8.setText("")
        self.colorButton_0_8.setCheckable(True)
        self.colorButton_0_8.setChecked(False)
        self.colorButton_0_8.setObjectName("colorButton_0_8")
        self.gridLayout.addWidget(self.colorButton_0_8, 0, 8, 1, 1)
        self.colorButton_0_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_9.setMouseTracking(True)
        self.colorButton_0_9.setToolTipDuration(2500)
        self.colorButton_0_9.setAutoFillBackground(False)
        self.colorButton_0_9.setStyleSheet("QPushButton {\n"
"    background-color: #FFFDD0;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_9.setText("")
        self.colorButton_0_9.setCheckable(True)
        self.colorButton_0_9.setChecked(False)
        self.colorButton_0_9.setObjectName("colorButton_0_9")
        self.gridLayout.addWidget(self.colorButton_0_9, 0, 9, 1, 1)
        self.colorButton_1_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_0.setMouseTracking(True)
        self.colorButton_1_0.setToolTipDuration(2500)
        self.colorButton_1_0.setAutoFillBackground(False)
        self.colorButton_1_0.setStyleSheet("QPushButton {\n"
"    background-color: #2F2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_0.setText("")
        self.colorButton_1_0.setCheckable(True)
        self.colorButton_1_0.setChecked(False)
        self.colorButton_1_0.setObjectName("colorButton_1_0")
        self.gridLayout.addWidget(self.colorButton_1_0, 1, 0, 1, 1)
        self.colorButton_1_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_1.setMouseTracking(True)
        self.colorButton_1_1.setToolTipDuration(2500)
        self.colorButton_1_1.setAutoFillBackground(False)
        self.colorButton_1_1.setStyleSheet("QPushButton {\n"
"    background-color: #3B2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_1.setText("")
        self.colorButton_1_1.setCheckable(True)
        self.colorButton_1_1.setChecked(False)
        self.colorButton_1_1.setObjectName("colorButton_1_1")
        self.gridLayout.addWidget(self.colorButton_1_1, 1, 1, 1, 1)
        self.colorButton_1_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_2.setMouseTracking(True)
        self.colorButton_1_2.setToolTipDuration(2500)
        self.colorButton_1_2.setAutoFillBackground(False)
        self.colorButton_1_2.setStyleSheet("QPushButton {\n"
"    background-color: #008080;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_2.setText("")
        self.colorButton_1_2.setCheckable(True)
        self.colorButton_1_2.setChecked(False)
        self.colorButton_1_2.setObjectName("colorButton_1_2")
        self.gridLayout.addWidget(self.colorButton_1_2, 1, 2, 1, 1)
        self.colorButton_1_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_3.setMouseTracking(True)
        self.colorButton_1_3.setToolTipDuration(2500)
        self.colorButton_1_3.setAutoFillBackground(False)
        self.colorButton_1_3.setStyleSheet("QPushButton {\n"
"    background-color:#006D77;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_3.setText("")
        self.colorButton_1_3.setCheckable(True)
        self.colorButton_1_3.setChecked(False)
        self.colorButton_1_3.setObjectName("colorButton_1_3")
        self.gridLayout.addWidget(self.colorButton_1_3, 1, 3, 1, 1)
        self.colorButton_1_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_4.setMouseTracking(True)
        self.colorButton_1_4.setToolTipDuration(2500)
        self.colorButton_1_4.setAutoFillBackground(False)
        self.colorButton_1_4.setStyleSheet("QPushButton {\n"
"    background-color: #A52A2A;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_4.setText("")
        self.colorButton_1_4.setCheckable(True)
        self.colorButton_1_4.setChecked(False)
        self.colorButton_1_4.setObjectName("colorButton_1_4")
        self.gridLayout.addWidget(self.colorButton_1_4, 1, 4, 1, 1)
        self.colorButton_1_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_5.setMouseTracking(True)
        self.colorButton_1_5.setToolTipDuration(2500)
        self.colorButton_1_5.setAutoFillBackground(False)
        self.colorButton_1_5.setStyleSheet("QPushButton {\n"
"    background-color: #FF0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_5.setText("")
        self.colorButton_1_5.setCheckable(True)
        self.colorButton_1_5.setChecked(False)
        self.colorButton_1_5.setObjectName("colorButton_1_5")
        self.gridLayout.addWidget(self.colorButton_1_5, 1, 5, 1, 1)
        self.colorButton_1_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_6.setMouseTracking(True)
        self.colorButton_1_6.setToolTipDuration(2500)
        self.colorButton_1_6.setAutoFillBackground(False)
        self.colorButton_1_6.setStyleSheet("QPushButton {\n"
"    background-color: #DC143C;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_6.setText("")
        self.colorButton_1_6.setCheckable(True)
        self.colorButton_1_6.setChecked(False)
        self.colorButton_1_6.setObjectName("colorButton_1_6")
        self.gridLayout.addWidget(self.colorButton_1_6, 1, 6, 1, 1)
        self.colorButton_1_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_7.setMouseTracking(True)
        self.colorButton_1_7.setToolTipDuration(2500)
        self.colorButton_1_7.setAutoFillBackground(False)
        self.colorButton_1_7.setStyleSheet("QPushButton {\n"
"    background-color: #87CEFA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_7.setText("")
        self.colorButton_1_7.setCheckable(True)
        self.colorButton_1_7.setChecked(False)
        self.colorButton_1_7.setObjectName("colorButton_1_7")
        self.gridLayout.addWidget(self.colorButton_1_7, 1, 7, 1, 1)
        self.colorButton_1_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_8.setMouseTracking(True)
        self.colorButton_1_8.setToolTipDuration(2500)
        self.colorButton_1_8.setAutoFillBackground(False)
        self.colorButton_1_8.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFE0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_8.setText("")
        self.colorButton_1_8.setCheckable(True)
        self.colorButton_1_8.setChecked(False)
        self.colorButton_1_8.setObjectName("colorButton_1_8")
        self.gridLayout.addWidget(self.colorButton_1_8, 1, 8, 1, 1)
        self.colorButton_1_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_1_9.setMouseTracking(True)
        self.colorButton_1_9.setToolTipDuration(2500)
        self.colorButton_1_9.setAutoFillBackground(False)
        self.colorButton_1_9.setStyleSheet("QPushButton {\n"
"    background-color: #F5F5F5;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_9.setText("")
        self.colorButton_1_9.setCheckable(True)
        self.colorButton_1_9.setChecked(False)
        self.colorButton_1_9.setObjectName("colorButton_1_9")
        self.gridLayout.addWidget(self.colorButton_1_9, 1, 9, 1, 1)
        self.colorButton_2_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_0.setMouseTracking(True)
        self.colorButton_2_0.setToolTipDuration(2500)
        self.colorButton_2_0.setAutoFillBackground(False)
        self.colorButton_2_0.setStyleSheet("QPushButton {\n"
"    background-color: #36454F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_0.setText("")
        self.colorButton_2_0.setCheckable(True)
        self.colorButton_2_0.setChecked(False)
        self.colorButton_2_0.setObjectName("colorButton_2_0")
        self.gridLayout.addWidget(self.colorButton_2_0, 2, 0, 1, 1)
        self.colorButton_2_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_1.setMouseTracking(True)
        self.colorButton_2_1.setToolTipDuration(2500)
        self.colorButton_2_1.setAutoFillBackground(False)
        self.colorButton_2_1.setStyleSheet("QPushButton {\n"
"    background-color: #301934;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_1.setText("")
        self.colorButton_2_1.setCheckable(True)
        self.colorButton_2_1.setChecked(False)
        self.colorButton_2_1.setObjectName("colorButton_2_1")
        self.gridLayout.addWidget(self.colorButton_2_1, 2, 1, 1, 1)
        self.colorButton_2_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_2.setMouseTracking(True)
        self.colorButton_2_2.setToolTipDuration(2500)
        self.colorButton_2_2.setAutoFillBackground(False)
        self.colorButton_2_2.setStyleSheet("QPushButton {\n"
"    background-color: #485320;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_2.setText("")
        self.colorButton_2_2.setCheckable(True)
        self.colorButton_2_2.setChecked(False)
        self.colorButton_2_2.setObjectName("colorButton_2_2")
        self.gridLayout.addWidget(self.colorButton_2_2, 2, 2, 1, 1)
        self.colorButton_2_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_3.setMouseTracking(True)
        self.colorButton_2_3.setToolTipDuration(2500)
        self.colorButton_2_3.setAutoFillBackground(False)
        self.colorButton_2_3.setStyleSheet("QPushButton {\n"
"    background-color: #191970;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_3.setText("")
        self.colorButton_2_3.setCheckable(True)
        self.colorButton_2_3.setChecked(False)
        self.colorButton_2_3.setObjectName("colorButton_2_3")
        self.gridLayout.addWidget(self.colorButton_2_3, 2, 3, 1, 1)
        self.colorButton_2_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_4.setMouseTracking(True)
        self.colorButton_2_4.setToolTipDuration(2500)
        self.colorButton_2_4.setAutoFillBackground(False)
        self.colorButton_2_4.setStyleSheet("QPushButton {\n"
"    background-color: #C04000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_4.setText("")
        self.colorButton_2_4.setCheckable(True)
        self.colorButton_2_4.setChecked(False)
        self.colorButton_2_4.setObjectName("colorButton_2_4")
        self.gridLayout.addWidget(self.colorButton_2_4, 2, 4, 1, 1)
        self.colorButton_2_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_5.setMouseTracking(True)
        self.colorButton_2_5.setToolTipDuration(2500)
        self.colorButton_2_5.setAutoFillBackground(False)
        self.colorButton_2_5.setStyleSheet("QPushButton {\n"
"    background-color: #800080;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_5.setText("")
        self.colorButton_2_5.setCheckable(True)
        self.colorButton_2_5.setChecked(False)
        self.colorButton_2_5.setObjectName("colorButton_2_5")
        self.gridLayout.addWidget(self.colorButton_2_5, 2, 5, 1, 1)
        self.colorButton_2_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_6.setMouseTracking(True)
        self.colorButton_2_6.setToolTipDuration(2500)
        self.colorButton_2_6.setAutoFillBackground(False)
        self.colorButton_2_6.setStyleSheet("QPushButton {\n"
"    background-color: #00FF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_6.setText("")
        self.colorButton_2_6.setCheckable(True)
        self.colorButton_2_6.setChecked(False)
        self.colorButton_2_6.setObjectName("colorButton_2_6")
        self.gridLayout.addWidget(self.colorButton_2_6, 2, 6, 1, 1)
        self.colorButton_2_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_7.setMouseTracking(True)
        self.colorButton_2_7.setToolTipDuration(2500)
        self.colorButton_2_7.setAutoFillBackground(False)
        self.colorButton_2_7.setStyleSheet("QPushButton {\n"
"    background-color: #87CEEB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_7.setText("")
        self.colorButton_2_7.setCheckable(True)
        self.colorButton_2_7.setChecked(False)
        self.colorButton_2_7.setObjectName("colorButton_2_7")
        self.gridLayout.addWidget(self.colorButton_2_7, 2, 7, 1, 1)
        self.colorButton_2_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_8.setMouseTracking(True)
        self.colorButton_2_8.setToolTipDuration(2500)
        self.colorButton_2_8.setAutoFillBackground(False)
        self.colorButton_2_8.setStyleSheet("QPushButton {\n"
"    background-color: #FFFF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_8.setText("")
        self.colorButton_2_8.setCheckable(True)
        self.colorButton_2_8.setChecked(False)
        self.colorButton_2_8.setObjectName("colorButton_2_8")
        self.gridLayout.addWidget(self.colorButton_2_8, 2, 8, 1, 1)
        self.colorButton_2_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_2_9.setMouseTracking(True)
        self.colorButton_2_9.setToolTipDuration(2500)
        self.colorButton_2_9.setAutoFillBackground(False)
        self.colorButton_2_9.setStyleSheet("QPushButton {\n"
"    background-color: #D3D3D3;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_9.setText("")
        self.colorButton_2_9.setCheckable(True)
        self.colorButton_2_9.setChecked(False)
        self.colorButton_2_9.setObjectName("colorButton_2_9")
        self.gridLayout.addWidget(self.colorButton_2_9, 2, 9, 1, 1)
        self.colorButton_3_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_0.setMouseTracking(True)
        self.colorButton_3_0.setToolTipDuration(2500)
        self.colorButton_3_0.setAutoFillBackground(False)
        self.colorButton_3_0.setStyleSheet("QPushButton {\n"
"    background-color: #00008B;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_0.setText("")
        self.colorButton_3_0.setCheckable(True)
        self.colorButton_3_0.setChecked(False)
        self.colorButton_3_0.setObjectName("colorButton_3_0")
        self.gridLayout.addWidget(self.colorButton_3_0, 3, 0, 1, 1)
        self.colorButton_3_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_1.setMouseTracking(True)
        self.colorButton_3_1.setToolTipDuration(2500)
        self.colorButton_3_1.setAutoFillBackground(False)
        self.colorButton_3_1.setStyleSheet("QPushButton {\n"
"    background-color: #3B3C36;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_1.setText("")
        self.colorButton_3_1.setCheckable(True)
        self.colorButton_3_1.setChecked(False)
        self.colorButton_3_1.setObjectName("colorButton_3_1")
        self.gridLayout.addWidget(self.colorButton_3_1, 3, 1, 1, 1)
        self.colorButton_3_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_2.setMouseTracking(True)
        self.colorButton_3_2.setToolTipDuration(2500)
        self.colorButton_3_2.setAutoFillBackground(False)
        self.colorButton_3_2.setStyleSheet("QPushButton {\n"
"    background-color: #228B22;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_2.setText("")
        self.colorButton_3_2.setCheckable(True)
        self.colorButton_3_2.setChecked(False)
        self.colorButton_3_2.setObjectName("colorButton_3_2")
        self.gridLayout.addWidget(self.colorButton_3_2, 3, 2, 1, 1)
        self.colorButton_3_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_3.setMouseTracking(True)
        self.colorButton_3_3.setToolTipDuration(2500)
        self.colorButton_3_3.setAutoFillBackground(False)
        self.colorButton_3_3.setStyleSheet("QPushButton {\n"
"    background-color: #0F52BA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_3.setText("")
        self.colorButton_3_3.setCheckable(True)
        self.colorButton_3_3.setChecked(False)
        self.colorButton_3_3.setObjectName("colorButton_3_3")
        self.gridLayout.addWidget(self.colorButton_3_3, 3, 3, 1, 1)
        self.colorButton_3_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_4.setMouseTracking(True)
        self.colorButton_3_4.setToolTipDuration(2500)
        self.colorButton_3_4.setAutoFillBackground(False)
        self.colorButton_3_4.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_4.setText("")
        self.colorButton_3_4.setCheckable(True)
        self.colorButton_3_4.setChecked(False)
        self.colorButton_3_4.setObjectName("colorButton_3_4")
        self.gridLayout.addWidget(self.colorButton_3_4, 3, 4, 1, 1)
        self.colorButton_3_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_5.setMouseTracking(True)
        self.colorButton_3_5.setToolTipDuration(2500)
        self.colorButton_3_5.setAutoFillBackground(False)
        self.colorButton_3_5.setStyleSheet("QPushButton {\n"
"    background-color: #C71585;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_5.setText("")
        self.colorButton_3_5.setCheckable(True)
        self.colorButton_3_5.setChecked(False)
        self.colorButton_3_5.setObjectName("colorButton_3_5")
        self.gridLayout.addWidget(self.colorButton_3_5, 3, 5, 1, 1)
        self.colorButton_3_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_6.setMouseTracking(True)
        self.colorButton_3_6.setToolTipDuration(2500)
        self.colorButton_3_6.setAutoFillBackground(False)
        self.colorButton_3_6.setStyleSheet("QPushButton {\n"
"    background-color: #00FF7F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_6.setText("")
        self.colorButton_3_6.setCheckable(True)
        self.colorButton_3_6.setChecked(False)
        self.colorButton_3_6.setObjectName("colorButton_3_6")
        self.gridLayout.addWidget(self.colorButton_3_6, 3, 6, 1, 1)
        self.colorButton_3_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_7.setMouseTracking(True)
        self.colorButton_3_7.setToolTipDuration(2500)
        self.colorButton_3_7.setAutoFillBackground(False)
        self.colorButton_3_7.setStyleSheet("QPushButton {\n"
"    background-color: #0000FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_7.setText("")
        self.colorButton_3_7.setCheckable(True)
        self.colorButton_3_7.setChecked(False)
        self.colorButton_3_7.setObjectName("colorButton_3_7")
        self.gridLayout.addWidget(self.colorButton_3_7, 3, 7, 1, 1)
        self.colorButton_3_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_8.setMouseTracking(True)
        self.colorButton_3_8.setToolTipDuration(2500)
        self.colorButton_3_8.setAutoFillBackground(False)
        self.colorButton_3_8.setStyleSheet("QPushButton {\n"
"    background-color: #FFD700;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_8.setText("")
        self.colorButton_3_8.setCheckable(True)
        self.colorButton_3_8.setChecked(False)
        self.colorButton_3_8.setObjectName("colorButton_3_8")
        self.gridLayout.addWidget(self.colorButton_3_8, 3, 8, 1, 1)
        self.colorButton_3_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_3_9.setMouseTracking(True)
        self.colorButton_3_9.setToolTipDuration(2500)
        self.colorButton_3_9.setAutoFillBackground(False)
        self.colorButton_3_9.setStyleSheet("QPushButton {\n"
"    background-color: #C0C0C0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_9.setText("")
        self.colorButton_3_9.setCheckable(True)
        self.colorButton_3_9.setChecked(False)
        self.colorButton_3_9.setObjectName("colorButton_3_9")
        self.gridLayout.addWidget(self.colorButton_3_9, 3, 9, 1, 1)
        self.colorButton_4_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_0.setMouseTracking(True)
        self.colorButton_4_0.setToolTipDuration(2500)
        self.colorButton_4_0.setAutoFillBackground(False)
        self.colorButton_4_0.setStyleSheet("QPushButton {\n"
"    background-color:#013220;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_0.setText("")
        self.colorButton_4_0.setCheckable(True)
        self.colorButton_4_0.setChecked(False)
        self.colorButton_4_0.setObjectName("colorButton_4_0")
        self.gridLayout.addWidget(self.colorButton_4_0, 4, 0, 1, 1)
        self.colorButton_4_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_1.setMouseTracking(True)
        self.colorButton_4_1.setToolTipDuration(2500)
        self.colorButton_4_1.setAutoFillBackground(False)
        self.colorButton_4_1.setStyleSheet("QPushButton {\n"
"    background-color:#800000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_1.setText("")
        self.colorButton_4_1.setCheckable(True)
        self.colorButton_4_1.setChecked(False)
        self.colorButton_4_1.setObjectName("colorButton_4_1")
        self.gridLayout.addWidget(self.colorButton_4_1, 4, 1, 1, 1)
        self.colorButton_4_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_2.setMouseTracking(True)
        self.colorButton_4_2.setToolTipDuration(2500)
        self.colorButton_4_2.setAutoFillBackground(False)
        self.colorButton_4_2.setStyleSheet("QPushButton {\n"
"    background-color: #8B4513;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_2.setText("")
        self.colorButton_4_2.setCheckable(True)
        self.colorButton_4_2.setChecked(False)
        self.colorButton_4_2.setObjectName("colorButton_4_2")
        self.gridLayout.addWidget(self.colorButton_4_2, 4, 2, 1, 1)
        self.colorButton_4_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_3.setMouseTracking(True)
        self.colorButton_4_3.setToolTipDuration(2500)
        self.colorButton_4_3.setAutoFillBackground(False)
        self.colorButton_4_3.setStyleSheet("QPushButton {\n"
"    background-color: #8B0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_3.setText("")
        self.colorButton_4_3.setCheckable(True)
        self.colorButton_4_3.setChecked(False)
        self.colorButton_4_3.setObjectName("colorButton_4_3")
        self.gridLayout.addWidget(self.colorButton_4_3, 4, 3, 1, 1)
        self.colorButton_4_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_4.setMouseTracking(True)
        self.colorButton_4_4.setToolTipDuration(2500)
        self.colorButton_4_4.setAutoFillBackground(False)
        self.colorButton_4_4.setStyleSheet("QPushButton {\n"
"    background-color: #FF8C00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_4.setText("")
        self.colorButton_4_4.setCheckable(True)
        self.colorButton_4_4.setChecked(False)
        self.colorButton_4_4.setObjectName("colorButton_4_4")
        self.gridLayout.addWidget(self.colorButton_4_4, 4, 4, 1, 1)
        self.colorButton_4_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_5.setMouseTracking(True)
        self.colorButton_4_5.setToolTipDuration(2500)
        self.colorButton_4_5.setAutoFillBackground(False)
        self.colorButton_4_5.setStyleSheet("QPushButton {\n"
"    background-color: #FF00FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_5.setText("")
        self.colorButton_4_5.setCheckable(True)
        self.colorButton_4_5.setChecked(False)
        self.colorButton_4_5.setObjectName("colorButton_4_5")
        self.gridLayout.addWidget(self.colorButton_4_5, 4, 5, 1, 1)
        self.colorButton_4_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_6.setMouseTracking(True)
        self.colorButton_4_6.setToolTipDuration(2500)
        self.colorButton_4_6.setAutoFillBackground(False)
        self.colorButton_4_6.setStyleSheet("QPushButton {\n"
"    background-color: #40E0D0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_6.setText("")
        self.colorButton_4_6.setCheckable(True)
        self.colorButton_4_6.setChecked(False)
        self.colorButton_4_6.setObjectName("colorButton_4_6")
        self.gridLayout.addWidget(self.colorButton_4_6, 4, 6, 1, 1)
        self.colorButton_4_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_7.setMouseTracking(True)
        self.colorButton_4_7.setToolTipDuration(2500)
        self.colorButton_4_7.setAutoFillBackground(False)
        self.colorButton_4_7.setStyleSheet("QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_7.setText("")
        self.colorButton_4_7.setCheckable(True)
        self.colorButton_4_7.setChecked(False)
        self.colorButton_4_7.setObjectName("colorButton_4_7")
        self.gridLayout.addWidget(self.colorButton_4_7, 4, 7, 1, 1)
        self.colorButton_4_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_8.setMouseTracking(True)
        self.colorButton_4_8.setToolTipDuration(2500)
        self.colorButton_4_8.setAutoFillBackground(False)
        self.colorButton_4_8.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFF0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_8.setText("")
        self.colorButton_4_8.setCheckable(True)
        self.colorButton_4_8.setChecked(False)
        self.colorButton_4_8.setObjectName("colorButton_4_8")
        self.gridLayout.addWidget(self.colorButton_4_8, 4, 8, 1, 1)
        self.colorButton_4_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_4_9.setMouseTracking(True)
        self.colorButton_4_9.setToolTipDuration(2500)
        self.colorButton_4_9.setAutoFillBackground(False)
        self.colorButton_4_9.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_9.setText("")
        self.colorButton_4_9.setCheckable(True)
        self.colorButton_4_9.setChecked(False)
        self.colorButton_4_9.setObjectName("colorButton_4_9")
        self.gridLayout.addWidget(self.colorButton_4_9, 4, 9, 1, 1)
        self.colorButton_0_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_2.setMouseTracking(True)
        self.colorButton_0_2.setToolTipDuration(2500)
        self.colorButton_0_2.setAutoFillBackground(False)
        self.colorButton_0_2.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_2.setText("")
        self.colorButton_0_2.setCheckable(True)
        self.colorButton_0_2.setChecked(False)
        self.colorButton_0_2.setObjectName("colorButton_0_2")
        self.gridLayout.addWidget(self.colorButton_0_2, 0, 2, 1, 1)
        self.colorButton_0_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.colorButton_0_3.setMouseTracking(True)
        self.colorButton_0_3.setToolTipDuration(2500)
        self.colorButton_0_3.setAutoFillBackground(False)
        self.colorButton_0_3.setStyleSheet("QPushButton {\n"
"    background-color: #006A4E;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_3.setText("")
        self.colorButton_0_3.setCheckable(True)
        self.colorButton_0_3.setChecked(False)
        self.colorButton_0_3.setObjectName("colorButton_0_3")
        self.gridLayout.addWidget(self.colorButton_0_3, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.w_GameOfLife)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(90, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.GameOfLife)
        self.label.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.GameOfLife)
        self.NoisePerlin = QtWidgets.QWidget()
        self.NoisePerlin.setObjectName("NoisePerlin")
        self.b_deleteOrigImage1 = QtWidgets.QPushButton(self.NoisePerlin)
        self.b_deleteOrigImage1.setGeometry(QtCore.QRect(740, 10, 31, 28))
        self.b_deleteOrigImage1.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteOrigImage1.setObjectName("b_deleteOrigImage1")
        self.b_AddOrigImage1 = QtWidgets.QPushButton(self.NoisePerlin)
        self.b_AddOrigImage1.setGeometry(QtCore.QRect(690, 10, 31, 28))
        self.b_AddOrigImage1.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_AddOrigImage1.setObjectName("b_AddOrigImage1")
        self.l_ProcImage_pg1 = QtWidgets.QLabel(self.NoisePerlin)
        self.l_ProcImage_pg1.setGeometry(QtCore.QRect(810, 40, 741, 551))
        self.l_ProcImage_pg1.setStyleSheet("background:white;")
        self.l_ProcImage_pg1.setText("")
        self.l_ProcImage_pg1.setObjectName("l_ProcImage_pg1")
        self.b_deleteProcImage1 = QtWidgets.QPushButton(self.NoisePerlin)
        self.b_deleteProcImage1.setGeometry(QtCore.QRect(1520, 10, 31, 28))
        self.b_deleteProcImage1.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteProcImage1.setObjectName("b_deleteProcImage1")
        self.l_OrigImage_pg1 = QtWidgets.QLabel(self.NoisePerlin)
        self.l_OrigImage_pg1.setGeometry(QtCore.QRect(30, 40, 741, 551))
        self.l_OrigImage_pg1.setStyleSheet("background:white;")
        self.l_OrigImage_pg1.setText("")
        self.l_OrigImage_pg1.setObjectName("l_OrigImage_pg1")
        self.b_SaveProcImage1 = QtWidgets.QPushButton(self.NoisePerlin)
        self.b_SaveProcImage1.setGeometry(QtCore.QRect(1470, 10, 31, 28))
        self.b_SaveProcImage1.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_SaveProcImage1.setObjectName("b_SaveProcImage1")
        self.w_NoisePerlin = QtWidgets.QWidget(self.NoisePerlin)
        self.w_NoisePerlin.setGeometry(QtCore.QRect(30, 610, 741, 241))
        self.w_NoisePerlin.setStyleSheet("border: 2px solid rgba(235, 225, 225, 0.9);")
        self.w_NoisePerlin.setObjectName("w_NoisePerlin")
        self.b_processImageNP = QtWidgets.QPushButton(self.w_NoisePerlin)
        self.b_processImageNP.setGeometry(QtCore.QRect(540, 80, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_processImageNP.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_processImageNP.setFont(font)
        self.b_processImageNP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_processImageNP.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_processImageNP.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"    text-decoration: underline;\n"
"}")
        self.b_processImageNP.setObjectName("b_processImageNP")
        self.layoutWidget_3 = QtWidgets.QWidget(self.w_NoisePerlin)
        self.layoutWidget_3.setGeometry(QtCore.QRect(37, 41, 461, 161))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(6, 0, 6, 0)
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.colorButton_0_40 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_40.setMouseTracking(True)
        self.colorButton_0_40.setToolTipDuration(2500)
        self.colorButton_0_40.setAutoFillBackground(False)
        self.colorButton_0_40.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_40.setText("")
        self.colorButton_0_40.setCheckable(True)
        self.colorButton_0_40.setChecked(False)
        self.colorButton_0_40.setObjectName("colorButton_0_40")
        self.gridLayout_3.addWidget(self.colorButton_0_40, 0, 0, 1, 1)
        self.colorButton_0_41 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_41.setMouseTracking(True)
        self.colorButton_0_41.setToolTipDuration(2500)
        self.colorButton_0_41.setAutoFillBackground(False)
        self.colorButton_0_41.setStyleSheet("QPushButton {\n"
"    background-color: #364135;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_41.setText("")
        self.colorButton_0_41.setCheckable(True)
        self.colorButton_0_41.setChecked(False)
        self.colorButton_0_41.setObjectName("colorButton_0_41")
        self.gridLayout_3.addWidget(self.colorButton_0_41, 0, 1, 1, 1)
        self.colorButton_0_42 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_42.setMouseTracking(True)
        self.colorButton_0_42.setToolTipDuration(2500)
        self.colorButton_0_42.setAutoFillBackground(False)
        self.colorButton_0_42.setStyleSheet("QPushButton {\n"
"    background-color: #9B111E;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_42.setText("")
        self.colorButton_0_42.setCheckable(True)
        self.colorButton_0_42.setChecked(False)
        self.colorButton_0_42.setObjectName("colorButton_0_42")
        self.gridLayout_3.addWidget(self.colorButton_0_42, 0, 4, 1, 1)
        self.colorButton_0_43 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_43.setMouseTracking(True)
        self.colorButton_0_43.setToolTipDuration(2500)
        self.colorButton_0_43.setAutoFillBackground(False)
        self.colorButton_0_43.setStyleSheet("QPushButton {\n"
"    background-color: #FFA500;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_43.setText("")
        self.colorButton_0_43.setCheckable(True)
        self.colorButton_0_43.setChecked(False)
        self.colorButton_0_43.setObjectName("colorButton_0_43")
        self.gridLayout_3.addWidget(self.colorButton_0_43, 0, 5, 1, 1)
        self.colorButton_0_44 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_44.setMouseTracking(True)
        self.colorButton_0_44.setToolTipDuration(2500)
        self.colorButton_0_44.setAutoFillBackground(False)
        self.colorButton_0_44.setStyleSheet("QPushButton {\n"
"    background-color: #FFC0CB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_44.setText("")
        self.colorButton_0_44.setCheckable(True)
        self.colorButton_0_44.setChecked(False)
        self.colorButton_0_44.setObjectName("colorButton_0_44")
        self.gridLayout_3.addWidget(self.colorButton_0_44, 0, 6, 1, 1)
        self.colorButton_0_45 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_45.setMouseTracking(True)
        self.colorButton_0_45.setToolTipDuration(2500)
        self.colorButton_0_45.setAutoFillBackground(False)
        self.colorButton_0_45.setStyleSheet("QPushButton {\n"
"    background-color: #7FFFD4;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_45.setText("")
        self.colorButton_0_45.setCheckable(True)
        self.colorButton_0_45.setChecked(False)
        self.colorButton_0_45.setObjectName("colorButton_0_45")
        self.gridLayout_3.addWidget(self.colorButton_0_45, 0, 7, 1, 1)
        self.colorButton_0_46 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_46.setMouseTracking(True)
        self.colorButton_0_46.setToolTipDuration(2500)
        self.colorButton_0_46.setAutoFillBackground(False)
        self.colorButton_0_46.setStyleSheet("QPushButton {\n"
"    background-color: #90EE90;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_46.setText("")
        self.colorButton_0_46.setCheckable(True)
        self.colorButton_0_46.setChecked(False)
        self.colorButton_0_46.setObjectName("colorButton_0_46")
        self.gridLayout_3.addWidget(self.colorButton_0_46, 0, 8, 1, 1)
        self.colorButton_0_47 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_47.setMouseTracking(True)
        self.colorButton_0_47.setToolTipDuration(2500)
        self.colorButton_0_47.setAutoFillBackground(False)
        self.colorButton_0_47.setStyleSheet("QPushButton {\n"
"    background-color: #FFFDD0;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_47.setText("")
        self.colorButton_0_47.setCheckable(True)
        self.colorButton_0_47.setChecked(False)
        self.colorButton_0_47.setObjectName("colorButton_0_47")
        self.gridLayout_3.addWidget(self.colorButton_0_47, 0, 9, 1, 1)
        self.colorButton_1_40 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_40.setMouseTracking(True)
        self.colorButton_1_40.setToolTipDuration(2500)
        self.colorButton_1_40.setAutoFillBackground(False)
        self.colorButton_1_40.setStyleSheet("QPushButton {\n"
"    background-color: #2F2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_40.setText("")
        self.colorButton_1_40.setCheckable(True)
        self.colorButton_1_40.setChecked(False)
        self.colorButton_1_40.setObjectName("colorButton_1_40")
        self.gridLayout_3.addWidget(self.colorButton_1_40, 1, 0, 1, 1)
        self.colorButton_1_41 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_41.setMouseTracking(True)
        self.colorButton_1_41.setToolTipDuration(2500)
        self.colorButton_1_41.setAutoFillBackground(False)
        self.colorButton_1_41.setStyleSheet("QPushButton {\n"
"    background-color: #3B2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_41.setText("")
        self.colorButton_1_41.setCheckable(True)
        self.colorButton_1_41.setChecked(False)
        self.colorButton_1_41.setObjectName("colorButton_1_41")
        self.gridLayout_3.addWidget(self.colorButton_1_41, 1, 1, 1, 1)
        self.colorButton_1_42 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_42.setMouseTracking(True)
        self.colorButton_1_42.setToolTipDuration(2500)
        self.colorButton_1_42.setAutoFillBackground(False)
        self.colorButton_1_42.setStyleSheet("QPushButton {\n"
"    background-color: #008080;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_42.setText("")
        self.colorButton_1_42.setCheckable(True)
        self.colorButton_1_42.setChecked(False)
        self.colorButton_1_42.setObjectName("colorButton_1_42")
        self.gridLayout_3.addWidget(self.colorButton_1_42, 1, 2, 1, 1)
        self.colorButton_1_43 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_43.setMouseTracking(True)
        self.colorButton_1_43.setToolTipDuration(2500)
        self.colorButton_1_43.setAutoFillBackground(False)
        self.colorButton_1_43.setStyleSheet("QPushButton {\n"
"    background-color:#006D77;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_43.setText("")
        self.colorButton_1_43.setCheckable(True)
        self.colorButton_1_43.setChecked(False)
        self.colorButton_1_43.setObjectName("colorButton_1_43")
        self.gridLayout_3.addWidget(self.colorButton_1_43, 1, 3, 1, 1)
        self.colorButton_1_44 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_44.setMouseTracking(True)
        self.colorButton_1_44.setToolTipDuration(2500)
        self.colorButton_1_44.setAutoFillBackground(False)
        self.colorButton_1_44.setStyleSheet("QPushButton {\n"
"    background-color: #A52A2A;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_44.setText("")
        self.colorButton_1_44.setCheckable(True)
        self.colorButton_1_44.setChecked(False)
        self.colorButton_1_44.setObjectName("colorButton_1_44")
        self.gridLayout_3.addWidget(self.colorButton_1_44, 1, 4, 1, 1)
        self.colorButton_1_45 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_45.setMouseTracking(True)
        self.colorButton_1_45.setToolTipDuration(2500)
        self.colorButton_1_45.setAutoFillBackground(False)
        self.colorButton_1_45.setStyleSheet("QPushButton {\n"
"    background-color: #FF0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_45.setText("")
        self.colorButton_1_45.setCheckable(True)
        self.colorButton_1_45.setChecked(False)
        self.colorButton_1_45.setObjectName("colorButton_1_45")
        self.gridLayout_3.addWidget(self.colorButton_1_45, 1, 5, 1, 1)
        self.colorButton_1_46 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_46.setMouseTracking(True)
        self.colorButton_1_46.setToolTipDuration(2500)
        self.colorButton_1_46.setAutoFillBackground(False)
        self.colorButton_1_46.setStyleSheet("QPushButton {\n"
"    background-color: #DC143C;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_46.setText("")
        self.colorButton_1_46.setCheckable(True)
        self.colorButton_1_46.setChecked(False)
        self.colorButton_1_46.setObjectName("colorButton_1_46")
        self.gridLayout_3.addWidget(self.colorButton_1_46, 1, 6, 1, 1)
        self.colorButton_1_47 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_47.setMouseTracking(True)
        self.colorButton_1_47.setToolTipDuration(2500)
        self.colorButton_1_47.setAutoFillBackground(False)
        self.colorButton_1_47.setStyleSheet("QPushButton {\n"
"    background-color: #87CEFA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_47.setText("")
        self.colorButton_1_47.setCheckable(True)
        self.colorButton_1_47.setChecked(False)
        self.colorButton_1_47.setObjectName("colorButton_1_47")
        self.gridLayout_3.addWidget(self.colorButton_1_47, 1, 7, 1, 1)
        self.colorButton_1_48 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_48.setMouseTracking(True)
        self.colorButton_1_48.setToolTipDuration(2500)
        self.colorButton_1_48.setAutoFillBackground(False)
        self.colorButton_1_48.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFE0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_48.setText("")
        self.colorButton_1_48.setCheckable(True)
        self.colorButton_1_48.setChecked(False)
        self.colorButton_1_48.setObjectName("colorButton_1_48")
        self.gridLayout_3.addWidget(self.colorButton_1_48, 1, 8, 1, 1)
        self.colorButton_1_49 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_1_49.setMouseTracking(True)
        self.colorButton_1_49.setToolTipDuration(2500)
        self.colorButton_1_49.setAutoFillBackground(False)
        self.colorButton_1_49.setStyleSheet("QPushButton {\n"
"    background-color: #F5F5F5;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_49.setText("")
        self.colorButton_1_49.setCheckable(True)
        self.colorButton_1_49.setChecked(False)
        self.colorButton_1_49.setObjectName("colorButton_1_49")
        self.gridLayout_3.addWidget(self.colorButton_1_49, 1, 9, 1, 1)
        self.colorButton_2_40 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_40.setMouseTracking(True)
        self.colorButton_2_40.setToolTipDuration(2500)
        self.colorButton_2_40.setAutoFillBackground(False)
        self.colorButton_2_40.setStyleSheet("QPushButton {\n"
"    background-color: #36454F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_40.setText("")
        self.colorButton_2_40.setCheckable(True)
        self.colorButton_2_40.setChecked(False)
        self.colorButton_2_40.setObjectName("colorButton_2_40")
        self.gridLayout_3.addWidget(self.colorButton_2_40, 2, 0, 1, 1)
        self.colorButton_2_41 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_41.setMouseTracking(True)
        self.colorButton_2_41.setToolTipDuration(2500)
        self.colorButton_2_41.setAutoFillBackground(False)
        self.colorButton_2_41.setStyleSheet("QPushButton {\n"
"    background-color: #301934;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_41.setText("")
        self.colorButton_2_41.setCheckable(True)
        self.colorButton_2_41.setChecked(False)
        self.colorButton_2_41.setObjectName("colorButton_2_41")
        self.gridLayout_3.addWidget(self.colorButton_2_41, 2, 1, 1, 1)
        self.colorButton_2_42 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_42.setMouseTracking(True)
        self.colorButton_2_42.setToolTipDuration(2500)
        self.colorButton_2_42.setAutoFillBackground(False)
        self.colorButton_2_42.setStyleSheet("QPushButton {\n"
"    background-color: #485320;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_42.setText("")
        self.colorButton_2_42.setCheckable(True)
        self.colorButton_2_42.setChecked(False)
        self.colorButton_2_42.setObjectName("colorButton_2_42")
        self.gridLayout_3.addWidget(self.colorButton_2_42, 2, 2, 1, 1)
        self.colorButton_2_43 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_43.setMouseTracking(True)
        self.colorButton_2_43.setToolTipDuration(2500)
        self.colorButton_2_43.setAutoFillBackground(False)
        self.colorButton_2_43.setStyleSheet("QPushButton {\n"
"    background-color: #191970;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_43.setText("")
        self.colorButton_2_43.setCheckable(True)
        self.colorButton_2_43.setChecked(False)
        self.colorButton_2_43.setObjectName("colorButton_2_43")
        self.gridLayout_3.addWidget(self.colorButton_2_43, 2, 3, 1, 1)
        self.colorButton_2_44 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_44.setMouseTracking(True)
        self.colorButton_2_44.setToolTipDuration(2500)
        self.colorButton_2_44.setAutoFillBackground(False)
        self.colorButton_2_44.setStyleSheet("QPushButton {\n"
"    background-color: #C04000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_44.setText("")
        self.colorButton_2_44.setCheckable(True)
        self.colorButton_2_44.setChecked(False)
        self.colorButton_2_44.setObjectName("colorButton_2_44")
        self.gridLayout_3.addWidget(self.colorButton_2_44, 2, 4, 1, 1)
        self.colorButton_2_45 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_45.setMouseTracking(True)
        self.colorButton_2_45.setToolTipDuration(2500)
        self.colorButton_2_45.setAutoFillBackground(False)
        self.colorButton_2_45.setStyleSheet("QPushButton {\n"
"    background-color: #800080;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_45.setText("")
        self.colorButton_2_45.setCheckable(True)
        self.colorButton_2_45.setChecked(False)
        self.colorButton_2_45.setObjectName("colorButton_2_45")
        self.gridLayout_3.addWidget(self.colorButton_2_45, 2, 5, 1, 1)
        self.colorButton_2_46 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_46.setMouseTracking(True)
        self.colorButton_2_46.setToolTipDuration(2500)
        self.colorButton_2_46.setAutoFillBackground(False)
        self.colorButton_2_46.setStyleSheet("QPushButton {\n"
"    background-color: #00FF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_46.setText("")
        self.colorButton_2_46.setCheckable(True)
        self.colorButton_2_46.setChecked(False)
        self.colorButton_2_46.setObjectName("colorButton_2_46")
        self.gridLayout_3.addWidget(self.colorButton_2_46, 2, 6, 1, 1)
        self.colorButton_2_47 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_47.setMouseTracking(True)
        self.colorButton_2_47.setToolTipDuration(2500)
        self.colorButton_2_47.setAutoFillBackground(False)
        self.colorButton_2_47.setStyleSheet("QPushButton {\n"
"    background-color: #87CEEB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_47.setText("")
        self.colorButton_2_47.setCheckable(True)
        self.colorButton_2_47.setChecked(False)
        self.colorButton_2_47.setObjectName("colorButton_2_47")
        self.gridLayout_3.addWidget(self.colorButton_2_47, 2, 7, 1, 1)
        self.colorButton_2_48 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_48.setMouseTracking(True)
        self.colorButton_2_48.setToolTipDuration(2500)
        self.colorButton_2_48.setAutoFillBackground(False)
        self.colorButton_2_48.setStyleSheet("QPushButton {\n"
"    background-color: #FFFF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_48.setText("")
        self.colorButton_2_48.setCheckable(True)
        self.colorButton_2_48.setChecked(False)
        self.colorButton_2_48.setObjectName("colorButton_2_48")
        self.gridLayout_3.addWidget(self.colorButton_2_48, 2, 8, 1, 1)
        self.colorButton_2_49 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_2_49.setMouseTracking(True)
        self.colorButton_2_49.setToolTipDuration(2500)
        self.colorButton_2_49.setAutoFillBackground(False)
        self.colorButton_2_49.setStyleSheet("QPushButton {\n"
"    background-color: #D3D3D3;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_49.setText("")
        self.colorButton_2_49.setCheckable(True)
        self.colorButton_2_49.setChecked(False)
        self.colorButton_2_49.setObjectName("colorButton_2_49")
        self.gridLayout_3.addWidget(self.colorButton_2_49, 2, 9, 1, 1)
        self.colorButton_3_40 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_40.setMouseTracking(True)
        self.colorButton_3_40.setToolTipDuration(2500)
        self.colorButton_3_40.setAutoFillBackground(False)
        self.colorButton_3_40.setStyleSheet("QPushButton {\n"
"    background-color: #00008B;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_40.setText("")
        self.colorButton_3_40.setCheckable(True)
        self.colorButton_3_40.setChecked(False)
        self.colorButton_3_40.setObjectName("colorButton_3_40")
        self.gridLayout_3.addWidget(self.colorButton_3_40, 3, 0, 1, 1)
        self.colorButton_3_41 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_41.setMouseTracking(True)
        self.colorButton_3_41.setToolTipDuration(2500)
        self.colorButton_3_41.setAutoFillBackground(False)
        self.colorButton_3_41.setStyleSheet("QPushButton {\n"
"    background-color: #3B3C36;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_41.setText("")
        self.colorButton_3_41.setCheckable(True)
        self.colorButton_3_41.setChecked(False)
        self.colorButton_3_41.setObjectName("colorButton_3_41")
        self.gridLayout_3.addWidget(self.colorButton_3_41, 3, 1, 1, 1)
        self.colorButton_3_42 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_42.setMouseTracking(True)
        self.colorButton_3_42.setToolTipDuration(2500)
        self.colorButton_3_42.setAutoFillBackground(False)
        self.colorButton_3_42.setStyleSheet("QPushButton {\n"
"    background-color: #228B22;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_42.setText("")
        self.colorButton_3_42.setCheckable(True)
        self.colorButton_3_42.setChecked(False)
        self.colorButton_3_42.setObjectName("colorButton_3_42")
        self.gridLayout_3.addWidget(self.colorButton_3_42, 3, 2, 1, 1)
        self.colorButton_3_43 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_43.setMouseTracking(True)
        self.colorButton_3_43.setToolTipDuration(2500)
        self.colorButton_3_43.setAutoFillBackground(False)
        self.colorButton_3_43.setStyleSheet("QPushButton {\n"
"    background-color: #0F52BA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_43.setText("")
        self.colorButton_3_43.setCheckable(True)
        self.colorButton_3_43.setChecked(False)
        self.colorButton_3_43.setObjectName("colorButton_3_43")
        self.gridLayout_3.addWidget(self.colorButton_3_43, 3, 3, 1, 1)
        self.colorButton_3_44 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_44.setMouseTracking(True)
        self.colorButton_3_44.setToolTipDuration(2500)
        self.colorButton_3_44.setAutoFillBackground(False)
        self.colorButton_3_44.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_44.setText("")
        self.colorButton_3_44.setCheckable(True)
        self.colorButton_3_44.setChecked(False)
        self.colorButton_3_44.setObjectName("colorButton_3_44")
        self.gridLayout_3.addWidget(self.colorButton_3_44, 3, 4, 1, 1)
        self.colorButton_3_45 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_45.setMouseTracking(True)
        self.colorButton_3_45.setToolTipDuration(2500)
        self.colorButton_3_45.setAutoFillBackground(False)
        self.colorButton_3_45.setStyleSheet("QPushButton {\n"
"    background-color: #C71585;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_45.setText("")
        self.colorButton_3_45.setCheckable(True)
        self.colorButton_3_45.setChecked(False)
        self.colorButton_3_45.setObjectName("colorButton_3_45")
        self.gridLayout_3.addWidget(self.colorButton_3_45, 3, 5, 1, 1)
        self.colorButton_3_46 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_46.setMouseTracking(True)
        self.colorButton_3_46.setToolTipDuration(2500)
        self.colorButton_3_46.setAutoFillBackground(False)
        self.colorButton_3_46.setStyleSheet("QPushButton {\n"
"    background-color: #00FF7F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_46.setText("")
        self.colorButton_3_46.setCheckable(True)
        self.colorButton_3_46.setChecked(False)
        self.colorButton_3_46.setObjectName("colorButton_3_46")
        self.gridLayout_3.addWidget(self.colorButton_3_46, 3, 6, 1, 1)
        self.colorButton_3_47 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_47.setMouseTracking(True)
        self.colorButton_3_47.setToolTipDuration(2500)
        self.colorButton_3_47.setAutoFillBackground(False)
        self.colorButton_3_47.setStyleSheet("QPushButton {\n"
"    background-color: #0000FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_47.setText("")
        self.colorButton_3_47.setCheckable(True)
        self.colorButton_3_47.setChecked(False)
        self.colorButton_3_47.setObjectName("colorButton_3_47")
        self.gridLayout_3.addWidget(self.colorButton_3_47, 3, 7, 1, 1)
        self.colorButton_3_48 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_48.setMouseTracking(True)
        self.colorButton_3_48.setToolTipDuration(2500)
        self.colorButton_3_48.setAutoFillBackground(False)
        self.colorButton_3_48.setStyleSheet("QPushButton {\n"
"    background-color: #FFD700;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_48.setText("")
        self.colorButton_3_48.setCheckable(True)
        self.colorButton_3_48.setChecked(False)
        self.colorButton_3_48.setObjectName("colorButton_3_48")
        self.gridLayout_3.addWidget(self.colorButton_3_48, 3, 8, 1, 1)
        self.colorButton_3_49 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_3_49.setMouseTracking(True)
        self.colorButton_3_49.setToolTipDuration(2500)
        self.colorButton_3_49.setAutoFillBackground(False)
        self.colorButton_3_49.setStyleSheet("QPushButton {\n"
"    background-color: #C0C0C0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_49.setText("")
        self.colorButton_3_49.setCheckable(True)
        self.colorButton_3_49.setChecked(False)
        self.colorButton_3_49.setObjectName("colorButton_3_49")
        self.gridLayout_3.addWidget(self.colorButton_3_49, 3, 9, 1, 1)
        self.colorButton_4_40 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_40.setMouseTracking(True)
        self.colorButton_4_40.setToolTipDuration(2500)
        self.colorButton_4_40.setAutoFillBackground(False)
        self.colorButton_4_40.setStyleSheet("QPushButton {\n"
"    background-color:#013220;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_40.setText("")
        self.colorButton_4_40.setCheckable(True)
        self.colorButton_4_40.setChecked(False)
        self.colorButton_4_40.setObjectName("colorButton_4_40")
        self.gridLayout_3.addWidget(self.colorButton_4_40, 4, 0, 1, 1)
        self.colorButton_4_41 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_41.setMouseTracking(True)
        self.colorButton_4_41.setToolTipDuration(2500)
        self.colorButton_4_41.setAutoFillBackground(False)
        self.colorButton_4_41.setStyleSheet("QPushButton {\n"
"    background-color:#800000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_41.setText("")
        self.colorButton_4_41.setCheckable(True)
        self.colorButton_4_41.setChecked(False)
        self.colorButton_4_41.setObjectName("colorButton_4_41")
        self.gridLayout_3.addWidget(self.colorButton_4_41, 4, 1, 1, 1)
        self.colorButton_4_42 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_42.setMouseTracking(True)
        self.colorButton_4_42.setToolTipDuration(2500)
        self.colorButton_4_42.setAutoFillBackground(False)
        self.colorButton_4_42.setStyleSheet("QPushButton {\n"
"    background-color: #8B4513;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_42.setText("")
        self.colorButton_4_42.setCheckable(True)
        self.colorButton_4_42.setChecked(False)
        self.colorButton_4_42.setObjectName("colorButton_4_42")
        self.gridLayout_3.addWidget(self.colorButton_4_42, 4, 2, 1, 1)
        self.colorButton_4_43 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_43.setMouseTracking(True)
        self.colorButton_4_43.setToolTipDuration(2500)
        self.colorButton_4_43.setAutoFillBackground(False)
        self.colorButton_4_43.setStyleSheet("QPushButton {\n"
"    background-color: #8B0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_43.setText("")
        self.colorButton_4_43.setCheckable(True)
        self.colorButton_4_43.setChecked(False)
        self.colorButton_4_43.setObjectName("colorButton_4_43")
        self.gridLayout_3.addWidget(self.colorButton_4_43, 4, 3, 1, 1)
        self.colorButton_4_44 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_44.setMouseTracking(True)
        self.colorButton_4_44.setToolTipDuration(2500)
        self.colorButton_4_44.setAutoFillBackground(False)
        self.colorButton_4_44.setStyleSheet("QPushButton {\n"
"    background-color: #FF8C00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_44.setText("")
        self.colorButton_4_44.setCheckable(True)
        self.colorButton_4_44.setChecked(False)
        self.colorButton_4_44.setObjectName("colorButton_4_44")
        self.gridLayout_3.addWidget(self.colorButton_4_44, 4, 4, 1, 1)
        self.colorButton_4_45 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_45.setMouseTracking(True)
        self.colorButton_4_45.setToolTipDuration(2500)
        self.colorButton_4_45.setAutoFillBackground(False)
        self.colorButton_4_45.setStyleSheet("QPushButton {\n"
"    background-color: #FF00FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_45.setText("")
        self.colorButton_4_45.setCheckable(True)
        self.colorButton_4_45.setChecked(False)
        self.colorButton_4_45.setObjectName("colorButton_4_45")
        self.gridLayout_3.addWidget(self.colorButton_4_45, 4, 5, 1, 1)
        self.colorButton_4_46 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_46.setMouseTracking(True)
        self.colorButton_4_46.setToolTipDuration(2500)
        self.colorButton_4_46.setAutoFillBackground(False)
        self.colorButton_4_46.setStyleSheet("QPushButton {\n"
"    background-color: #40E0D0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_46.setText("")
        self.colorButton_4_46.setCheckable(True)
        self.colorButton_4_46.setChecked(False)
        self.colorButton_4_46.setObjectName("colorButton_4_46")
        self.gridLayout_3.addWidget(self.colorButton_4_46, 4, 6, 1, 1)
        self.colorButton_4_47 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_47.setMouseTracking(True)
        self.colorButton_4_47.setToolTipDuration(2500)
        self.colorButton_4_47.setAutoFillBackground(False)
        self.colorButton_4_47.setStyleSheet("QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_47.setText("")
        self.colorButton_4_47.setCheckable(True)
        self.colorButton_4_47.setChecked(False)
        self.colorButton_4_47.setObjectName("colorButton_4_47")
        self.gridLayout_3.addWidget(self.colorButton_4_47, 4, 7, 1, 1)
        self.colorButton_4_48 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_48.setMouseTracking(True)
        self.colorButton_4_48.setToolTipDuration(2500)
        self.colorButton_4_48.setAutoFillBackground(False)
        self.colorButton_4_48.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFF0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_48.setText("")
        self.colorButton_4_48.setCheckable(True)
        self.colorButton_4_48.setChecked(False)
        self.colorButton_4_48.setObjectName("colorButton_4_48")
        self.gridLayout_3.addWidget(self.colorButton_4_48, 4, 8, 1, 1)
        self.colorButton_4_49 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_4_49.setMouseTracking(True)
        self.colorButton_4_49.setToolTipDuration(2500)
        self.colorButton_4_49.setAutoFillBackground(False)
        self.colorButton_4_49.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_49.setText("")
        self.colorButton_4_49.setCheckable(True)
        self.colorButton_4_49.setChecked(False)
        self.colorButton_4_49.setObjectName("colorButton_4_49")
        self.gridLayout_3.addWidget(self.colorButton_4_49, 4, 9, 1, 1)
        self.colorButton_0_48 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_48.setMouseTracking(True)
        self.colorButton_0_48.setToolTipDuration(2500)
        self.colorButton_0_48.setAutoFillBackground(False)
        self.colorButton_0_48.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_48.setText("")
        self.colorButton_0_48.setCheckable(True)
        self.colorButton_0_48.setChecked(False)
        self.colorButton_0_48.setObjectName("colorButton_0_48")
        self.gridLayout_3.addWidget(self.colorButton_0_48, 0, 2, 1, 1)
        self.colorButton_0_49 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.colorButton_0_49.setMouseTracking(True)
        self.colorButton_0_49.setToolTipDuration(2500)
        self.colorButton_0_49.setAutoFillBackground(False)
        self.colorButton_0_49.setStyleSheet("QPushButton {\n"
"    background-color: #006A4E;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_49.setText("")
        self.colorButton_0_49.setCheckable(True)
        self.colorButton_0_49.setChecked(False)
        self.colorButton_0_49.setObjectName("colorButton_0_49")
        self.gridLayout_3.addWidget(self.colorButton_0_49, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.w_NoisePerlin)
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QtCore.QRect(90, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_2 = QtWidgets.QLabel(self.NoisePerlin)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.NoisePerlin)
        self.KrivaKoxa = QtWidgets.QWidget()
        self.KrivaKoxa.setObjectName("KrivaKoxa")
        self.b_deleteProcImage2 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.b_deleteProcImage2.setGeometry(QtCore.QRect(1520, 10, 31, 28))
        self.b_deleteProcImage2.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteProcImage2.setObjectName("b_deleteProcImage2")
        self.l_OrigImage_pg2 = QtWidgets.QLabel(self.KrivaKoxa)
        self.l_OrigImage_pg2.setGeometry(QtCore.QRect(30, 40, 741, 551))
        self.l_OrigImage_pg2.setStyleSheet("background:white;")
        self.l_OrigImage_pg2.setText("")
        self.l_OrigImage_pg2.setObjectName("l_OrigImage_pg2")
        self.l_ProcImage_pg2 = QtWidgets.QLabel(self.KrivaKoxa)
        self.l_ProcImage_pg2.setGeometry(QtCore.QRect(810, 40, 741, 551))
        self.l_ProcImage_pg2.setStyleSheet("background:white;")
        self.l_ProcImage_pg2.setText("")
        self.l_ProcImage_pg2.setObjectName("l_ProcImage_pg2")
        self.b_deleteOrigImage2 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.b_deleteOrigImage2.setGeometry(QtCore.QRect(740, 10, 31, 28))
        self.b_deleteOrigImage2.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteOrigImage2.setObjectName("b_deleteOrigImage2")
        self.b_SaveProcImage2 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.b_SaveProcImage2.setGeometry(QtCore.QRect(1470, 10, 31, 28))
        self.b_SaveProcImage2.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_SaveProcImage2.setObjectName("b_SaveProcImage2")
        self.b_AddOrigImage2 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.b_AddOrigImage2.setGeometry(QtCore.QRect(690, 10, 31, 28))
        self.b_AddOrigImage2.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_AddOrigImage2.setObjectName("b_AddOrigImage2")
        self.w_KrivaKoha = QtWidgets.QWidget(self.KrivaKoxa)
        self.w_KrivaKoha.setGeometry(QtCore.QRect(30, 610, 741, 241))
        self.w_KrivaKoha.setStyleSheet("border: 2px solid rgba(235, 225, 225, 0.9);")
        self.w_KrivaKoha.setObjectName("w_KrivaKoha")
        self.b_processImageKrivaKoxa = QtWidgets.QPushButton(self.w_KrivaKoha)
        self.b_processImageKrivaKoxa.setGeometry(QtCore.QRect(540, 80, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_processImageKrivaKoxa.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_processImageKrivaKoxa.setFont(font)
        self.b_processImageKrivaKoxa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_processImageKrivaKoxa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_processImageKrivaKoxa.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"    text-decoration: underline;\n"
"}")
        self.b_processImageKrivaKoxa.setObjectName("b_processImageKrivaKoxa")
        self.layoutWidget_4 = QtWidgets.QWidget(self.w_KrivaKoha)
        self.layoutWidget_4.setGeometry(QtCore.QRect(37, 41, 461, 161))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(6, 0, 6, 0)
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.colorButton_0_50 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_50.setMouseTracking(True)
        self.colorButton_0_50.setToolTipDuration(2500)
        self.colorButton_0_50.setAutoFillBackground(False)
        self.colorButton_0_50.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_50.setText("")
        self.colorButton_0_50.setCheckable(True)
        self.colorButton_0_50.setChecked(False)
        self.colorButton_0_50.setObjectName("colorButton_0_50")
        self.gridLayout_4.addWidget(self.colorButton_0_50, 0, 0, 1, 1)
        self.colorButton_0_51 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_51.setMouseTracking(True)
        self.colorButton_0_51.setToolTipDuration(2500)
        self.colorButton_0_51.setAutoFillBackground(False)
        self.colorButton_0_51.setStyleSheet("QPushButton {\n"
"    background-color: #364135;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_51.setText("")
        self.colorButton_0_51.setCheckable(True)
        self.colorButton_0_51.setChecked(False)
        self.colorButton_0_51.setObjectName("colorButton_0_51")
        self.gridLayout_4.addWidget(self.colorButton_0_51, 0, 1, 1, 1)
        self.colorButton_0_52 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_52.setMouseTracking(True)
        self.colorButton_0_52.setToolTipDuration(2500)
        self.colorButton_0_52.setAutoFillBackground(False)
        self.colorButton_0_52.setStyleSheet("QPushButton {\n"
"    background-color: #9B111E;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_52.setText("")
        self.colorButton_0_52.setCheckable(True)
        self.colorButton_0_52.setChecked(False)
        self.colorButton_0_52.setObjectName("colorButton_0_52")
        self.gridLayout_4.addWidget(self.colorButton_0_52, 0, 4, 1, 1)
        self.colorButton_0_53 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_53.setMouseTracking(True)
        self.colorButton_0_53.setToolTipDuration(2500)
        self.colorButton_0_53.setAutoFillBackground(False)
        self.colorButton_0_53.setStyleSheet("QPushButton {\n"
"    background-color: #FFA500;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_53.setText("")
        self.colorButton_0_53.setCheckable(True)
        self.colorButton_0_53.setChecked(False)
        self.colorButton_0_53.setObjectName("colorButton_0_53")
        self.gridLayout_4.addWidget(self.colorButton_0_53, 0, 5, 1, 1)
        self.colorButton_0_54 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_54.setMouseTracking(True)
        self.colorButton_0_54.setToolTipDuration(2500)
        self.colorButton_0_54.setAutoFillBackground(False)
        self.colorButton_0_54.setStyleSheet("QPushButton {\n"
"    background-color: #FFC0CB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_54.setText("")
        self.colorButton_0_54.setCheckable(True)
        self.colorButton_0_54.setChecked(False)
        self.colorButton_0_54.setObjectName("colorButton_0_54")
        self.gridLayout_4.addWidget(self.colorButton_0_54, 0, 6, 1, 1)
        self.colorButton_0_55 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_55.setMouseTracking(True)
        self.colorButton_0_55.setToolTipDuration(2500)
        self.colorButton_0_55.setAutoFillBackground(False)
        self.colorButton_0_55.setStyleSheet("QPushButton {\n"
"    background-color: #7FFFD4;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_55.setText("")
        self.colorButton_0_55.setCheckable(True)
        self.colorButton_0_55.setChecked(False)
        self.colorButton_0_55.setObjectName("colorButton_0_55")
        self.gridLayout_4.addWidget(self.colorButton_0_55, 0, 7, 1, 1)
        self.colorButton_0_56 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_56.setMouseTracking(True)
        self.colorButton_0_56.setToolTipDuration(2500)
        self.colorButton_0_56.setAutoFillBackground(False)
        self.colorButton_0_56.setStyleSheet("QPushButton {\n"
"    background-color: #90EE90;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_56.setText("")
        self.colorButton_0_56.setCheckable(True)
        self.colorButton_0_56.setChecked(False)
        self.colorButton_0_56.setObjectName("colorButton_0_56")
        self.gridLayout_4.addWidget(self.colorButton_0_56, 0, 8, 1, 1)
        self.colorButton_0_57 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_57.setMouseTracking(True)
        self.colorButton_0_57.setToolTipDuration(2500)
        self.colorButton_0_57.setAutoFillBackground(False)
        self.colorButton_0_57.setStyleSheet("QPushButton {\n"
"    background-color: #FFFDD0;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_57.setText("")
        self.colorButton_0_57.setCheckable(True)
        self.colorButton_0_57.setChecked(False)
        self.colorButton_0_57.setObjectName("colorButton_0_57")
        self.gridLayout_4.addWidget(self.colorButton_0_57, 0, 9, 1, 1)
        self.colorButton_1_50 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_50.setMouseTracking(True)
        self.colorButton_1_50.setToolTipDuration(2500)
        self.colorButton_1_50.setAutoFillBackground(False)
        self.colorButton_1_50.setStyleSheet("QPushButton {\n"
"    background-color: #2F2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_50.setText("")
        self.colorButton_1_50.setCheckable(True)
        self.colorButton_1_50.setChecked(False)
        self.colorButton_1_50.setObjectName("colorButton_1_50")
        self.gridLayout_4.addWidget(self.colorButton_1_50, 1, 0, 1, 1)
        self.colorButton_1_51 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_51.setMouseTracking(True)
        self.colorButton_1_51.setToolTipDuration(2500)
        self.colorButton_1_51.setAutoFillBackground(False)
        self.colorButton_1_51.setStyleSheet("QPushButton {\n"
"    background-color: #3B2F2F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_51.setText("")
        self.colorButton_1_51.setCheckable(True)
        self.colorButton_1_51.setChecked(False)
        self.colorButton_1_51.setObjectName("colorButton_1_51")
        self.gridLayout_4.addWidget(self.colorButton_1_51, 1, 1, 1, 1)
        self.colorButton_1_52 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_52.setMouseTracking(True)
        self.colorButton_1_52.setToolTipDuration(2500)
        self.colorButton_1_52.setAutoFillBackground(False)
        self.colorButton_1_52.setStyleSheet("QPushButton {\n"
"    background-color: #008080;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_52.setText("")
        self.colorButton_1_52.setCheckable(True)
        self.colorButton_1_52.setChecked(False)
        self.colorButton_1_52.setObjectName("colorButton_1_52")
        self.gridLayout_4.addWidget(self.colorButton_1_52, 1, 2, 1, 1)
        self.colorButton_1_53 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_53.setMouseTracking(True)
        self.colorButton_1_53.setToolTipDuration(2500)
        self.colorButton_1_53.setAutoFillBackground(False)
        self.colorButton_1_53.setStyleSheet("QPushButton {\n"
"    background-color:#006D77;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_53.setText("")
        self.colorButton_1_53.setCheckable(True)
        self.colorButton_1_53.setChecked(False)
        self.colorButton_1_53.setObjectName("colorButton_1_53")
        self.gridLayout_4.addWidget(self.colorButton_1_53, 1, 3, 1, 1)
        self.colorButton_1_54 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_54.setMouseTracking(True)
        self.colorButton_1_54.setToolTipDuration(2500)
        self.colorButton_1_54.setAutoFillBackground(False)
        self.colorButton_1_54.setStyleSheet("QPushButton {\n"
"    background-color: #A52A2A;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_54.setText("")
        self.colorButton_1_54.setCheckable(True)
        self.colorButton_1_54.setChecked(False)
        self.colorButton_1_54.setObjectName("colorButton_1_54")
        self.gridLayout_4.addWidget(self.colorButton_1_54, 1, 4, 1, 1)
        self.colorButton_1_55 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_55.setMouseTracking(True)
        self.colorButton_1_55.setToolTipDuration(2500)
        self.colorButton_1_55.setAutoFillBackground(False)
        self.colorButton_1_55.setStyleSheet("QPushButton {\n"
"    background-color: #FF0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_55.setText("")
        self.colorButton_1_55.setCheckable(True)
        self.colorButton_1_55.setChecked(False)
        self.colorButton_1_55.setObjectName("colorButton_1_55")
        self.gridLayout_4.addWidget(self.colorButton_1_55, 1, 5, 1, 1)
        self.colorButton_1_56 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_56.setMouseTracking(True)
        self.colorButton_1_56.setToolTipDuration(2500)
        self.colorButton_1_56.setAutoFillBackground(False)
        self.colorButton_1_56.setStyleSheet("QPushButton {\n"
"    background-color: #DC143C;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_56.setText("")
        self.colorButton_1_56.setCheckable(True)
        self.colorButton_1_56.setChecked(False)
        self.colorButton_1_56.setObjectName("colorButton_1_56")
        self.gridLayout_4.addWidget(self.colorButton_1_56, 1, 6, 1, 1)
        self.colorButton_1_57 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_57.setMouseTracking(True)
        self.colorButton_1_57.setToolTipDuration(2500)
        self.colorButton_1_57.setAutoFillBackground(False)
        self.colorButton_1_57.setStyleSheet("QPushButton {\n"
"    background-color: #87CEFA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_57.setText("")
        self.colorButton_1_57.setCheckable(True)
        self.colorButton_1_57.setChecked(False)
        self.colorButton_1_57.setObjectName("colorButton_1_57")
        self.gridLayout_4.addWidget(self.colorButton_1_57, 1, 7, 1, 1)
        self.colorButton_1_58 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_58.setMouseTracking(True)
        self.colorButton_1_58.setToolTipDuration(2500)
        self.colorButton_1_58.setAutoFillBackground(False)
        self.colorButton_1_58.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFE0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_58.setText("")
        self.colorButton_1_58.setCheckable(True)
        self.colorButton_1_58.setChecked(False)
        self.colorButton_1_58.setObjectName("colorButton_1_58")
        self.gridLayout_4.addWidget(self.colorButton_1_58, 1, 8, 1, 1)
        self.colorButton_1_59 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_1_59.setMouseTracking(True)
        self.colorButton_1_59.setToolTipDuration(2500)
        self.colorButton_1_59.setAutoFillBackground(False)
        self.colorButton_1_59.setStyleSheet("QPushButton {\n"
"    background-color: #F5F5F5;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_1_59.setText("")
        self.colorButton_1_59.setCheckable(True)
        self.colorButton_1_59.setChecked(False)
        self.colorButton_1_59.setObjectName("colorButton_1_59")
        self.gridLayout_4.addWidget(self.colorButton_1_59, 1, 9, 1, 1)
        self.colorButton_2_50 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_50.setMouseTracking(True)
        self.colorButton_2_50.setToolTipDuration(2500)
        self.colorButton_2_50.setAutoFillBackground(False)
        self.colorButton_2_50.setStyleSheet("QPushButton {\n"
"    background-color: #36454F;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_50.setText("")
        self.colorButton_2_50.setCheckable(True)
        self.colorButton_2_50.setChecked(False)
        self.colorButton_2_50.setObjectName("colorButton_2_50")
        self.gridLayout_4.addWidget(self.colorButton_2_50, 2, 0, 1, 1)
        self.colorButton_2_51 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_51.setMouseTracking(True)
        self.colorButton_2_51.setToolTipDuration(2500)
        self.colorButton_2_51.setAutoFillBackground(False)
        self.colorButton_2_51.setStyleSheet("QPushButton {\n"
"    background-color: #301934;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_51.setText("")
        self.colorButton_2_51.setCheckable(True)
        self.colorButton_2_51.setChecked(False)
        self.colorButton_2_51.setObjectName("colorButton_2_51")
        self.gridLayout_4.addWidget(self.colorButton_2_51, 2, 1, 1, 1)
        self.colorButton_2_52 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_52.setMouseTracking(True)
        self.colorButton_2_52.setToolTipDuration(2500)
        self.colorButton_2_52.setAutoFillBackground(False)
        self.colorButton_2_52.setStyleSheet("QPushButton {\n"
"    background-color: #485320;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_52.setText("")
        self.colorButton_2_52.setCheckable(True)
        self.colorButton_2_52.setChecked(False)
        self.colorButton_2_52.setObjectName("colorButton_2_52")
        self.gridLayout_4.addWidget(self.colorButton_2_52, 2, 2, 1, 1)
        self.colorButton_2_53 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_53.setMouseTracking(True)
        self.colorButton_2_53.setToolTipDuration(2500)
        self.colorButton_2_53.setAutoFillBackground(False)
        self.colorButton_2_53.setStyleSheet("QPushButton {\n"
"    background-color: #191970;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_53.setText("")
        self.colorButton_2_53.setCheckable(True)
        self.colorButton_2_53.setChecked(False)
        self.colorButton_2_53.setObjectName("colorButton_2_53")
        self.gridLayout_4.addWidget(self.colorButton_2_53, 2, 3, 1, 1)
        self.colorButton_2_54 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_54.setMouseTracking(True)
        self.colorButton_2_54.setToolTipDuration(2500)
        self.colorButton_2_54.setAutoFillBackground(False)
        self.colorButton_2_54.setStyleSheet("QPushButton {\n"
"    background-color: #C04000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_54.setText("")
        self.colorButton_2_54.setCheckable(True)
        self.colorButton_2_54.setChecked(False)
        self.colorButton_2_54.setObjectName("colorButton_2_54")
        self.gridLayout_4.addWidget(self.colorButton_2_54, 2, 4, 1, 1)
        self.colorButton_2_55 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_55.setMouseTracking(True)
        self.colorButton_2_55.setToolTipDuration(2500)
        self.colorButton_2_55.setAutoFillBackground(False)
        self.colorButton_2_55.setStyleSheet("QPushButton {\n"
"    background-color: #800080;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_55.setText("")
        self.colorButton_2_55.setCheckable(True)
        self.colorButton_2_55.setChecked(False)
        self.colorButton_2_55.setObjectName("colorButton_2_55")
        self.gridLayout_4.addWidget(self.colorButton_2_55, 2, 5, 1, 1)
        self.colorButton_2_56 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_56.setMouseTracking(True)
        self.colorButton_2_56.setToolTipDuration(2500)
        self.colorButton_2_56.setAutoFillBackground(False)
        self.colorButton_2_56.setStyleSheet("QPushButton {\n"
"    background-color: #00FF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_56.setText("")
        self.colorButton_2_56.setCheckable(True)
        self.colorButton_2_56.setChecked(False)
        self.colorButton_2_56.setObjectName("colorButton_2_56")
        self.gridLayout_4.addWidget(self.colorButton_2_56, 2, 6, 1, 1)
        self.colorButton_2_57 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_57.setMouseTracking(True)
        self.colorButton_2_57.setToolTipDuration(2500)
        self.colorButton_2_57.setAutoFillBackground(False)
        self.colorButton_2_57.setStyleSheet("QPushButton {\n"
"    background-color: #87CEEB;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_57.setText("")
        self.colorButton_2_57.setCheckable(True)
        self.colorButton_2_57.setChecked(False)
        self.colorButton_2_57.setObjectName("colorButton_2_57")
        self.gridLayout_4.addWidget(self.colorButton_2_57, 2, 7, 1, 1)
        self.colorButton_2_58 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_58.setMouseTracking(True)
        self.colorButton_2_58.setToolTipDuration(2500)
        self.colorButton_2_58.setAutoFillBackground(False)
        self.colorButton_2_58.setStyleSheet("QPushButton {\n"
"    background-color: #FFFF00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_58.setText("")
        self.colorButton_2_58.setCheckable(True)
        self.colorButton_2_58.setChecked(False)
        self.colorButton_2_58.setObjectName("colorButton_2_58")
        self.gridLayout_4.addWidget(self.colorButton_2_58, 2, 8, 1, 1)
        self.colorButton_2_59 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_2_59.setMouseTracking(True)
        self.colorButton_2_59.setToolTipDuration(2500)
        self.colorButton_2_59.setAutoFillBackground(False)
        self.colorButton_2_59.setStyleSheet("QPushButton {\n"
"    background-color: #D3D3D3;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_2_59.setText("")
        self.colorButton_2_59.setCheckable(True)
        self.colorButton_2_59.setChecked(False)
        self.colorButton_2_59.setObjectName("colorButton_2_59")
        self.gridLayout_4.addWidget(self.colorButton_2_59, 2, 9, 1, 1)
        self.colorButton_3_50 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_50.setMouseTracking(True)
        self.colorButton_3_50.setToolTipDuration(2500)
        self.colorButton_3_50.setAutoFillBackground(False)
        self.colorButton_3_50.setStyleSheet("QPushButton {\n"
"    background-color: #00008B;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_50.setText("")
        self.colorButton_3_50.setCheckable(True)
        self.colorButton_3_50.setChecked(False)
        self.colorButton_3_50.setObjectName("colorButton_3_50")
        self.gridLayout_4.addWidget(self.colorButton_3_50, 3, 0, 1, 1)
        self.colorButton_3_51 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_51.setMouseTracking(True)
        self.colorButton_3_51.setToolTipDuration(2500)
        self.colorButton_3_51.setAutoFillBackground(False)
        self.colorButton_3_51.setStyleSheet("QPushButton {\n"
"    background-color: #3B3C36;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_51.setText("")
        self.colorButton_3_51.setCheckable(True)
        self.colorButton_3_51.setChecked(False)
        self.colorButton_3_51.setObjectName("colorButton_3_51")
        self.gridLayout_4.addWidget(self.colorButton_3_51, 3, 1, 1, 1)
        self.colorButton_3_52 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_52.setMouseTracking(True)
        self.colorButton_3_52.setToolTipDuration(2500)
        self.colorButton_3_52.setAutoFillBackground(False)
        self.colorButton_3_52.setStyleSheet("QPushButton {\n"
"    background-color: #228B22;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_52.setText("")
        self.colorButton_3_52.setCheckable(True)
        self.colorButton_3_52.setChecked(False)
        self.colorButton_3_52.setObjectName("colorButton_3_52")
        self.gridLayout_4.addWidget(self.colorButton_3_52, 3, 2, 1, 1)
        self.colorButton_3_53 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_53.setMouseTracking(True)
        self.colorButton_3_53.setToolTipDuration(2500)
        self.colorButton_3_53.setAutoFillBackground(False)
        self.colorButton_3_53.setStyleSheet("QPushButton {\n"
"    background-color: #0F52BA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_53.setText("")
        self.colorButton_3_53.setCheckable(True)
        self.colorButton_3_53.setChecked(False)
        self.colorButton_3_53.setObjectName("colorButton_3_53")
        self.gridLayout_4.addWidget(self.colorButton_3_53, 3, 3, 1, 1)
        self.colorButton_3_54 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_54.setMouseTracking(True)
        self.colorButton_3_54.setToolTipDuration(2500)
        self.colorButton_3_54.setAutoFillBackground(False)
        self.colorButton_3_54.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_54.setText("")
        self.colorButton_3_54.setCheckable(True)
        self.colorButton_3_54.setChecked(False)
        self.colorButton_3_54.setObjectName("colorButton_3_54")
        self.gridLayout_4.addWidget(self.colorButton_3_54, 3, 4, 1, 1)
        self.colorButton_3_55 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_55.setMouseTracking(True)
        self.colorButton_3_55.setToolTipDuration(2500)
        self.colorButton_3_55.setAutoFillBackground(False)
        self.colorButton_3_55.setStyleSheet("QPushButton {\n"
"    background-color: #C71585;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_55.setText("")
        self.colorButton_3_55.setCheckable(True)
        self.colorButton_3_55.setChecked(False)
        self.colorButton_3_55.setObjectName("colorButton_3_55")
        self.gridLayout_4.addWidget(self.colorButton_3_55, 3, 5, 1, 1)
        self.colorButton_3_56 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_56.setMouseTracking(True)
        self.colorButton_3_56.setToolTipDuration(2500)
        self.colorButton_3_56.setAutoFillBackground(False)
        self.colorButton_3_56.setStyleSheet("QPushButton {\n"
"    background-color: #00FF7F;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_56.setText("")
        self.colorButton_3_56.setCheckable(True)
        self.colorButton_3_56.setChecked(False)
        self.colorButton_3_56.setObjectName("colorButton_3_56")
        self.gridLayout_4.addWidget(self.colorButton_3_56, 3, 6, 1, 1)
        self.colorButton_3_57 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_57.setMouseTracking(True)
        self.colorButton_3_57.setToolTipDuration(2500)
        self.colorButton_3_57.setAutoFillBackground(False)
        self.colorButton_3_57.setStyleSheet("QPushButton {\n"
"    background-color: #0000FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_57.setText("")
        self.colorButton_3_57.setCheckable(True)
        self.colorButton_3_57.setChecked(False)
        self.colorButton_3_57.setObjectName("colorButton_3_57")
        self.gridLayout_4.addWidget(self.colorButton_3_57, 3, 7, 1, 1)
        self.colorButton_3_58 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_58.setMouseTracking(True)
        self.colorButton_3_58.setToolTipDuration(2500)
        self.colorButton_3_58.setAutoFillBackground(False)
        self.colorButton_3_58.setStyleSheet("QPushButton {\n"
"    background-color: #FFD700;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_58.setText("")
        self.colorButton_3_58.setCheckable(True)
        self.colorButton_3_58.setChecked(False)
        self.colorButton_3_58.setObjectName("colorButton_3_58")
        self.gridLayout_4.addWidget(self.colorButton_3_58, 3, 8, 1, 1)
        self.colorButton_3_59 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_3_59.setMouseTracking(True)
        self.colorButton_3_59.setToolTipDuration(2500)
        self.colorButton_3_59.setAutoFillBackground(False)
        self.colorButton_3_59.setStyleSheet("QPushButton {\n"
"    background-color: #C0C0C0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_3_59.setText("")
        self.colorButton_3_59.setCheckable(True)
        self.colorButton_3_59.setChecked(False)
        self.colorButton_3_59.setObjectName("colorButton_3_59")
        self.gridLayout_4.addWidget(self.colorButton_3_59, 3, 9, 1, 1)
        self.colorButton_4_50 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_50.setMouseTracking(True)
        self.colorButton_4_50.setToolTipDuration(2500)
        self.colorButton_4_50.setAutoFillBackground(False)
        self.colorButton_4_50.setStyleSheet("QPushButton {\n"
"    background-color:#013220;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_50.setText("")
        self.colorButton_4_50.setCheckable(True)
        self.colorButton_4_50.setChecked(False)
        self.colorButton_4_50.setObjectName("colorButton_4_50")
        self.gridLayout_4.addWidget(self.colorButton_4_50, 4, 0, 1, 1)
        self.colorButton_4_51 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_51.setMouseTracking(True)
        self.colorButton_4_51.setToolTipDuration(2500)
        self.colorButton_4_51.setAutoFillBackground(False)
        self.colorButton_4_51.setStyleSheet("QPushButton {\n"
"    background-color:#800000;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_51.setText("")
        self.colorButton_4_51.setCheckable(True)
        self.colorButton_4_51.setChecked(False)
        self.colorButton_4_51.setObjectName("colorButton_4_51")
        self.gridLayout_4.addWidget(self.colorButton_4_51, 4, 1, 1, 1)
        self.colorButton_4_52 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_52.setMouseTracking(True)
        self.colorButton_4_52.setToolTipDuration(2500)
        self.colorButton_4_52.setAutoFillBackground(False)
        self.colorButton_4_52.setStyleSheet("QPushButton {\n"
"    background-color: #8B4513;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Коли кнопка в стані наведення */\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"/* Коли кнопка натиснута й активна */\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_52.setText("")
        self.colorButton_4_52.setCheckable(True)
        self.colorButton_4_52.setChecked(False)
        self.colorButton_4_52.setObjectName("colorButton_4_52")
        self.gridLayout_4.addWidget(self.colorButton_4_52, 4, 2, 1, 1)
        self.colorButton_4_53 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_53.setMouseTracking(True)
        self.colorButton_4_53.setToolTipDuration(2500)
        self.colorButton_4_53.setAutoFillBackground(False)
        self.colorButton_4_53.setStyleSheet("QPushButton {\n"
"    background-color: #8B0000;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_53.setText("")
        self.colorButton_4_53.setCheckable(True)
        self.colorButton_4_53.setChecked(False)
        self.colorButton_4_53.setObjectName("colorButton_4_53")
        self.gridLayout_4.addWidget(self.colorButton_4_53, 4, 3, 1, 1)
        self.colorButton_4_54 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_54.setMouseTracking(True)
        self.colorButton_4_54.setToolTipDuration(2500)
        self.colorButton_4_54.setAutoFillBackground(False)
        self.colorButton_4_54.setStyleSheet("QPushButton {\n"
"    background-color: #FF8C00;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_54.setText("")
        self.colorButton_4_54.setCheckable(True)
        self.colorButton_4_54.setChecked(False)
        self.colorButton_4_54.setObjectName("colorButton_4_54")
        self.gridLayout_4.addWidget(self.colorButton_4_54, 4, 4, 1, 1)
        self.colorButton_4_55 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_55.setMouseTracking(True)
        self.colorButton_4_55.setToolTipDuration(2500)
        self.colorButton_4_55.setAutoFillBackground(False)
        self.colorButton_4_55.setStyleSheet("QPushButton {\n"
"    background-color: #FF00FF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_55.setText("")
        self.colorButton_4_55.setCheckable(True)
        self.colorButton_4_55.setChecked(False)
        self.colorButton_4_55.setObjectName("colorButton_4_55")
        self.gridLayout_4.addWidget(self.colorButton_4_55, 4, 5, 1, 1)
        self.colorButton_4_56 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_56.setMouseTracking(True)
        self.colorButton_4_56.setToolTipDuration(2500)
        self.colorButton_4_56.setAutoFillBackground(False)
        self.colorButton_4_56.setStyleSheet("QPushButton {\n"
"    background-color: #40E0D0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_56.setText("")
        self.colorButton_4_56.setCheckable(True)
        self.colorButton_4_56.setChecked(False)
        self.colorButton_4_56.setObjectName("colorButton_4_56")
        self.gridLayout_4.addWidget(self.colorButton_4_56, 4, 6, 1, 1)
        self.colorButton_4_57 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_57.setMouseTracking(True)
        self.colorButton_4_57.setToolTipDuration(2500)
        self.colorButton_4_57.setAutoFillBackground(False)
        self.colorButton_4_57.setStyleSheet("QPushButton {\n"
"    background-color: #E6E6FA;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_57.setText("")
        self.colorButton_4_57.setCheckable(True)
        self.colorButton_4_57.setChecked(False)
        self.colorButton_4_57.setObjectName("colorButton_4_57")
        self.gridLayout_4.addWidget(self.colorButton_4_57, 4, 7, 1, 1)
        self.colorButton_4_58 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_58.setMouseTracking(True)
        self.colorButton_4_58.setToolTipDuration(2500)
        self.colorButton_4_58.setAutoFillBackground(False)
        self.colorButton_4_58.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFF0;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_58.setText("")
        self.colorButton_4_58.setCheckable(True)
        self.colorButton_4_58.setChecked(False)
        self.colorButton_4_58.setObjectName("colorButton_4_58")
        self.gridLayout_4.addWidget(self.colorButton_4_58, 4, 8, 1, 1)
        self.colorButton_4_59 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_4_59.setMouseTracking(True)
        self.colorButton_4_59.setToolTipDuration(2500)
        self.colorButton_4_59.setAutoFillBackground(False)
        self.colorButton_4_59.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_4_59.setText("")
        self.colorButton_4_59.setCheckable(True)
        self.colorButton_4_59.setChecked(False)
        self.colorButton_4_59.setObjectName("colorButton_4_59")
        self.gridLayout_4.addWidget(self.colorButton_4_59, 4, 9, 1, 1)
        self.colorButton_0_58 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_58.setMouseTracking(True)
        self.colorButton_0_58.setToolTipDuration(2500)
        self.colorButton_0_58.setAutoFillBackground(False)
        self.colorButton_0_58.setStyleSheet("QPushButton {\n"
"    background-color: #4B0082;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_58.setText("")
        self.colorButton_0_58.setCheckable(True)
        self.colorButton_0_58.setChecked(False)
        self.colorButton_0_58.setObjectName("colorButton_0_58")
        self.gridLayout_4.addWidget(self.colorButton_0_58, 0, 2, 1, 1)
        self.colorButton_0_59 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.colorButton_0_59.setMouseTracking(True)
        self.colorButton_0_59.setToolTipDuration(2500)
        self.colorButton_0_59.setAutoFillBackground(False)
        self.colorButton_0_59.setStyleSheet("QPushButton {\n"
"    background-color: #006A4E;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    border: 3px solid black;\n"
"}\n"
"")
        self.colorButton_0_59.setText("")
        self.colorButton_0_59.setCheckable(True)
        self.colorButton_0_59.setChecked(False)
        self.colorButton_0_59.setObjectName("colorButton_0_59")
        self.gridLayout_4.addWidget(self.colorButton_0_59, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.w_KrivaKoha)
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QtCore.QRect(90, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(self.KrivaKoxa)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.KrivaKoxa)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 291, 981))
        self.listWidget_2.setMouseTracking(True)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget_2.setTabKeyNavigation(False)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_2.addItem(item)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(290, 10, 1631, 931))
        self.stackedWidget_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, \n"
"    stop:0 rgba(100, 50, 150, 200), \n"
"    stop:0.427447 rgba(80, 100, 180, 200), \n"
"    stop:1 rgba(160, 100, 180, 220));\n"
"")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Encryption = QtWidgets.QWidget()
        self.Encryption.setObjectName("Encryption")
        self.b_AddOrigImageEnc = QtWidgets.QPushButton(self.Encryption)
        self.b_AddOrigImageEnc.setGeometry(QtCore.QRect(700, 20, 31, 28))
        self.b_AddOrigImageEnc.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_AddOrigImageEnc.setObjectName("b_AddOrigImageEnc")
        self.l_OrigImageEnc = QtWidgets.QLabel(self.Encryption)
        self.l_OrigImageEnc.setGeometry(QtCore.QRect(40, 50, 741, 551))
        self.l_OrigImageEnc.setStyleSheet("background:white;")
        self.l_OrigImageEnc.setText("")
        self.l_OrigImageEnc.setObjectName("l_OrigImageEnc")
        self.b_deleteOrigImageEnc = QtWidgets.QPushButton(self.Encryption)
        self.b_deleteOrigImageEnc.setGeometry(QtCore.QRect(750, 20, 31, 28))
        self.b_deleteOrigImageEnc.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteOrigImageEnc.setObjectName("b_deleteOrigImageEnc")
        self.b_deleteProcImageEnc = QtWidgets.QPushButton(self.Encryption)
        self.b_deleteProcImageEnc.setGeometry(QtCore.QRect(1530, 20, 31, 28))
        self.b_deleteProcImageEnc.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteProcImageEnc.setObjectName("b_deleteProcImageEnc")
        self.l_ProcImageEnc = QtWidgets.QLabel(self.Encryption)
        self.l_ProcImageEnc.setGeometry(QtCore.QRect(820, 50, 741, 551))
        self.l_ProcImageEnc.setStyleSheet("background:white;")
        self.l_ProcImageEnc.setText("")
        self.l_ProcImageEnc.setObjectName("l_ProcImageEnc")
        self.b_SaveProcImageEnc = QtWidgets.QPushButton(self.Encryption)
        self.b_SaveProcImageEnc.setGeometry(QtCore.QRect(1480, 20, 31, 28))
        self.b_SaveProcImageEnc.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_SaveProcImageEnc.setObjectName("b_SaveProcImageEnc")
        self.frame_2 = QtWidgets.QFrame(self.Encryption)
        self.frame_2.setGeometry(QtCore.QRect(590, 640, 431, 151))
        self.frame_2.setStyleSheet("border: 2px solid rgba(235, 225, 225, 0.9);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.le_EncryptedText = QtWidgets.QLineEdit(self.frame_2)
        self.le_EncryptedText.setEnabled(True)
        self.le_EncryptedText.setGeometry(QtCore.QRect(20, 80, 391, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.le_EncryptedText.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.le_EncryptedText.setFont(font)
        self.le_EncryptedText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.le_EncryptedText.setAutoFillBackground(False)
        self.le_EncryptedText.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"}")
        self.le_EncryptedText.setText("")
        self.le_EncryptedText.setMaxLength(50)
        self.le_EncryptedText.setFrame(False)
        self.le_EncryptedText.setReadOnly(False)
        self.le_EncryptedText.setObjectName("le_EncryptedText")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setEnabled(False)
        self.label_19.setGeometry(QtCore.QRect(20, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setMouseTracking(True)
        self.label_19.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.b_ProcImageEncryptedText = QtWidgets.QPushButton(self.frame_2)
        self.b_ProcImageEncryptedText.setGeometry(QtCore.QRect(220, 30, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_ProcImageEncryptedText.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_ProcImageEncryptedText.setFont(font)
        self.b_ProcImageEncryptedText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_ProcImageEncryptedText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_ProcImageEncryptedText.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"    text-decoration: underline;\n"
"}")
        self.b_ProcImageEncryptedText.setObjectName("b_ProcImageEncryptedText")
        self.stackedWidget_2.addWidget(self.Encryption)
        self.Decryption = QtWidgets.QWidget()
        self.Decryption.setObjectName("Decryption")
        self.b_deleteOrigImageDec = QtWidgets.QPushButton(self.Decryption)
        self.b_deleteOrigImageDec.setGeometry(QtCore.QRect(750, 20, 31, 28))
        self.b_deleteOrigImageDec.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteOrigImageDec.setObjectName("b_deleteOrigImageDec")
        self.l_OrigImageDec = QtWidgets.QLabel(self.Decryption)
        self.l_OrigImageDec.setGeometry(QtCore.QRect(40, 50, 741, 551))
        self.l_OrigImageDec.setStyleSheet("background:white;")
        self.l_OrigImageDec.setText("")
        self.l_OrigImageDec.setObjectName("l_OrigImageDec")
        self.b_AddOrigImageDec = QtWidgets.QPushButton(self.Decryption)
        self.b_AddOrigImageDec.setGeometry(QtCore.QRect(700, 20, 31, 28))
        self.b_AddOrigImageDec.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_AddOrigImageDec.setObjectName("b_AddOrigImageDec")
        self.b_deleteProcImageDec = QtWidgets.QPushButton(self.Decryption)
        self.b_deleteProcImageDec.setGeometry(QtCore.QRect(1530, 20, 31, 28))
        self.b_deleteProcImageDec.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_deleteProcImageDec.setObjectName("b_deleteProcImageDec")
        self.l_ProcImageDec = QtWidgets.QLabel(self.Decryption)
        self.l_ProcImageDec.setGeometry(QtCore.QRect(820, 50, 741, 551))
        self.l_ProcImageDec.setStyleSheet("background:white;")
        self.l_ProcImageDec.setText("")
        self.l_ProcImageDec.setObjectName("l_ProcImageDec")
        self.b_SaveProcImageDec = QtWidgets.QPushButton(self.Decryption)
        self.b_SaveProcImageDec.setGeometry(QtCore.QRect(1480, 20, 31, 28))
        self.b_SaveProcImageDec.setStyleSheet("background:purple;\n"
"color:white;\n"
"")
        self.b_SaveProcImageDec.setObjectName("b_SaveProcImageDec")
        self.frame = QtWidgets.QFrame(self.Decryption)
        self.frame.setGeometry(QtCore.QRect(580, 630, 431, 211))
        self.frame.setStyleSheet("border: 2px solid rgba(235, 225, 225, 0.9);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setEnabled(False)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.b_ProcImageDecryptedText = QtWidgets.QPushButton(self.frame)
        self.b_ProcImageDecryptedText.setGeometry(QtCore.QRect(220, 20, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_ProcImageDecryptedText.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_ProcImageDecryptedText.setFont(font)
        self.b_ProcImageDecryptedText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_ProcImageDecryptedText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_ProcImageDecryptedText.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"    text-decoration: underline;\n"
"}")
        self.b_ProcImageDecryptedText.setObjectName("b_ProcImageDecryptedText")
        self.te_DecryptedText = QtWidgets.QTextEdit(self.frame)
        self.te_DecryptedText.setGeometry(QtCore.QRect(20, 70, 391, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.te_DecryptedText.setFont(font)
        self.te_DecryptedText.setStyleSheet("color:white;")
        self.te_DecryptedText.setObjectName("te_DecryptedText")
        self.frame.raise_()
        self.b_deleteOrigImageDec.raise_()
        self.l_OrigImageDec.raise_()
        self.b_AddOrigImageDec.raise_()
        self.b_deleteProcImageDec.raise_()
        self.l_ProcImageDec.raise_()
        self.b_SaveProcImageDec.raise_()
        self.stackedWidget_2.addWidget(self.Decryption)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tw_History = QtWidgets.QTableWidget(self.tab_3)
        self.tw_History.setGeometry(QtCore.QRect(40, 40, 1571, 801))
        self.tw_History.setObjectName("tw_History")
        self.tw_History.setColumnCount(6)
        self.tw_History.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tw_History.setHorizontalHeaderItem(5, item)
        self.tw_History.horizontalHeader().setDefaultSectionSize(250)
        self.b_RestoreHistory = QtWidgets.QPushButton(self.tab_3)
        self.b_RestoreHistory.setGeometry(QtCore.QRect(1660, 350, 201, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 137, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.b_RestoreHistory.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_RestoreHistory.setFont(font)
        self.b_RestoreHistory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_RestoreHistory.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_RestoreHistory.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.3);\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    color: #fff;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover {\n"
"    font-weight:bold;\n"
"    border: 2px solid rgba(235, 225, 225, 0.9);\n"
"    background-color: rgba(200, 200, 200, 0.5);\n"
"}")
        self.b_RestoreHistory.setObjectName("b_RestoreHistory")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(110, 120, 491, 91))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(110, 250, 491, 91))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(110, 400, 491, 91))
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_4, "")
        self.b_exit = QtWidgets.QPushButton(self.centralwidget)
        self.b_exit.setGeometry(QtCore.QRect(1800, 10, 81, 28))
        self.b_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_exit.setMouseTracking(True)
        self.b_exit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.b_exit.setStyleSheet("color:white;\n"
"font-weight:bold;")
        self.b_exit.setObjectName("b_exit")
        self.la_username = QtWidgets.QLabel(self.centralwidget)
        self.la_username.setGeometry(QtCore.QRect(1564, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.la_username.setFont(font)
        self.la_username.setStyleSheet("background:transparent;\n"
"color:white;\n"
"")
        self.la_username.setObjectName("la_username")
        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget_2.setCurrentRow(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Main Menu"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainMenu", "ГРА ЖИТТЯ"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainMenu", "ШУМ ПЕРЛІНА"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainMenu", "КРИВА КОХА"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.b_deleteOrigImage0.setText(_translate("MainMenu", "X"))
        self.b_AddOrigImage0.setText(_translate("MainMenu", "+"))
        self.b_deleteProcImage0.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImage0.setText(_translate("MainMenu", "+"))
        self.b_processImageGOF.setText(_translate("MainMenu", "Обробити фото"))
        self.colorButton_0_0.setToolTip(_translate("MainMenu", "Чорний"))
        self.colorButton_0_1.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_0_4.setToolTip(_translate("MainMenu", "Червоний рубін"))
        self.colorButton_0_5.setToolTip(_translate("MainMenu", "Помаранчевий"))
        self.colorButton_0_6.setToolTip(_translate("MainMenu", "Рожевий"))
        self.colorButton_0_7.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.colorButton_0_8.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_9.setToolTip(_translate("MainMenu", "Кремовий"))
        self.colorButton_1_0.setToolTip(_translate("MainMenu", "Темно-сірий"))
        self.colorButton_1_1.setToolTip(_translate("MainMenu", "Темно-коричневий"))
        self.colorButton_1_2.setToolTip(_translate("MainMenu", "Темний бірюзовий"))
        self.colorButton_1_3.setToolTip(_translate("MainMenu", "Морська хвиля (темна)"))
        self.colorButton_1_4.setToolTip(_translate("MainMenu", "Каштановий"))
        self.colorButton_1_5.setToolTip(_translate("MainMenu", "Червоний"))
        self.colorButton_1_6.setToolTip(_translate("MainMenu", "Малиновий"))
        self.colorButton_1_7.setToolTip(_translate("MainMenu", "Блакитний"))
        self.colorButton_1_8.setToolTip(_translate("MainMenu", "Світло-жовтий"))
        self.colorButton_1_9.setToolTip(_translate("MainMenu", "Білий дим"))
        self.colorButton_2_0.setToolTip(_translate("MainMenu", "Антрацитовий"))
        self.colorButton_2_1.setToolTip(_translate("MainMenu", "Темно-сливовий"))
        self.colorButton_2_2.setToolTip(_translate("MainMenu", "Темний хакі"))
        self.colorButton_2_3.setToolTip(_translate("MainMenu", "Глибокий синій"))
        self.colorButton_2_4.setToolTip(_translate("MainMenu", "Махагон"))
        self.colorButton_2_5.setToolTip(_translate("MainMenu", "Пурпуровий"))
        self.colorButton_2_6.setToolTip(_translate("MainMenu", "Яскраво-зелений"))
        self.colorButton_2_7.setToolTip(_translate("MainMenu", "Небесно-блакитний"))
        self.colorButton_2_8.setToolTip(_translate("MainMenu", "Жовтий"))
        self.colorButton_2_9.setToolTip(_translate("MainMenu", "Світло-сірий"))
        self.colorButton_3_0.setToolTip(_translate("MainMenu", "Темно-синій"))
        self.colorButton_3_1.setToolTip(_translate("MainMenu", "Графіт"))
        self.colorButton_3_2.setToolTip(_translate("MainMenu", "Лісовий зелений"))
        self.colorButton_3_3.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.colorButton_3_4.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_5.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_6.setToolTip(_translate("MainMenu", "Весняний зелений"))
        self.colorButton_3_7.setToolTip(_translate("MainMenu", "Синій (стандартний)"))
        self.colorButton_3_8.setToolTip(_translate("MainMenu", "Золотий"))
        self.colorButton_3_9.setToolTip(_translate("MainMenu", "Сріблястий"))
        self.colorButton_4_0.setToolTip(_translate("MainMenu", "Темно-зелений"))
        self.colorButton_4_1.setToolTip(_translate("MainMenu", "Бордовий"))
        self.colorButton_4_2.setToolTip(_translate("MainMenu", "Коричневий"))
        self.colorButton_4_3.setToolTip(_translate("MainMenu", "Темно-червоний"))
        self.colorButton_4_4.setToolTip(_translate("MainMenu", "Темно-оранжевий"))
        self.colorButton_4_5.setToolTip(_translate("MainMenu", "Фуксія"))
        self.colorButton_4_6.setToolTip(_translate("MainMenu", "Бірюзовий"))
        self.colorButton_4_7.setToolTip(_translate("MainMenu", "Лавандовий"))
        self.colorButton_4_8.setToolTip(_translate("MainMenu", "Слонова кістка"))
        self.colorButton_4_9.setToolTip(_translate("MainMenu", "Білий"))
        self.colorButton_0_2.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_3.setToolTip(_translate("MainMenu", "Пляшково-зелений"))
        self.label_13.setText(_translate("MainMenu", "Палітра кольорів"))
        self.label.setText(_translate("MainMenu", "1"))
        self.b_deleteOrigImage1.setText(_translate("MainMenu", "X"))
        self.b_AddOrigImage1.setText(_translate("MainMenu", "+"))
        self.b_deleteProcImage1.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImage1.setText(_translate("MainMenu", "+"))
        self.b_processImageNP.setText(_translate("MainMenu", "Обробити фото"))
        self.colorButton_0_40.setToolTip(_translate("MainMenu", "Чорний"))
        self.colorButton_0_41.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_0_42.setToolTip(_translate("MainMenu", "Червоний рубін"))
        self.colorButton_0_43.setToolTip(_translate("MainMenu", "Помаранчевий"))
        self.colorButton_0_44.setToolTip(_translate("MainMenu", "Рожевий"))
        self.colorButton_0_45.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.colorButton_0_46.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_47.setToolTip(_translate("MainMenu", "Кремовий"))
        self.colorButton_1_40.setToolTip(_translate("MainMenu", "Темно-сірий"))
        self.colorButton_1_41.setToolTip(_translate("MainMenu", "Темно-коричневий"))
        self.colorButton_1_42.setToolTip(_translate("MainMenu", "Темний бірюзовий"))
        self.colorButton_1_43.setToolTip(_translate("MainMenu", "Морська хвиля (темна)"))
        self.colorButton_1_44.setToolTip(_translate("MainMenu", "Каштановий"))
        self.colorButton_1_45.setToolTip(_translate("MainMenu", "Червоний"))
        self.colorButton_1_46.setToolTip(_translate("MainMenu", "Малиновий"))
        self.colorButton_1_47.setToolTip(_translate("MainMenu", "Блакитний"))
        self.colorButton_1_48.setToolTip(_translate("MainMenu", "Світло-жовтий"))
        self.colorButton_1_49.setToolTip(_translate("MainMenu", "Білий дим"))
        self.colorButton_2_40.setToolTip(_translate("MainMenu", "Антрацитовий"))
        self.colorButton_2_41.setToolTip(_translate("MainMenu", "Темно-сливовий"))
        self.colorButton_2_42.setToolTip(_translate("MainMenu", "Темний хакі"))
        self.colorButton_2_43.setToolTip(_translate("MainMenu", "Глибокий синій"))
        self.colorButton_2_44.setToolTip(_translate("MainMenu", "Махагон"))
        self.colorButton_2_45.setToolTip(_translate("MainMenu", "Пурпуровий"))
        self.colorButton_2_46.setToolTip(_translate("MainMenu", "Яскраво-зелений"))
        self.colorButton_2_47.setToolTip(_translate("MainMenu", "Небесно-блакитний"))
        self.colorButton_2_48.setToolTip(_translate("MainMenu", "Жовтий"))
        self.colorButton_2_49.setToolTip(_translate("MainMenu", "Світло-сірий"))
        self.colorButton_3_40.setToolTip(_translate("MainMenu", "Темно-синій"))
        self.colorButton_3_41.setToolTip(_translate("MainMenu", "Графіт"))
        self.colorButton_3_42.setToolTip(_translate("MainMenu", "Лісовий зелений"))
        self.colorButton_3_43.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.colorButton_3_44.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_45.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_46.setToolTip(_translate("MainMenu", "Весняний зелений"))
        self.colorButton_3_47.setToolTip(_translate("MainMenu", "Синій (стандартний)"))
        self.colorButton_3_48.setToolTip(_translate("MainMenu", "Золотий"))
        self.colorButton_3_49.setToolTip(_translate("MainMenu", "Сріблястий"))
        self.colorButton_4_40.setToolTip(_translate("MainMenu", "Темно-зелений"))
        self.colorButton_4_41.setToolTip(_translate("MainMenu", "Бордовий"))
        self.colorButton_4_42.setToolTip(_translate("MainMenu", "Коричневий"))
        self.colorButton_4_43.setToolTip(_translate("MainMenu", "Темно-червоний"))
        self.colorButton_4_44.setToolTip(_translate("MainMenu", "Темно-оранжевий"))
        self.colorButton_4_45.setToolTip(_translate("MainMenu", "Фуксія"))
        self.colorButton_4_46.setToolTip(_translate("MainMenu", "Бірюзовий"))
        self.colorButton_4_47.setToolTip(_translate("MainMenu", "Лавандовий"))
        self.colorButton_4_48.setToolTip(_translate("MainMenu", "Слонова кістка"))
        self.colorButton_4_49.setToolTip(_translate("MainMenu", "Білий"))
        self.colorButton_0_48.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_49.setToolTip(_translate("MainMenu", "Пляшково-зелений"))
        self.label_14.setText(_translate("MainMenu", "Палітра кольорів"))
        self.label_2.setText(_translate("MainMenu", "2"))
        self.b_deleteProcImage2.setText(_translate("MainMenu", "X"))
        self.b_deleteOrigImage2.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImage2.setText(_translate("MainMenu", "+"))
        self.b_AddOrigImage2.setText(_translate("MainMenu", "+"))
        self.b_processImageKrivaKoxa.setText(_translate("MainMenu", "Обробити фото"))
        self.colorButton_0_50.setToolTip(_translate("MainMenu", "Чорний"))
        self.colorButton_0_51.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_0_52.setToolTip(_translate("MainMenu", "Червоний рубін"))
        self.colorButton_0_53.setToolTip(_translate("MainMenu", "Помаранчевий"))
        self.colorButton_0_54.setToolTip(_translate("MainMenu", "Рожевий"))
        self.colorButton_0_55.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.colorButton_0_56.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_57.setToolTip(_translate("MainMenu", "Кремовий"))
        self.colorButton_1_50.setToolTip(_translate("MainMenu", "Темно-сірий"))
        self.colorButton_1_51.setToolTip(_translate("MainMenu", "Темно-коричневий"))
        self.colorButton_1_52.setToolTip(_translate("MainMenu", "Темний бірюзовий"))
        self.colorButton_1_53.setToolTip(_translate("MainMenu", "Морська хвиля (темна)"))
        self.colorButton_1_54.setToolTip(_translate("MainMenu", "Каштановий"))
        self.colorButton_1_55.setToolTip(_translate("MainMenu", "Червоний"))
        self.colorButton_1_56.setToolTip(_translate("MainMenu", "Малиновий"))
        self.colorButton_1_57.setToolTip(_translate("MainMenu", "Блакитний"))
        self.colorButton_1_58.setToolTip(_translate("MainMenu", "Світло-жовтий"))
        self.colorButton_1_59.setToolTip(_translate("MainMenu", "Білий дим"))
        self.colorButton_2_50.setToolTip(_translate("MainMenu", "Антрацитовий"))
        self.colorButton_2_51.setToolTip(_translate("MainMenu", "Темно-сливовий"))
        self.colorButton_2_52.setToolTip(_translate("MainMenu", "Темний хакі"))
        self.colorButton_2_53.setToolTip(_translate("MainMenu", "Глибокий синій"))
        self.colorButton_2_54.setToolTip(_translate("MainMenu", "Махагон"))
        self.colorButton_2_55.setToolTip(_translate("MainMenu", "Пурпуровий"))
        self.colorButton_2_56.setToolTip(_translate("MainMenu", "Яскраво-зелений"))
        self.colorButton_2_57.setToolTip(_translate("MainMenu", "Небесно-блакитний"))
        self.colorButton_2_58.setToolTip(_translate("MainMenu", "Жовтий"))
        self.colorButton_2_59.setToolTip(_translate("MainMenu", "Світло-сірий"))
        self.colorButton_3_50.setToolTip(_translate("MainMenu", "Темно-синій"))
        self.colorButton_3_51.setToolTip(_translate("MainMenu", "Графіт"))
        self.colorButton_3_52.setToolTip(_translate("MainMenu", "Лісовий зелений"))
        self.colorButton_3_53.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.colorButton_3_54.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_55.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_56.setToolTip(_translate("MainMenu", "Весняний зелений"))
        self.colorButton_3_57.setToolTip(_translate("MainMenu", "Синій (стандартний)"))
        self.colorButton_3_58.setToolTip(_translate("MainMenu", "Золотий"))
        self.colorButton_3_59.setToolTip(_translate("MainMenu", "Сріблястий"))
        self.colorButton_4_50.setToolTip(_translate("MainMenu", "Темно-зелений"))
        self.colorButton_4_51.setToolTip(_translate("MainMenu", "Бордовий"))
        self.colorButton_4_52.setToolTip(_translate("MainMenu", "Коричневий"))
        self.colorButton_4_53.setToolTip(_translate("MainMenu", "Темно-червоний"))
        self.colorButton_4_54.setToolTip(_translate("MainMenu", "Темно-оранжевий"))
        self.colorButton_4_55.setToolTip(_translate("MainMenu", "Фуксія"))
        self.colorButton_4_56.setToolTip(_translate("MainMenu", "Бірюзовий"))
        self.colorButton_4_57.setToolTip(_translate("MainMenu", "Лавандовий"))
        self.colorButton_4_58.setToolTip(_translate("MainMenu", "Слонова кістка"))
        self.colorButton_4_59.setToolTip(_translate("MainMenu", "Білий"))
        self.colorButton_0_58.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_59.setToolTip(_translate("MainMenu", "Пляшково-зелений"))
        self.label_15.setText(_translate("MainMenu", "Палітра кольорів"))
        self.label_3.setText(_translate("MainMenu", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainMenu", "Генерація"))
        self.listWidget_2.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainMenu", "ШИФРУВАННЯ"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainMenu", "ДЕШИФРУВАННЯ"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.b_AddOrigImageEnc.setText(_translate("MainMenu", "+"))
        self.b_deleteOrigImageEnc.setText(_translate("MainMenu", "X"))
        self.b_deleteProcImageEnc.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImageEnc.setText(_translate("MainMenu", "+"))
        self.le_EncryptedText.setPlaceholderText(_translate("MainMenu", "Зашифрований текст"))
        self.label_19.setText(_translate("MainMenu", "ШИФРУВАННЯ"))
        self.b_ProcImageEncryptedText.setText(_translate("MainMenu", "Обробити фото"))
        self.b_deleteOrigImageDec.setText(_translate("MainMenu", "X"))
        self.b_AddOrigImageDec.setText(_translate("MainMenu", "+"))
        self.b_deleteProcImageDec.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImageDec.setText(_translate("MainMenu", "+"))
        self.label_18.setText(_translate("MainMenu", "ДЕШИФРУВАННЯ"))
        self.b_ProcImageDecryptedText.setText(_translate("MainMenu", "Обробити фото"))
        self.te_DecryptedText.setHtml(_translate("MainMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainMenu", "Стеганографія"))
        item = self.tw_History.horizontalHeaderItem(0)
        item.setText(_translate("MainMenu", "Шлях оригіналу"))
        item = self.tw_History.horizontalHeaderItem(1)
        item.setText(_translate("MainMenu", "Шлях обробленого"))
        item = self.tw_History.horizontalHeaderItem(2)
        item.setText(_translate("MainMenu", "Метод обробки"))
        item = self.tw_History.horizontalHeaderItem(3)
        item.setText(_translate("MainMenu", "Комбінації кольорів"))
        item = self.tw_History.horizontalHeaderItem(4)
        item.setText(_translate("MainMenu", "Зашифроване повідомлення"))
        item = self.tw_History.horizontalHeaderItem(5)
        item.setText(_translate("MainMenu", "Розшифроване повідомлення"))
        self.b_RestoreHistory.setText(_translate("MainMenu", "Відновити"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainMenu", "Історія"))
        self.label_9.setText(_translate("MainMenu", "Про Андрія:"))
        self.label_10.setText(_translate("MainMenu", "Про Софію:"))
        self.label_11.setText(_translate("MainMenu", "Про Руслана:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainMenu", "Інформація"))
        self.b_exit.setText(_translate("MainMenu", "Вийти"))
        self.la_username.setText(_translate("MainMenu", "Noname"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
