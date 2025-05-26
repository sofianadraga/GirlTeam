
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
        self.stackedWidget.setGeometry(QtCore.QRect(190, 0, 1701, 981))
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
        self.label = QtWidgets.QLabel(self.GameOfLife)
        self.label.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label.setStyleSheet("background:transparent;")
        self.label.setObjectName("label")
        self.b_processImageGOF = QtWidgets.QPushButton(self.GameOfLife)
        self.b_processImageGOF.setGeometry(QtCore.QRect(706, 790, 171, 41))
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
        self.pushButton_7 = QtWidgets.QPushButton(self.GameOfLife)
        self.pushButton_7.setGeometry(QtCore.QRect(425, 681, 241, 91))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.GameOfLife)
        self.pushButton_8.setGeometry(QtCore.QRect(676, 681, 241, 91))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.GameOfLife)
        self.pushButton_9.setGeometry(QtCore.QRect(927, 681, 241, 91))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.colorButton_0_66 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_66.setGeometry(QtCore.QRect(480, 690, 41, 16))
        self.colorButton_0_66.setMouseTracking(True)
        self.colorButton_0_66.setToolTipDuration(2500)
        self.colorButton_0_66.setAutoFillBackground(False)
        self.colorButton_0_66.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_66.setText("")
        self.colorButton_0_66.setCheckable(True)
        self.colorButton_0_66.setChecked(False)
        self.colorButton_0_66.setObjectName("colorButton_0_66")
        self.colorButton_0_67 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_67.setGeometry(QtCore.QRect(571, 690, 41, 16))
        self.colorButton_0_67.setMouseTracking(True)
        self.colorButton_0_67.setToolTipDuration(2500)
        self.colorButton_0_67.setAutoFillBackground(False)
        self.colorButton_0_67.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_67.setText("")
        self.colorButton_0_67.setCheckable(True)
        self.colorButton_0_67.setChecked(False)
        self.colorButton_0_67.setObjectName("colorButton_0_67")
        self.colorButton_0_68 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_68.setGeometry(QtCore.QRect(525, 690, 42, 16))
        self.colorButton_0_68.setMouseTracking(True)
        self.colorButton_0_68.setToolTipDuration(2500)
        self.colorButton_0_68.setAutoFillBackground(False)
        self.colorButton_0_68.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_68.setText("")
        self.colorButton_0_68.setCheckable(True)
        self.colorButton_0_68.setChecked(False)
        self.colorButton_0_68.setObjectName("colorButton_0_68")
        self.colorButton_3_66 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_3_66.setGeometry(QtCore.QRect(820, 690, 42, 16))
        self.colorButton_3_66.setMouseTracking(True)
        self.colorButton_3_66.setToolTipDuration(2500)
        self.colorButton_3_66.setAutoFillBackground(False)
        self.colorButton_3_66.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_66.setText("")
        self.colorButton_3_66.setCheckable(True)
        self.colorButton_3_66.setChecked(False)
        self.colorButton_3_66.setObjectName("colorButton_3_66")
        self.colorButton_3_67 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_3_67.setGeometry(QtCore.QRect(775, 690, 41, 16))
        self.colorButton_3_67.setMouseTracking(True)
        self.colorButton_3_67.setToolTipDuration(2500)
        self.colorButton_3_67.setAutoFillBackground(False)
        self.colorButton_3_67.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_67.setText("")
        self.colorButton_3_67.setCheckable(True)
        self.colorButton_3_67.setChecked(False)
        self.colorButton_3_67.setObjectName("colorButton_3_67")
        self.colorButton_3_68 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_3_68.setGeometry(QtCore.QRect(730, 690, 41, 16))
        self.colorButton_3_68.setMouseTracking(True)
        self.colorButton_3_68.setToolTipDuration(2500)
        self.colorButton_3_68.setAutoFillBackground(False)
        self.colorButton_3_68.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_68.setText("")
        self.colorButton_3_68.setCheckable(True)
        self.colorButton_3_68.setChecked(False)
        self.colorButton_3_68.setObjectName("colorButton_3_68")
        self.colorButton_0_69 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_69.setGeometry(QtCore.QRect(980, 690, 41, 16))
        self.colorButton_0_69.setMouseTracking(True)
        self.colorButton_0_69.setToolTipDuration(2500)
        self.colorButton_0_69.setAutoFillBackground(False)
        self.colorButton_0_69.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_69.setText("")
        self.colorButton_0_69.setCheckable(True)
        self.colorButton_0_69.setChecked(False)
        self.colorButton_0_69.setObjectName("colorButton_0_69")
        self.colorButton_0_70 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_70.setGeometry(QtCore.QRect(1070, 690, 42, 16))
        self.colorButton_0_70.setMouseTracking(True)
        self.colorButton_0_70.setToolTipDuration(2500)
        self.colorButton_0_70.setAutoFillBackground(False)
        self.colorButton_0_70.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_70.setText("")
        self.colorButton_0_70.setCheckable(True)
        self.colorButton_0_70.setChecked(False)
        self.colorButton_0_70.setObjectName("colorButton_0_70")
        self.colorButton_0_71 = QtWidgets.QPushButton(self.GameOfLife)
        self.colorButton_0_71.setGeometry(QtCore.QRect(1025, 690, 41, 16))
        self.colorButton_0_71.setMouseTracking(True)
        self.colorButton_0_71.setToolTipDuration(2500)
        self.colorButton_0_71.setAutoFillBackground(False)
        self.colorButton_0_71.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_71.setText("")
        self.colorButton_0_71.setCheckable(True)
        self.colorButton_0_71.setChecked(False)
        self.colorButton_0_71.setObjectName("colorButton_0_71")
        self.label_17 = QtWidgets.QLabel(self.GameOfLife)
        self.label_17.setEnabled(False)
        self.label_17.setGeometry(QtCore.QRect(610, 620, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
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
        self.label_2 = QtWidgets.QLabel(self.NoisePerlin)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setObjectName("label_2")
        self.b_processImageNP = QtWidgets.QPushButton(self.NoisePerlin)
        self.b_processImageNP.setGeometry(QtCore.QRect(706, 790, 171, 41))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.NoisePerlin)
        self.pushButton_4.setGeometry(QtCore.QRect(425, 681, 241, 91))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.NoisePerlin)
        self.pushButton_5.setGeometry(QtCore.QRect(676, 681, 241, 91))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.NoisePerlin)
        self.pushButton_6.setGeometry(QtCore.QRect(927, 681, 241, 91))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_16 = QtWidgets.QLabel(self.NoisePerlin)
        self.label_16.setEnabled(False)
        self.label_16.setGeometry(QtCore.QRect(610, 620, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-weight:bold;\n"
"border:none;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.colorButton_0_63 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_63.setGeometry(QtCore.QRect(525, 690, 42, 16))
        self.colorButton_0_63.setMouseTracking(True)
        self.colorButton_0_63.setToolTipDuration(2500)
        self.colorButton_0_63.setAutoFillBackground(False)
        self.colorButton_0_63.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_63.setText("")
        self.colorButton_0_63.setCheckable(True)
        self.colorButton_0_63.setChecked(False)
        self.colorButton_0_63.setObjectName("colorButton_0_63")
        self.colorButton_0_64 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_64.setGeometry(QtCore.QRect(571, 690, 41, 16))
        self.colorButton_0_64.setMouseTracking(True)
        self.colorButton_0_64.setToolTipDuration(2500)
        self.colorButton_0_64.setAutoFillBackground(False)
        self.colorButton_0_64.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_64.setText("")
        self.colorButton_0_64.setCheckable(True)
        self.colorButton_0_64.setChecked(False)
        self.colorButton_0_64.setObjectName("colorButton_0_64")
        self.colorButton_0_65 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_65.setGeometry(QtCore.QRect(480, 690, 41, 16))
        self.colorButton_0_65.setMouseTracking(True)
        self.colorButton_0_65.setToolTipDuration(2500)
        self.colorButton_0_65.setAutoFillBackground(False)
        self.colorButton_0_65.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_65.setText("")
        self.colorButton_0_65.setCheckable(True)
        self.colorButton_0_65.setChecked(False)
        self.colorButton_0_65.setObjectName("colorButton_0_65")
        self.colorButton_3_63 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_3_63.setGeometry(QtCore.QRect(775, 690, 41, 16))
        self.colorButton_3_63.setMouseTracking(True)
        self.colorButton_3_63.setToolTipDuration(2500)
        self.colorButton_3_63.setAutoFillBackground(False)
        self.colorButton_3_63.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_63.setText("")
        self.colorButton_3_63.setCheckable(True)
        self.colorButton_3_63.setChecked(False)
        self.colorButton_3_63.setObjectName("colorButton_3_63")
        self.colorButton_3_64 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_3_64.setGeometry(QtCore.QRect(820, 690, 42, 16))
        self.colorButton_3_64.setMouseTracking(True)
        self.colorButton_3_64.setToolTipDuration(2500)
        self.colorButton_3_64.setAutoFillBackground(False)
        self.colorButton_3_64.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_64.setText("")
        self.colorButton_3_64.setCheckable(True)
        self.colorButton_3_64.setChecked(False)
        self.colorButton_3_64.setObjectName("colorButton_3_64")
        self.colorButton_3_65 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_3_65.setGeometry(QtCore.QRect(730, 690, 41, 16))
        self.colorButton_3_65.setMouseTracking(True)
        self.colorButton_3_65.setToolTipDuration(2500)
        self.colorButton_3_65.setAutoFillBackground(False)
        self.colorButton_3_65.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_65.setText("")
        self.colorButton_3_65.setCheckable(True)
        self.colorButton_3_65.setChecked(False)
        self.colorButton_3_65.setObjectName("colorButton_3_65")
        self.colorButton_0_57 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_57.setGeometry(QtCore.QRect(1025, 690, 41, 16))
        self.colorButton_0_57.setMouseTracking(True)
        self.colorButton_0_57.setToolTipDuration(2500)
        self.colorButton_0_57.setAutoFillBackground(False)
        self.colorButton_0_57.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_57.setText("")
        self.colorButton_0_57.setCheckable(True)
        self.colorButton_0_57.setChecked(False)
        self.colorButton_0_57.setObjectName("colorButton_0_57")
        self.colorButton_0_58 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_58.setGeometry(QtCore.QRect(1070, 690, 42, 16))
        self.colorButton_0_58.setMouseTracking(True)
        self.colorButton_0_58.setToolTipDuration(2500)
        self.colorButton_0_58.setAutoFillBackground(False)
        self.colorButton_0_58.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_58.setText("")
        self.colorButton_0_58.setCheckable(True)
        self.colorButton_0_58.setChecked(False)
        self.colorButton_0_58.setObjectName("colorButton_0_58")
        self.colorButton_0_59 = QtWidgets.QPushButton(self.NoisePerlin)
        self.colorButton_0_59.setGeometry(QtCore.QRect(980, 690, 41, 16))
        self.colorButton_0_59.setMouseTracking(True)
        self.colorButton_0_59.setToolTipDuration(2500)
        self.colorButton_0_59.setAutoFillBackground(False)
        self.colorButton_0_59.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_59.setText("")
        self.colorButton_0_59.setCheckable(True)
        self.colorButton_0_59.setChecked(False)
        self.colorButton_0_59.setObjectName("colorButton_0_59")
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
        self.label_3 = QtWidgets.QLabel(self.KrivaKoxa)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.colorButton_0_56 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_56.setGeometry(QtCore.QRect(1070, 690, 42, 16))
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
        self.colorButton_0_55 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_55.setGeometry(QtCore.QRect(1025, 690, 41, 16))
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
        self.colorButton_0_54 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_54.setGeometry(QtCore.QRect(980, 690, 41, 16))
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
        self.colorButton_3_62 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_3_62.setGeometry(QtCore.QRect(820, 690, 42, 16))
        self.colorButton_3_62.setMouseTracking(True)
        self.colorButton_3_62.setToolTipDuration(2500)
        self.colorButton_3_62.setAutoFillBackground(False)
        self.colorButton_3_62.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_62.setText("")
        self.colorButton_3_62.setCheckable(True)
        self.colorButton_3_62.setChecked(False)
        self.colorButton_3_62.setObjectName("colorButton_3_62")
        self.colorButton_3_60 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_3_60.setGeometry(QtCore.QRect(775, 690, 41, 16))
        self.colorButton_3_60.setMouseTracking(True)
        self.colorButton_3_60.setToolTipDuration(2500)
        self.colorButton_3_60.setAutoFillBackground(False)
        self.colorButton_3_60.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_60.setText("")
        self.colorButton_3_60.setCheckable(True)
        self.colorButton_3_60.setChecked(False)
        self.colorButton_3_60.setObjectName("colorButton_3_60")
        self.colorButton_3_61 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_3_61.setGeometry(QtCore.QRect(730, 690, 41, 16))
        self.colorButton_3_61.setMouseTracking(True)
        self.colorButton_3_61.setToolTipDuration(2500)
        self.colorButton_3_61.setAutoFillBackground(False)
        self.colorButton_3_61.setStyleSheet("QPushButton {\n"
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
        self.colorButton_3_61.setText("")
        self.colorButton_3_61.setCheckable(True)
        self.colorButton_3_61.setChecked(False)
        self.colorButton_3_61.setObjectName("colorButton_3_61")
        self.b_processImageKrivaKoxa = QtWidgets.QPushButton(self.KrivaKoxa)
        self.b_processImageKrivaKoxa.setGeometry(QtCore.QRect(706, 790, 171, 41))
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
        self.label_15 = QtWidgets.QLabel(self.KrivaKoxa)
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QtCore.QRect(610, 620, 361, 20))
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
        self.pushButton = QtWidgets.QPushButton(self.KrivaKoxa)
        self.pushButton.setGeometry(QtCore.QRect(425, 681, 241, 91))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.colorButton_0_61 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_61.setGeometry(QtCore.QRect(571, 690, 41, 16))
        self.colorButton_0_61.setMouseTracking(True)
        self.colorButton_0_61.setToolTipDuration(2500)
        self.colorButton_0_61.setAutoFillBackground(False)
        self.colorButton_0_61.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_61.setText("")
        self.colorButton_0_61.setCheckable(True)
        self.colorButton_0_61.setChecked(False)
        self.colorButton_0_61.setObjectName("colorButton_0_61")
        self.colorButton_0_62 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_62.setGeometry(QtCore.QRect(525, 690, 42, 16))
        self.colorButton_0_62.setMouseTracking(True)
        self.colorButton_0_62.setToolTipDuration(2500)
        self.colorButton_0_62.setAutoFillBackground(False)
        self.colorButton_0_62.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_62.setText("")
        self.colorButton_0_62.setCheckable(True)
        self.colorButton_0_62.setChecked(False)
        self.colorButton_0_62.setObjectName("colorButton_0_62")
        self.colorButton_0_60 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.colorButton_0_60.setGeometry(QtCore.QRect(480, 690, 41, 16))
        self.colorButton_0_60.setMouseTracking(True)
        self.colorButton_0_60.setToolTipDuration(2500)
        self.colorButton_0_60.setAutoFillBackground(False)
        self.colorButton_0_60.setStyleSheet("QPushButton {\n"
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
        self.colorButton_0_60.setText("")
        self.colorButton_0_60.setCheckable(True)
        self.colorButton_0_60.setChecked(False)
        self.colorButton_0_60.setObjectName("colorButton_0_60")
        self.pushButton_2 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.pushButton_2.setGeometry(QtCore.QRect(676, 681, 241, 91))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.KrivaKoxa)
        self.pushButton_3.setGeometry(QtCore.QRect(927, 681, 241, 91))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"    stop:0 rgba(70, 35, 105, 200),\n"
"    stop:0.427447 rgba(60, 75, 135, 200),\n"
"    stop:1 rgba(120, 75, 135, 220));\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.b_deleteProcImage2.raise_()
        self.l_OrigImage_pg2.raise_()
        self.l_ProcImage_pg2.raise_()
        self.b_deleteOrigImage2.raise_()
        self.b_SaveProcImage2.raise_()
        self.b_AddOrigImage2.raise_()
        self.label_3.raise_()
        self.colorButton_0_56.raise_()
        self.colorButton_0_55.raise_()
        self.colorButton_0_54.raise_()
        self.colorButton_3_62.raise_()
        self.colorButton_3_60.raise_()
        self.colorButton_3_61.raise_()
        self.b_processImageKrivaKoxa.raise_()
        self.label_15.raise_()
        self.pushButton.raise_()
        self.colorButton_0_61.raise_()
        self.colorButton_0_62.raise_()
        self.colorButton_0_60.raise_()
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
        self.label.setText(_translate("MainMenu", "1"))
        self.b_processImageGOF.setText(_translate("MainMenu", "Обробити фото"))
        self.colorButton_0_66.setToolTip(_translate("MainMenu", "Чорний"))
        self.colorButton_0_67.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_68.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_3_66.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_67.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_68.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.colorButton_0_69.setToolTip(_translate("MainMenu", "Рожевий"))
        self.colorButton_0_70.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_71.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.label_17.setText(_translate("MainMenu", "Кольори"))
        self.b_deleteOrigImage1.setText(_translate("MainMenu", "X"))
        self.b_AddOrigImage1.setText(_translate("MainMenu", "+"))
        self.b_deleteProcImage1.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImage1.setText(_translate("MainMenu", "+"))
        self.label_2.setText(_translate("MainMenu", "2"))
        self.b_processImageNP.setText(_translate("MainMenu", "Обробити фото"))
        self.label_16.setText(_translate("MainMenu", "Кольори"))
        self.colorButton_0_63.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_0_64.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_65.setToolTip(_translate("MainMenu", "Чорний"))
        self.colorButton_3_63.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_64.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_65.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.colorButton_0_57.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.colorButton_0_58.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_59.setToolTip(_translate("MainMenu", "Рожевий"))
        self.b_deleteProcImage2.setText(_translate("MainMenu", "X"))
        self.b_deleteOrigImage2.setText(_translate("MainMenu", "X"))
        self.b_SaveProcImage2.setText(_translate("MainMenu", "+"))
        self.b_AddOrigImage2.setText(_translate("MainMenu", "+"))
        self.label_3.setText(_translate("MainMenu", "3"))
        self.colorButton_0_56.setToolTip(_translate("MainMenu", "Світло-зелений"))
        self.colorButton_0_55.setToolTip(_translate("MainMenu", "Аквамарин"))
        self.colorButton_0_54.setToolTip(_translate("MainMenu", "Рожевий"))
        self.colorButton_3_62.setToolTip(_translate("MainMenu", "Темно-рожевий"))
        self.colorButton_3_60.setToolTip(_translate("MainMenu", "Індиго"))
        self.colorButton_3_61.setToolTip(_translate("MainMenu", "Сапфіровий"))
        self.b_processImageKrivaKoxa.setText(_translate("MainMenu", "Обробити фото"))
        self.label_15.setText(_translate("MainMenu", "Кольори"))
        self.colorButton_0_61.setToolTip(_translate("MainMenu", "Темно-пурпурний"))
        self.colorButton_0_62.setToolTip(_translate("MainMenu", "Вугільний"))
        self.colorButton_0_60.setToolTip(_translate("MainMenu", "Чорний"))
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
