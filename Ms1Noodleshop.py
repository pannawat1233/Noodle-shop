from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 1077)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 921, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.label_29.setObjectName("label_29")
        self.Accapt = QtWidgets.QPushButton(self.centralwidget)
        self.Accapt.setGeometry(QtCore.QRect(540, 650, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Accapt.setFont(font)
        self.Accapt.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.Accapt.setObjectName("Accapt")
        self.money1 = QtWidgets.QLabel(self.centralwidget)
        self.money1.setGeometry(QtCore.QRect(70, 720, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.money1.setFont(font)
        self.money1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.money1.setObjectName("money1")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(540, 720, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Clear.setObjectName("Clear")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 751, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TgAT3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT3.setFont(font)
        self.TgAT3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT3.setObjectName("TgAT3")
        self.gridLayout.addWidget(self.TgAT3, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color: rgb(255, 248, 29);")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 14, 1)
        self.TgAT10 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT10.setFont(font)
        self.TgAT10.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT10.setObjectName("TgAT10")
        self.gridLayout.addWidget(self.TgAT10, 9, 1, 1, 1)
        self.G11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G11.setFont(font)
        self.G11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G11.setObjectName("G11")
        self.gridLayout.addWidget(self.G11, 10, 2, 1, 2)
        self.TgAT11 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT11.setFont(font)
        self.TgAT11.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT11.setObjectName("TgAT11")
        self.gridLayout.addWidget(self.TgAT11, 10, 1, 1, 1)
        self.G10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G10.setFont(font)
        self.G10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G10.setObjectName("G10")
        self.gridLayout.addWidget(self.G10, 9, 2, 1, 2)
        self.TgAT7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT7.setFont(font)
        self.TgAT7.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT7.setObjectName("TgAT7")
        self.gridLayout.addWidget(self.TgAT7, 6, 1, 1, 1)
        self.G7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G7.setFont(font)
        self.G7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G7.setObjectName("G7")
        self.gridLayout.addWidget(self.G7, 6, 2, 1, 2)
        self.TgAT6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT6.setFont(font)
        self.TgAT6.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT6.setObjectName("TgAT6")
        self.gridLayout.addWidget(self.TgAT6, 5, 1, 1, 1)
        self.TgAT8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT8.setFont(font)
        self.TgAT8.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT8.setObjectName("TgAT8")
        self.gridLayout.addWidget(self.TgAT8, 7, 1, 1, 1)
        self.G8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G8.setFont(font)
        self.G8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G8.setObjectName("G8")
        self.gridLayout.addWidget(self.G8, 7, 2, 1, 2)
        self.G6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G6.setFont(font)
        self.G6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G6.setObjectName("G6")
        self.gridLayout.addWidget(self.G6, 5, 2, 1, 2)
        self.G5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G5.setFont(font)
        self.G5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G5.setObjectName("G5")
        self.gridLayout.addWidget(self.G5, 4, 2, 1, 2)
        self.G9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G9.setFont(font)
        self.G9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G9.setObjectName("G9")
        self.gridLayout.addWidget(self.G9, 8, 2, 1, 2)
        self.TgAT9 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT9.setFont(font)
        self.TgAT9.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT9.setObjectName("TgAT9")
        self.gridLayout.addWidget(self.TgAT9, 8, 1, 1, 1)
        self.TgAT4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT4.setFont(font)
        self.TgAT4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT4.setObjectName("TgAT4")
        self.gridLayout.addWidget(self.TgAT4, 3, 1, 1, 1)
        self.G2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G2.setFont(font)
        self.G2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G2.setObjectName("G2")
        self.gridLayout.addWidget(self.G2, 1, 2, 1, 2)
        self.TgAT5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT5.setFont(font)
        self.TgAT5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT5.setObjectName("TgAT5")
        self.gridLayout.addWidget(self.TgAT5, 4, 1, 1, 1)
        self.G4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G4.setFont(font)
        self.G4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G4.setObjectName("G4")
        self.gridLayout.addWidget(self.G4, 3, 2, 1, 2)
        self.G3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G3.setFont(font)
        self.G3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G3.setObjectName("G3")
        self.gridLayout.addWidget(self.G3, 2, 2, 1, 2)
        self.TgAT12 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT12.setFont(font)
        self.TgAT12.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT12.setObjectName("TgAT12")
        self.gridLayout.addWidget(self.TgAT12, 11, 1, 1, 1)
        self.TgAT1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT1.setFont(font)
        self.TgAT1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT1.setObjectName("TgAT1")
        self.gridLayout.addWidget(self.TgAT1, 0, 1, 1, 1)
        self.G1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G1.setFont(font)
        self.G1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G1.setObjectName("G1")
        self.gridLayout.addWidget(self.G1, 0, 2, 1, 2)
        self.TgAT2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT2.setFont(font)
        self.TgAT2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT2.setObjectName("TgAT2")
        self.gridLayout.addWidget(self.TgAT2, 1, 1, 1, 1)
        self.TgAT14 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgAT14.setFont(font)
        self.TgAT14.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.TgAT14.setObjectName("TgAT14")
        self.gridLayout.addWidget(self.TgAT14, 12, 1, 1, 1)
        self.G12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G12.setFont(font)
        self.G12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G12.setObjectName("G12")
        self.gridLayout.addWidget(self.G12, 11, 2, 1, 2)
        self.G14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.G14.setFont(font)
        self.G14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G14.setObjectName("G14")
        self.gridLayout.addWidget(self.G14, 12, 2, 1, 2)
        self.TgBT2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT2.setFont(font)
        self.TgBT2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT2.setObjectName("TgBT2")
        self.gridLayout.addWidget(self.TgBT2, 1, 4, 1, 1)
        self.TgBT3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT3.setFont(font)
        self.TgBT3.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT3.setObjectName("TgBT3")
        self.gridLayout.addWidget(self.TgBT3, 2, 4, 1, 1)
        self.TgABT1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgABT1.setFont(font)
        self.TgABT1.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgABT1.setObjectName("TgABT1")
       

        self.gridLayout.addWidget(self.TgABT1, 0, 4, 1, 1)
        self.TgBT4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT4.setFont(font)
        self.TgBT4.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT4.setObjectName("TgBT4")
        self.gridLayout.addWidget(self.TgBT4, 3, 4, 1, 1)
        self.TgBT6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT6.setFont(font)
        self.TgBT6.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT6.setObjectName("TgBT6")
        self.gridLayout.addWidget(self.TgBT6, 5, 4, 1, 1)
        self.TgBT8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT8.setFont(font)
        self.TgBT8.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT8.setObjectName("TgBT8")
        self.gridLayout.addWidget(self.TgBT8, 7, 4, 1, 1)
        self.TgBT7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT7.setFont(font)
        self.TgBT7.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT7.setObjectName("TgBT7")
        self.gridLayout.addWidget(self.TgBT7, 6, 4, 1, 1)
        self.TgBT9 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT9.setFont(font)
        self.TgBT9.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT9.setObjectName("TgBT9")
        self.gridLayout.addWidget(self.TgBT9, 8, 4, 1, 1)
        self.TgBT10 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT10.setFont(font)
        self.TgBT10.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT10.setObjectName("TgBT10")
        self.gridLayout.addWidget(self.TgBT10, 9, 4, 1, 1)
        self.TgBT11 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT11.setFont(font)
        self.TgBT11.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT11.setObjectName("TgBT11")
        self.gridLayout.addWidget(self.TgBT11, 10, 4, 1, 1)
        self.TgBT14 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT14.setFont(font)
        self.TgBT14.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT14.setObjectName("TgBT14")
        self.gridLayout.addWidget(self.TgBT14, 12, 4, 1, 1)
        self.TgBT12 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT12.setFont(font)
        self.TgBT12.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT12.setObjectName("TgBT12")
        self.gridLayout.addWidget(self.TgBT12, 11, 4, 1, 1)
        self.TgBT5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TgBT5.setFont(font)
        self.TgBT5.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.TgBT5.setObjectName("TgBT5")
        self.gridLayout.addWidget(self.TgBT5, 4, 4, 1, 1)
        self.money = QtWidgets.QLineEdit(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(70, 650, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.money.setFont(font)
        self.money.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.money.setObjectName("money")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(70, 790, 671, 192))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.TgABT1.clicked.connect(self.Tg1)
        self.TgBT2.clicked.connect(self.Tg2)
        self.TgBT3.clicked.connect(self.Tg3)
        self.TgBT4.clicked.connect(self.Tg4)
        self.TgBT5.clicked.connect(self.Tg5)
        self.TgBT6.clicked.connect(self.Tg6)
        self.TgBT7.clicked.connect(self.Tg7)
        self.TgBT8.clicked.connect(self.Tg8)
        self.TgBT9.clicked.connect(self.Tg9)
        self.TgBT10.clicked.connect(self.Tg10)
        self.TgBT11.clicked.connect(self.Tg11)
        self.TgBT12.clicked.connect(self.Tg12)
        self.TgBT14.clicked.connect(self.Tg14)

        self.TgAT1.clicked.connect(self.dg1)
        self.TgAT2.clicked.connect(self.dg2)
        self.TgAT3.clicked.connect(self.dg3)
        self.TgAT4.clicked.connect(self.dg4)
        self.TgAT5.clicked.connect(self.dg5)
        self.TgAT6.clicked.connect(self.dg6)
        self.TgAT7.clicked.connect(self.dg7)
        self.TgAT8.clicked.connect(self.dg8)
        self.TgAT9.clicked.connect(self.dg9)
        self.TgAT10.clicked.connect(self.dg10)
        self.TgAT11.clicked.connect(self.dg11)
        self.TgAT12.clicked.connect(self.dg12)
        self.TgAT14.clicked.connect(self.dg14)
        self.Clear.clicked.connect(self.dgclear)
        self.Accapt.clicked.connect(self.dgAccapt)
        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_29.setText(_translate("MainWindow", "                           ร้านขายก๋วยเตี๋ยว"))
        self.Accapt.setText(_translate("MainWindow", "ยืนยัน"))
        self.money1.setText(_translate("MainWindow", "           0"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.TgAT3.setText(_translate("MainWindow", "-"))
        self.label_12.setText(_translate("MainWindow", "1 ก๋วยเตี๋ยวเรือ"))
        self.label_13.setText(_translate("MainWindow", "2. ก๋วยเตี๋ยวต้มยำสูตรโบราณ"))
        self.label_14.setText(_translate("MainWindow", "3. ก๋วยเตี๋ยวเย็นตาโฟ"))
        self.label_15.setText(_translate("MainWindow", "4. ก๋วยเตี๋ยวเรือ เนื้อ"))
        self.label_10.setText(_translate("MainWindow", "5. ก๋วยเตี๋ยวต้มยำเนื้อ"))
        self.label_18.setText(_translate("MainWindow", "6. ก๋วยเตี๋ยวไก่"))
        self.label_19.setText(_translate("MainWindow", "7. บะหมี่เกี๊ยว"))
        self.label_24.setText(_translate("MainWindow", "8. เกาเหลาหมู"))
        self.label_23.setText(_translate("MainWindow", "9. เกาเหลาเนื้อ"))
        self.label_26.setText(_translate("MainWindow", "10. บะหมี่เกี๊ยวหมูแดง"))
        self.label_25.setText(_translate("MainWindow", "11. บะหมี่เกี๊ยวหมูกรอบ"))
        self.label_28.setText(_translate("MainWindow", "12. ก๋วยเตี๋ยวเป็ดพะโล้"))
        self.TgAT10.setText(_translate("MainWindow", "-"))
        self.G11.setText(_translate("MainWindow", " 0"))
        self.TgAT11.setText(_translate("MainWindow", "-"))
        self.G10.setText(_translate("MainWindow", " 0"))
        self.TgAT7.setText(_translate("MainWindow", "-"))
        self.G7.setText(_translate("MainWindow", " 0"))
        self.TgAT6.setText(_translate("MainWindow", "-"))
        self.TgAT8.setText(_translate("MainWindow", "-"))
        self.G8.setText(_translate("MainWindow", " 0"))
        self.G6.setText(_translate("MainWindow", " 0"))
        self.G5.setText(_translate("MainWindow", " 0"))
        self.G9.setText(_translate("MainWindow", " 0"))
        self.TgAT9.setText(_translate("MainWindow", "-"))
        self.TgAT4.setText(_translate("MainWindow", "-"))
        self.G2.setText(_translate("MainWindow", " 0"))
        self.TgAT5.setText(_translate("MainWindow", "-"))
        self.G4.setText(_translate("MainWindow", " 0"))
        self.G3.setText(_translate("MainWindow", " 0"))
        self.TgAT12.setText(_translate("MainWindow", "-"))
        self.TgAT1.setText(_translate("MainWindow", "-"))
        self.G1.setText(_translate("MainWindow", " 0"))
        self.TgAT2.setText(_translate("MainWindow", "-"))
        self.TgAT14.setText(_translate("MainWindow", "-"))
        self.G12.setText(_translate("MainWindow", " 0"))
        self.G14.setText(_translate("MainWindow", " 0"))
        self.TgBT2.setText(_translate("MainWindow", "+"))
        self.TgBT3.setText(_translate("MainWindow", "+"))
        self.TgABT1.setText(_translate("MainWindow", "+"))
        self.TgBT4.setText(_translate("MainWindow", "+"))
        self.TgBT6.setText(_translate("MainWindow", "+"))
        self.TgBT8.setText(_translate("MainWindow", "+"))
        self.TgBT7.setText(_translate("MainWindow", "+"))
        self.TgBT9.setText(_translate("MainWindow", "+"))
        self.TgBT10.setText(_translate("MainWindow", "+"))
        self.TgBT11.setText(_translate("MainWindow", "+"))
        self.TgBT14.setText(_translate("MainWindow", "+"))
        self.TgBT12.setText(_translate("MainWindow", "+"))
        self.TgBT5.setText(_translate("MainWindow", "+"))

        

        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
        self.a6 = 0
        self.a7 = 0
        self.a8 = 0
        self.a9 = 0
        self.a10 = 0
        self.a11 = 0
        self.a12 = 0
        self.a14 = 0

        self.b1 = 0
        self.b2 = 0
        self.b3 = 0
        self.BM = 0


        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0
        self.c6 = 0
        self.c7 = 0
        self.c8 = 0
        self.c9 = 0
        self.c11 = 0
        self.c12 = 0
        self.c13 = 0

        self.i =1



    
    numberStar = []
    numberStarfood = []

    def dgclear(self):
        self.b1 = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
        self.a6 = 0
        self.a7 = 0
        self.a8 = 0
        self.a9 = 0
        self.a10 = 0
        self.a11 = 0
        self.a12 = 0
        self.a14 = 0

        self.money1.setText(str(self.b1))
        self.money.setText(str())
        self.G1.setText(str(self.b1))
        self.G2.setText(str(self.b1))
        self.G3.setText(str(self.b1))
        self.G4.setText(str(self.b1))
        self.G5.setText(str(self.b1)) 
        self.G6.setText(str(self.b1))
        self.G7.setText(str(self.b1))
        self.G8.setText(str(self.b1))
        self.G9.setText(str(self.b1))
        self.G10.setText(str(self.b1))
        self.G11.setText(str(self.b1))
        self.G12.setText(str(self.b1))
        self.G14.setText(str(self.b1))
        self.listWidget.clear()
        self.numberStar.clear()
        return self.b1
    
    def Tg1(self):
        
        self.numberStar.append("ก๋วยเตี๋ยวเรือ")
        self.a1+= 1
        self.G1.setText(str(self.a1))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg2(self):
       
        self.numberStar.append("ก๋วยเตี๋ยวต้มยำสูตรโบราณ")
        self.a2+= 1
        self.G2.setText(str(self.a2))
        self.b1 +=45
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg3(self):
       
        self.numberStar.append("ก๋วยเตี๋ยวเย็นตาโฟ")
        self.a3+= 1
        self.G3.setText(str(self.a3))
        self.b1 += 40
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg4(self):
       
        self.numberStar.append("ก๋วยเตี๋ยวเรือ เนื้อ")
        self.a4+= 1
        self.G4.setText(str(self.a4))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg5(self):
        
        self.numberStar.append("ก๋วยเตี๋ยวต้มยำเนื้อ")
        self.a5+= 1
        self.G5.setText(str(self.a5))
        self.b1 += 55
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg6(self):
        
        self.numberStar.append("ก๋วยเตี๋ยวไก่")
        self.a6+= 1
        self.G6.setText(str(self.a6))
        self.b1 +=50
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg7(self):
        
        self.numberStar.append("บะหมี่เกี๊ยว")
        self.a7+= 1
        self.G7.setText(str(self.a7))
        self.b1 += 45
        self.money1.setText(str(self.b1))
        return self.b1

    def Tg8(self):
        
        self.numberStar.append("เกาเหลาหมู")
        self.a8+= 1
        self.G8.setText(str(self.a8))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1


    def Tg9(self):
       
        self.numberStar.append("เกาเหลาเนื้อ")
        self.a9+= 1
        self.G9.setText(str(self.a9))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1


    def Tg10(self):
       
        self.numberStar.append("บะหมี่เกี๊ยวหมูแดง")
        self.a10+= 1
        self.G10.setText(str(self.a10))
        self.b1 +=50
        self.money1.setText(str(self.b1))
        return self.b1


    def Tg11(self):
       
        self.numberStar.append("บะหมี่เกี๊ยวหมูกรอบ")
        self.a11+= 1
        self.G11.setText(str(self.a11))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1


    def Tg12(self):
        
        self.numberStar.append("บะหมี่เกี๊ยว")
        self.a12+= 1
        self.G12.setText(str(self.a12))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1


    def Tg14(self):
        
        self.numberStar.append("ก๋วยเตี๋ยวเป็ดพะโล้")
        self.a14+= 1
        self.G14.setText(str(self.a14))
        self.b1 += 50
        self.money1.setText(str(self.b1))
        return self.b1



    def dg1(self):
        if self.a1 > 0:
            self.numberStar.append(self.a1)
            self.a1= self.a1 - self.i
            self.G1.setText(str(self.a1))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg2(self):
        if self.a2 > 0:
            self.numberStar.append(self.a2)
            self.a2= self.a2 - self.i
            self.G2.setText(str(self.a2))
            self.b1 -=45
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg3(self):
        if self.a3 > 0:
            self.numberStar.append(self.a3)
            self.a3= self.a3 - self.i
            self.G3.setText(str(self.a3))
            self.b1 -=40
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()
    def dg4(self):
        if self.a4 > 0:
            self.numberStar.append(self.a4)
            self.a4= self.a4 - self.i
            self.G4.setText(str(self.a4))            
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg5(self):
        if self.a5 > 0:
            self.numberStar.append(self.a5)
            self.a5= self.a5 - self.i
            self.G5.setText(str(self.a5))
            self.b1 -=55
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg6(self):
        if self.a6 > 0:
            self.numberStar.append(self.a6)
            self.a6= self.a6 - self.i
            self.G6.setText(str(self.a6))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg7(self):
        if self.a7 > 0:
            self.numberStar.append(self.a7)
            self.a7= self.a7 - self.i
            self.G7.setText(str(self.a7))
            self.b1 -=45
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg8(self):
        if self.a8 > 0:
            self.numberStar.append(self.a8)
            self.a8= self.a8 - self.i
            self.G8.setText(str(self.a8))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg9(self):
        if self.a9 > 0:
            self.numberStar.append(self.a9)
            self.a9= self.a9 - self.i
            self.G9.setText(str(self.a9))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg10(self):
        if self.a10 > 0:
            self.numberStar.append(self.a10)
            self.a10= self.a10 - self.i
            self.G10.setText(str(self.a10))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def dg11(self):
        if self.a11 > 0:
            self.numberStar.append(self.a11)
            self.a11= self.a11 - self.i
            self.G11.setText(str(self.a11))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg12(self):
        if self.a12 > 0:
            self.numberStar.append(self.a12)
            self.a12= self.a12 - self.i
            self.G12.setText(str(self.a12))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()

    def dg14(self):
        if self.a14 > 0:
            self.numberStar.append(self.a14)
            self.a14= self.a14 - self.i
            self.G14.setText(str(self.a14))
            self.b1 -=50
            self.money1.setText(str(self.b1))
            return self.b1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ไม่สามารภลบคำขอได้อีก")
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def dgAccapt(self):
        try:
            money = int(self.money.text())
            p1 = money-self.b1
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("เงินทอน"+str(p1)+"บาท")
            msg.setWindowTitle("money")
            uniqe_numberStar = list (set(self.numberStar))
            numberStar_text = "\n".join(map(str, uniqe_numberStar))
            self.listWidget.addItem(str(numberStar_text))
            self.b1 = 0
            self.a1 = 0
            self.a2 = 0
            self.a3 = 0
            self.a4 = 0
            self.a5 = 0
            self.a6 = 0
            self.a7 = 0
            self.a8 = 0
            self.a9 = 0
            self.a10 = 0
            self.a11 = 0
            self.a12 = 0
            self.a14 = 0

            self.money1.setText(str(self.b1))
            self.money.setText(str())
            self.G1.setText(str(self.b1))
            self.G2.setText(str(self.b1))
            self.G3.setText(str(self.b1))
            self.G4.setText(str(self.b1))
            self.G5.setText(str(self.b1)) 
            self.G6.setText(str(self.b1))
            self.G7.setText(str(self.b1))
            self.G8.setText(str(self.b1))
            self.G9.setText(str(self.b1))
            self.G10.setText(str(self.b1))
            self.G11.setText(str(self.b1))
            self.G12.setText(str(self.b1))
            self.G14.setText(str(self.b1))

            msg.exec_()
            
           
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("กรุณาใส่ตัวเลข")
            msg.setWindowTitle("Error")
            msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())