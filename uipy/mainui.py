# # -*- coding: utf-8 -*-
#
# ################################################################################
# ## Form generated from reading UI file 'mainkBvBWA.ui'
# ##
# ## Created by: Qt User Interface Compiler version 6.10.0
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################
#
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
#     QLabel, QLineEdit, QMainWindow, QPushButton,
#     QSizePolicy, QStackedWidget, QStatusBar, QTableWidget,
#     QTableWidgetItem, QVBoxLayout, QWidget)
# #import icons_rc
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(884, 602)
#         icon = QIcon()
#         icon.addFile(u":/logo/Atoplogo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
#         MainWindow.setWindowIcon(icon)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.topGroup = QGroupBox(self.centralwidget)
#         self.topGroup.setObjectName(u"topGroup")
#         self.topGroup.setGeometry(QRect(10, 0, 871, 81))
#         self.topLogo = QLabel(self.topGroup)
#         self.topLogo.setObjectName(u"topLogo")
#         self.topLogo.setGeometry(QRect(0, 0, 81, 71))
#         self.topLogo.setPixmap(QPixmap(u":/logo/Alogo.jpg"))
#         self.topLogo.setScaledContents(True)
#         self.topName = QLabel(self.topGroup)
#         self.topName.setObjectName(u"topName")
#         self.topName.setGeometry(QRect(280, 10, 341, 61))
#         font = QFont()
#         font.setPointSize(25)
#         self.topName.setFont(font)
#         self.topName.setTextFormat(Qt.TextFormat.AutoText)
#         self.leftGroup = QGroupBox(self.centralwidget)
#         self.leftGroup.setObjectName(u"leftGroup")
#         self.leftGroup.setGeometry(QRect(0, 80, 161, 431))
#         self.verticalLayout = QVBoxLayout(self.leftGroup)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.industrialC = QPushButton(self.leftGroup)
#         self.industrialC.setObjectName(u"industrialC")
#         font1 = QFont()
#         font1.setPointSize(15)
#         font1.setBold(False)
#         self.industrialC.setFont(font1)
#
#         self.verticalLayout.addWidget(self.industrialC)
#
#         self.hyperspectralC = QPushButton(self.leftGroup)
#         self.hyperspectralC.setObjectName(u"hyperspectralC")
#         self.hyperspectralC.setFont(font1)
#
#         self.verticalLayout.addWidget(self.hyperspectralC)
#
#         self.connect = QPushButton(self.leftGroup)
#         self.connect.setObjectName(u"connect")
#         self.connect.setFont(font1)
#
#         self.verticalLayout.addWidget(self.connect)
#
#         self.yoloDetection = QPushButton(self.leftGroup)
#         self.yoloDetection.setObjectName(u"yoloDetection")
#         self.yoloDetection.setFont(font1)
#
#         self.verticalLayout.addWidget(self.yoloDetection)
#
#         self.F2 = QPushButton(self.leftGroup)
#         self.F2.setObjectName(u"F2")
#         self.F2.setFont(font1)
#
#         self.verticalLayout.addWidget(self.F2)
#
#         self.F3 = QPushButton(self.leftGroup)
#         self.F3.setObjectName(u"F3")
#         self.F3.setFont(font1)
#
#         self.verticalLayout.addWidget(self.F3)
#
#         self.rightGroup = QGroupBox(self.centralwidget)
#         self.rightGroup.setObjectName(u"rightGroup")
#         self.rightGroup.setGeometry(QRect(160, 80, 721, 431))
#         self.stackedWidget = QStackedWidget(self.rightGroup)
#         self.stackedWidget.setObjectName(u"stackedWidget")
#         self.stackedWidget.setGeometry(QRect(0, 10, 711, 421))
#         self.initialPage = QWidget()
#         self.initialPage.setObjectName(u"initialPage")
#         self.stackedWidget.addWidget(self.initialPage)
#         self.connectPage = QWidget()
#         self.connectPage.setObjectName(u"connectPage")
#         self.IndPara = QGroupBox(self.connectPage)
#         self.IndPara.setObjectName(u"IndPara")
#         self.IndPara.setGeometry(QRect(0, 0, 351, 221))
#         self.verticalLayout_2 = QVBoxLayout(self.IndPara)
#         self.verticalLayout_2.setObjectName(u"verticalLayout_2")
#         self.horizontalLayout = QHBoxLayout()
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.label_2 = QLabel(self.IndPara)
#         self.label_2.setObjectName(u"label_2")
#
#         self.horizontalLayout.addWidget(self.label_2)
#
#         self.IndIP = QLineEdit(self.IndPara)
#         self.IndIP.setObjectName(u"IndIP")
#
#         self.horizontalLayout.addWidget(self.IndIP)
#
#
#         self.verticalLayout_2.addLayout(self.horizontalLayout)
#
#         self.horizontalLayout_2 = QHBoxLayout()
#         self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
#         self.label_5 = QLabel(self.IndPara)
#         self.label_5.setObjectName(u"label_5")
#
#         self.horizontalLayout_2.addWidget(self.label_5)
#
#         self.IndPort = QLineEdit(self.IndPara)
#         self.IndPort.setObjectName(u"IndPort")
#
#         self.horizontalLayout_2.addWidget(self.IndPort)
#
#
#         self.verticalLayout_2.addLayout(self.horizontalLayout_2)
#
#         self.horizontalLayout_3 = QHBoxLayout()
#         self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
#         self.led1 = QLabel(self.IndPara)
#         self.led1.setObjectName(u"led1")
#
#         self.horizontalLayout_3.addWidget(self.led1)
#
#         self.InfoCon1 = QLabel(self.IndPara)
#         self.InfoCon1.setObjectName(u"InfoCon1")
#
#         self.horizontalLayout_3.addWidget(self.InfoCon1)
#
#         self.IndCon = QPushButton(self.IndPara)
#         self.IndCon.setObjectName(u"IndCon")
#
#         self.horizontalLayout_3.addWidget(self.IndCon)
#
#
#         self.verticalLayout_2.addLayout(self.horizontalLayout_3)
#
#         self.PLCPara = QGroupBox(self.connectPage)
#         self.PLCPara.setObjectName(u"PLCPara")
#         self.PLCPara.setGeometry(QRect(360, 0, 351, 221))
#         self.verticalLayout_3 = QVBoxLayout(self.PLCPara)
#         self.verticalLayout_3.setObjectName(u"verticalLayout_3")
#         self.horizontalLayout_4 = QHBoxLayout()
#         self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
#         self.label_3 = QLabel(self.PLCPara)
#         self.label_3.setObjectName(u"label_3")
#
#         self.horizontalLayout_4.addWidget(self.label_3)
#
#         self.PLCIP = QLineEdit(self.PLCPara)
#         self.PLCIP.setObjectName(u"PLCIP")
#
#         self.horizontalLayout_4.addWidget(self.PLCIP)
#
#
#         self.verticalLayout_3.addLayout(self.horizontalLayout_4)
#
#         self.horizontalLayout_5 = QHBoxLayout()
#         self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
#         self.label_6 = QLabel(self.PLCPara)
#         self.label_6.setObjectName(u"label_6")
#
#         self.horizontalLayout_5.addWidget(self.label_6)
#
#         self.PLCPort = QLineEdit(self.PLCPara)
#         self.PLCPort.setObjectName(u"PLCPort")
#
#         self.horizontalLayout_5.addWidget(self.PLCPort)
#
#
#         self.verticalLayout_3.addLayout(self.horizontalLayout_5)
#
#         self.horizontalLayout_6 = QHBoxLayout()
#         self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
#         self.led2 = QLabel(self.PLCPara)
#         self.led2.setObjectName(u"led2")
#
#         self.horizontalLayout_6.addWidget(self.led2)
#
#         self.PLCCon = QLabel(self.PLCPara)
#         self.PLCCon.setObjectName(u"PLCCon")
#
#         self.horizontalLayout_6.addWidget(self.PLCCon)
#
#         self.InfoCon2 = QPushButton(self.PLCPara)
#         self.InfoCon2.setObjectName(u"InfoCon2")
#
#         self.horizontalLayout_6.addWidget(self.InfoCon2)
#
#
#         self.verticalLayout_3.addLayout(self.horizontalLayout_6)
#
#         self.monitorPara = QGroupBox(self.connectPage)
#         self.monitorPara.setObjectName(u"monitorPara")
#         self.monitorPara.setGeometry(QRect(0, 220, 721, 201))
#         self.tableWidget = QTableWidget(self.monitorPara)
#         if (self.tableWidget.columnCount() < 5):
#             self.tableWidget.setColumnCount(5)
#         __qtablewidgetitem = QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
#         __qtablewidgetitem1 = QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
#         __qtablewidgetitem2 = QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
#         __qtablewidgetitem3 = QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
#         __qtablewidgetitem4 = QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
#         if (self.tableWidget.rowCount() < 5):
#             self.tableWidget.setRowCount(5)
#         __qtablewidgetitem5 = QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
#         __qtablewidgetitem6 = QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
#         __qtablewidgetitem7 = QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
#         __qtablewidgetitem8 = QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
#         __qtablewidgetitem9 = QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
#         self.tableWidget.setObjectName(u"tableWidget")
#         self.tableWidget.setGeometry(QRect(10, 20, 681, 191))
#         self.tableWidget.horizontalHeader().setVisible(True)
#         self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
#         self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
#         self.tableWidget.verticalHeader().setVisible(True)
#         self.stackedWidget.addWidget(self.connectPage)
#         self.yoloPage = QWidget()
#         self.yoloPage.setObjectName(u"yoloPage")
#         self.label = QLabel(self.yoloPage)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(10, 30, 361, 331))
#         self.layoutWidget = QWidget(self.yoloPage)
#         self.layoutWidget.setObjectName(u"layoutWidget")
#         self.layoutWidget.setGeometry(QRect(10, 370, 681, 26))
#         self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
#         self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
#         self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
#         self.yoloEdit = QLineEdit(self.layoutWidget)
#         self.yoloEdit.setObjectName(u"yoloEdit")
#
#         self.horizontalLayout_7.addWidget(self.yoloEdit)
#
#         self.pushButton = QPushButton(self.layoutWidget)
#         self.pushButton.setObjectName(u"pushButton")
#
#         self.horizontalLayout_7.addWidget(self.pushButton)
#
#         self.stackedWidget.addWidget(self.yoloPage)
#         self.bottomGroup = QGroupBox(self.centralwidget)
#         self.bottomGroup.setObjectName(u"bottomGroup")
#         self.bottomGroup.setGeometry(QRect(0, 510, 881, 71))
#         self.home = QLabel(self.bottomGroup)
#         self.home.setObjectName(u"home")
#         self.home.setGeometry(QRect(10, 10, 61, 61))
#         self.home.setPixmap(QPixmap(u":/icon/home.png"))
#         self.home.setScaledContents(True)
#         self.home.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.Start = QPushButton(self.bottomGroup)
#         self.Start.setObjectName(u"Start")
#         self.Start.setGeometry(QRect(80, 10, 75, 61))
#         self.Stop = QPushButton(self.bottomGroup)
#         self.Stop.setObjectName(u"Stop")
#         self.Stop.setGeometry(QRect(280, 10, 75, 61))
#         self.Pause = QPushButton(self.bottomGroup)
#         self.Pause.setObjectName(u"Pause")
#         self.Pause.setGeometry(QRect(450, 10, 75, 61))
#         self.Reset = QPushButton(self.bottomGroup)
#         self.Reset.setObjectName(u"Reset")
#         self.Reset.setGeometry(QRect(630, 10, 75, 61))
#         self.startLed = QLabel(self.bottomGroup)
#         self.startLed.setObjectName(u"startLed")
#         self.startLed.setGeometry(QRect(180, 15, 71, 51))
#         self.stopLed = QLabel(self.bottomGroup)
#         self.stopLed.setObjectName(u"stopLed")
#         self.stopLed.setGeometry(QRect(370, 10, 71, 51))
#         self.pauseLed = QLabel(self.bottomGroup)
#         self.pauseLed.setObjectName(u"pauseLed")
#         self.pauseLed.setGeometry(QRect(540, 10, 71, 51))
#         self.resetLed = QLabel(self.bottomGroup)
#         self.resetLed.setObjectName(u"resetLed")
#         self.resetLed.setGeometry(QRect(720, 10, 81, 51))
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#
#         self.stackedWidget.setCurrentIndex(2)
#
#
#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi
#
#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7389\u7c73\u79cd\u5b50\u6d3b\u529b\u68c0\u6d4b\u7cfb\u7edf", None))
#         self.topGroup.setTitle("")
#         self.topLogo.setText("")
#         self.topName.setText(QCoreApplication.translate("MainWindow", u"\u7389\u7c73\u79cd\u5b50\u6d3b\u529b\u68c0\u6d4b\u7cfb\u7edf", None))
#         self.leftGroup.setTitle("")
#         self.industrialC.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u76f8\u673a", None))
#         self.hyperspectralC.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5149\u8c31\u76f8\u673a", None))
#         self.connect.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8baf", None))
#         self.yoloDetection.setText(QCoreApplication.translate("MainWindow", u"yolo\u68c0\u6d4b", None))
#         self.F2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
#         self.F3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
#         self.rightGroup.setTitle("")
#         self.IndPara.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u76f8\u673a\u901a\u8baf\u53c2\u6570", None))
#         self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807IP", None))
#         self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7aef\u53e3\u53f7", None))
#         self.led1.setText(QCoreApplication.translate("MainWindow", u"Led", None))
#         self.InfoCon1.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65ad\u5f00", None))
#         self.IndCon.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
#         self.PLCPara.setTitle(QCoreApplication.translate("MainWindow", u"PLC\u901a\u8baf\u53c2\u6570", None))
#         self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807IP", None))
#         self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7aef\u53e3\u53f7", None))
#         self.led2.setText(QCoreApplication.translate("MainWindow", u"Led", None))
#         self.PLCCon.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65ad\u5f00", None))
#         self.InfoCon2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
#         self.monitorPara.setTitle(QCoreApplication.translate("MainWindow", u"PLC\u76d1\u63a7", None))
#         ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
#         ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
#         ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
#         ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
#         ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
#         ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740", None));
#         ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
#         ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
#         ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
#         ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
#         self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#         self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#         self.bottomGroup.setTitle("")
#         self.home.setText("")
#         self.Start.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
#         self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
#         self.Pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
#         self.Reset.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d", None))
#         self.startLed.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6307\u793a\u706f", None))
#         self.stopLed.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u6307\u793a\u706f", None))
#         self.pauseLed.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u6307\u793a\u706f", None))
#         self.resetLed.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d\u6307\u793a\u706f", None))
#     # retranslateUi
#

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindwAOvm.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
#import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 602)
        icon = QIcon()
        icon.addFile(u":/logo/Atoplogo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topGroup = QGroupBox(self.centralwidget)
        self.topGroup.setObjectName(u"topGroup")
        self.topGroup.setGeometry(QRect(10, 0, 871, 81))
        self.topLogo = QLabel(self.topGroup)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(0, 0, 81, 71))
        self.topLogo.setPixmap(QPixmap(u":/logo/Alogo.jpg"))
        self.topLogo.setScaledContents(True)
        self.topName = QLabel(self.topGroup)
        self.topName.setObjectName(u"topName")
        self.topName.setGeometry(QRect(280, 10, 341, 61))
        font = QFont()
        font.setPointSize(25)
        self.topName.setFont(font)
        self.topName.setTextFormat(Qt.TextFormat.AutoText)
        self.leftGroup = QGroupBox(self.centralwidget)
        self.leftGroup.setObjectName(u"leftGroup")
        self.leftGroup.setGeometry(QRect(0, 80, 161, 431))
        self.verticalLayout = QVBoxLayout(self.leftGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.industrialC = QPushButton(self.leftGroup)
        self.industrialC.setObjectName(u"industrialC")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.industrialC.setFont(font1)

        self.verticalLayout.addWidget(self.industrialC)

        self.hyperspectralC = QPushButton(self.leftGroup)
        self.hyperspectralC.setObjectName(u"hyperspectralC")
        self.hyperspectralC.setFont(font1)

        self.verticalLayout.addWidget(self.hyperspectralC)

        self.connect = QPushButton(self.leftGroup)
        self.connect.setObjectName(u"connect")
        self.connect.setFont(font1)

        self.verticalLayout.addWidget(self.connect)

        self.yoloDetection = QPushButton(self.leftGroup)
        self.yoloDetection.setObjectName(u"yoloDetection")
        self.yoloDetection.setFont(font1)

        self.verticalLayout.addWidget(self.yoloDetection)

        self.F2 = QPushButton(self.leftGroup)
        self.F2.setObjectName(u"F2")
        self.F2.setFont(font1)

        self.verticalLayout.addWidget(self.F2)

        self.F3 = QPushButton(self.leftGroup)
        self.F3.setObjectName(u"F3")
        self.F3.setFont(font1)

        self.verticalLayout.addWidget(self.F3)

        self.rightGroup = QGroupBox(self.centralwidget)
        self.rightGroup.setObjectName(u"rightGroup")
        self.rightGroup.setGeometry(QRect(160, 80, 721, 431))
        self.stackedWidget = QStackedWidget(self.rightGroup)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 711, 421))
        self.initialPage = QWidget()
        self.initialPage.setObjectName(u"initialPage")
        self.stackedWidget.addWidget(self.initialPage)
        self.connectPage = QWidget()
        self.connectPage.setObjectName(u"connectPage")
        self.IndPara = QGroupBox(self.connectPage)
        self.IndPara.setObjectName(u"IndPara")
        self.IndPara.setGeometry(QRect(0, 0, 351, 221))
        self.verticalLayout_2 = QVBoxLayout(self.IndPara)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.IndPara)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.IndIP = QLineEdit(self.IndPara)
        self.IndIP.setObjectName(u"IndIP")

        self.horizontalLayout.addWidget(self.IndIP)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.IndPara)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.IndPort = QLineEdit(self.IndPara)
        self.IndPort.setObjectName(u"IndPort")

        self.horizontalLayout_2.addWidget(self.IndPort)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.led1 = QLabel(self.IndPara)
        self.led1.setObjectName(u"led1")

        self.horizontalLayout_3.addWidget(self.led1)

        self.InfoCon1 = QLabel(self.IndPara)
        self.InfoCon1.setObjectName(u"InfoCon1")

        self.horizontalLayout_3.addWidget(self.InfoCon1)

        self.IndCon = QPushButton(self.IndPara)
        self.IndCon.setObjectName(u"IndCon")

        self.horizontalLayout_3.addWidget(self.IndCon)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.PLCPara = QGroupBox(self.connectPage)
        self.PLCPara.setObjectName(u"PLCPara")
        self.PLCPara.setGeometry(QRect(360, 0, 351, 221))
        self.verticalLayout_3 = QVBoxLayout(self.PLCPara)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.PLCPara)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.PLCIP = QLineEdit(self.PLCPara)
        self.PLCIP.setObjectName(u"PLCIP")

        self.horizontalLayout_4.addWidget(self.PLCIP)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.PLCPara)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.PLCPort = QLineEdit(self.PLCPara)
        self.PLCPort.setObjectName(u"PLCPort")

        self.horizontalLayout_5.addWidget(self.PLCPort)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.led2 = QLabel(self.PLCPara)
        self.led2.setObjectName(u"led2")

        self.horizontalLayout_6.addWidget(self.led2)

        self.PLCCon = QLabel(self.PLCPara)
        self.PLCCon.setObjectName(u"PLCCon")

        self.horizontalLayout_6.addWidget(self.PLCCon)

        self.InfoCon2 = QPushButton(self.PLCPara)
        self.InfoCon2.setObjectName(u"InfoCon2")

        self.horizontalLayout_6.addWidget(self.InfoCon2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.monitorPara = QGroupBox(self.connectPage)
        self.monitorPara.setObjectName(u"monitorPara")
        self.monitorPara.setGeometry(QRect(0, 220, 721, 201))
        self.tableWidget = QTableWidget(self.monitorPara)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 681, 191))
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.tableWidget.verticalHeader().setVisible(True)
        self.stackedWidget.addWidget(self.connectPage)
        self.yoloPage = QWidget()
        self.yoloPage.setObjectName(u"yoloPage")
        self.widget = QWidget(self.yoloPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 671, 411))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.yoloLog = QPlainTextEdit(self.widget)
        self.yoloLog.setObjectName(u"yoloLog")

        self.verticalLayout_4.addWidget(self.yoloLog)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.yoloEdit = QLineEdit(self.widget)
        self.yoloEdit.setObjectName(u"yoloEdit")

        self.horizontalLayout_7.addWidget(self.yoloEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.yoloPage)
        self.bottomGroup = QGroupBox(self.centralwidget)
        self.bottomGroup.setObjectName(u"bottomGroup")
        self.bottomGroup.setGeometry(QRect(0, 510, 881, 71))
        self.home = QLabel(self.bottomGroup)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(10, 10, 61, 61))
        self.home.setPixmap(QPixmap(u":/icon/home.png"))
        self.home.setScaledContents(True)
        self.home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Start = QPushButton(self.bottomGroup)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(80, 10, 75, 61))
        self.Stop = QPushButton(self.bottomGroup)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(280, 10, 75, 61))
        self.Pause = QPushButton(self.bottomGroup)
        self.Pause.setObjectName(u"Pause")
        self.Pause.setGeometry(QRect(450, 10, 75, 61))
        self.Reset = QPushButton(self.bottomGroup)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(630, 10, 75, 61))
        self.startLed = QLabel(self.bottomGroup)
        self.startLed.setObjectName(u"startLed")
        self.startLed.setGeometry(QRect(180, 15, 71, 51))
        self.stopLed = QLabel(self.bottomGroup)
        self.stopLed.setObjectName(u"stopLed")
        self.stopLed.setGeometry(QRect(370, 10, 71, 51))
        self.pauseLed = QLabel(self.bottomGroup)
        self.pauseLed.setObjectName(u"pauseLed")
        self.pauseLed.setGeometry(QRect(540, 10, 71, 51))
        self.resetLed = QLabel(self.bottomGroup)
        self.resetLed.setObjectName(u"resetLed")
        self.resetLed.setGeometry(QRect(720, 10, 81, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7389\u7c73\u79cd\u5b50\u6d3b\u529b\u68c0\u6d4b\u7cfb\u7edf", None))
        self.topGroup.setTitle("")
        self.topLogo.setText("")
        self.topName.setText(QCoreApplication.translate("MainWindow", u"\u7389\u7c73\u79cd\u5b50\u6d3b\u529b\u68c0\u6d4b\u7cfb\u7edf", None))
        self.leftGroup.setTitle("")
        self.industrialC.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u76f8\u673a", None))
        self.hyperspectralC.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5149\u8c31\u76f8\u673a", None))
        self.connect.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8baf", None))
        self.yoloDetection.setText(QCoreApplication.translate("MainWindow", u"yolo\u68c0\u6d4b", None))
        self.F2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.F3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.rightGroup.setTitle("")
        self.IndPara.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u76f8\u673a\u901a\u8baf\u53c2\u6570", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807IP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7aef\u53e3\u53f7", None))
        self.led1.setText(QCoreApplication.translate("MainWindow", u"Led", None))
        self.InfoCon1.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65ad\u5f00", None))
        self.IndCon.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.PLCPara.setTitle(QCoreApplication.translate("MainWindow", u"PLC\u901a\u8baf\u53c2\u6570", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807IP", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7aef\u53e3\u53f7", None))
        self.led2.setText(QCoreApplication.translate("MainWindow", u"Led", None))
        self.PLCCon.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65ad\u5f00", None))
        self.InfoCon2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.monitorPara.setTitle(QCoreApplication.translate("MainWindow", u"PLC\u76d1\u63a7", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b", None))
        self.bottomGroup.setTitle("")
        self.home.setText("")
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.Pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d", None))
        self.startLed.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6307\u793a\u706f", None))
        self.stopLed.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u6307\u793a\u706f", None))
        self.pauseLed.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u6307\u793a\u706f", None))
        self.resetLed.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d\u6307\u793a\u706f", None))
    # retranslateUi

