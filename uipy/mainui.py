# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLVhIyk.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
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
        self.layoutWidget = QWidget(self.monitorPara)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 701, 91))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.out1 = QLineEdit(self.layoutWidget)
        self.out1.setObjectName(u"out1")

        self.horizontalLayout_8.addWidget(self.out1)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.out2 = QLineEdit(self.layoutWidget)
        self.out2.setObjectName(u"out2")

        self.horizontalLayout_9.addWidget(self.out2)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.out3 = QLineEdit(self.layoutWidget)
        self.out3.setObjectName(u"out3")

        self.horizontalLayout_10.addWidget(self.out3)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.out4 = QLineEdit(self.layoutWidget)
        self.out4.setObjectName(u"out4")

        self.horizontalLayout_11.addWidget(self.out4)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.out5 = QLineEdit(self.layoutWidget)
        self.out5.setObjectName(u"out5")

        self.horizontalLayout_12.addWidget(self.out5)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.out6 = QLineEdit(self.layoutWidget)
        self.out6.setObjectName(u"out6")

        self.horizontalLayout_15.addWidget(self.out6)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_16.addWidget(self.label_11)

        self.out7 = QLineEdit(self.layoutWidget)
        self.out7.setObjectName(u"out7")

        self.horizontalLayout_16.addWidget(self.out7)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.out8 = QLineEdit(self.layoutWidget)
        self.out8.setObjectName(u"out8")

        self.horizontalLayout_17.addWidget(self.out8)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.out9 = QLineEdit(self.layoutWidget)
        self.out9.setObjectName(u"out9")

        self.horizontalLayout_18.addWidget(self.out9)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_19.addWidget(self.label_14)

        self.out10 = QLineEdit(self.layoutWidget)
        self.out10.setObjectName(u"out10")

        self.horizontalLayout_19.addWidget(self.out10)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.layoutWidget_2 = QWidget(self.monitorPara)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 110, 701, 81))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_21.addWidget(self.label_15)

        self.in1 = QLineEdit(self.layoutWidget_2)
        self.in1.setObjectName(u"in1")

        self.horizontalLayout_21.addWidget(self.in1)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_22.addWidget(self.label_16)

        self.in2 = QLineEdit(self.layoutWidget_2)
        self.in2.setObjectName(u"in2")

        self.horizontalLayout_22.addWidget(self.in2)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_23.addWidget(self.label_17)

        self.in3 = QLineEdit(self.layoutWidget_2)
        self.in3.setObjectName(u"in3")

        self.horizontalLayout_23.addWidget(self.in3)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.in4 = QLineEdit(self.layoutWidget_2)
        self.in4.setObjectName(u"in4")

        self.horizontalLayout_24.addWidget(self.in4)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_19 = QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_25.addWidget(self.label_19)

        self.in5 = QLineEdit(self.layoutWidget_2)
        self.in5.setObjectName(u"in5")

        self.horizontalLayout_25.addWidget(self.in5)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_25)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_20 = QLabel(self.layoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_27.addWidget(self.label_20)

        self.in6 = QLineEdit(self.layoutWidget_2)
        self.in6.setObjectName(u"in6")

        self.horizontalLayout_27.addWidget(self.in6)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_21 = QLabel(self.layoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_28.addWidget(self.label_21)

        self.in7 = QLineEdit(self.layoutWidget_2)
        self.in7.setObjectName(u"in7")

        self.horizontalLayout_28.addWidget(self.in7)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_22 = QLabel(self.layoutWidget_2)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_29.addWidget(self.label_22)

        self.in8 = QLineEdit(self.layoutWidget_2)
        self.in8.setObjectName(u"in8")

        self.horizontalLayout_29.addWidget(self.in8)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_23 = QLabel(self.layoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_30.addWidget(self.label_23)

        self.in9 = QLineEdit(self.layoutWidget_2)
        self.in9.setObjectName(u"in9")

        self.horizontalLayout_30.addWidget(self.in9)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_24 = QLabel(self.layoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_31.addWidget(self.label_24)

        self.in10 = QLineEdit(self.layoutWidget_2)
        self.in10.setObjectName(u"in10")

        self.horizontalLayout_31.addWidget(self.in10)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_31)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.stackedWidget.addWidget(self.connectPage)
        self.yoloPage = QWidget()
        self.yoloPage.setObjectName(u"yoloPage")
        self.layoutWidget1 = QWidget(self.yoloPage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 0, 671, 411))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.yoloLog = QPlainTextEdit(self.layoutWidget1)
        self.yoloLog.setObjectName(u"yoloLog")

        self.verticalLayout_4.addWidget(self.yoloLog)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.yoloEdit = QLineEdit(self.layoutWidget1)
        self.yoloEdit.setObjectName(u"yoloEdit")

        self.horizontalLayout_7.addWidget(self.yoloEdit)

        self.pushButton = QPushButton(self.layoutWidget1)
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

        self.stackedWidget.setCurrentIndex(1)


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
        self.monitorPara.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53d1\u9001", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OUT1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OUT2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OUT3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"OUT4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"OUT5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"OUT6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"OUT7", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"OUT8", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TCP9", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OUT10", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IN1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"IN2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"iIN3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"IN4", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"IN5", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"IN6", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"IN7", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"IN8", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IN9", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"IN10", None))
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

