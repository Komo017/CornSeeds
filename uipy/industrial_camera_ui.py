# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IndustrialCameraLXQnGZ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
#import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 613)
        icon = QIcon()
        icon.addFile(u":/logo/Atoplogo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topGroup = QGroupBox(self.centralwidget)
        self.topGroup.setObjectName(u"topGroup")
        self.topGroup.setGeometry(QRect(10, 0, 871, 81))
        self.topName = QLabel(self.topGroup)
        self.topName.setObjectName(u"topName")
        self.topName.setGeometry(QRect(280, 10, 341, 61))
        font = QFont()
        font.setPointSize(25)
        self.topName.setFont(font)
        self.topName.setTextFormat(Qt.TextFormat.AutoText)
        self.leftGroup = QGroupBox(self.centralwidget)
        self.leftGroup.setObjectName(u"leftGroup")
        self.leftGroup.setGeometry(QRect(0, 80, 161, 521))
        self.verticalLayout = QVBoxLayout(self.leftGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.manualPhoto = QPushButton(self.leftGroup)
        self.manualPhoto.setObjectName(u"manualPhoto")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.manualPhoto.setFont(font1)

        self.verticalLayout.addWidget(self.manualPhoto)

        self.autoPhoto = QPushButton(self.leftGroup)
        self.autoPhoto.setObjectName(u"autoPhoto")
        self.autoPhoto.setFont(font1)

        self.verticalLayout.addWidget(self.autoPhoto)

        self.ratePhoto = QPushButton(self.leftGroup)
        self.ratePhoto.setObjectName(u"ratePhoto")
        self.ratePhoto.setFont(font1)

        self.verticalLayout.addWidget(self.ratePhoto)

        self.RGBsettings = QPushButton(self.leftGroup)
        self.RGBsettings.setObjectName(u"RGBsettings")
        self.RGBsettings.setFont(font1)

        self.verticalLayout.addWidget(self.RGBsettings)

        self.HSVchannel = QPushButton(self.leftGroup)
        self.HSVchannel.setObjectName(u"HSVchannel")
        self.HSVchannel.setFont(font1)

        self.verticalLayout.addWidget(self.HSVchannel)

        self.Configuration = QPushButton(self.leftGroup)
        self.Configuration.setObjectName(u"Configuration")
        self.Configuration.setFont(font1)

        self.verticalLayout.addWidget(self.Configuration)

        self.Settings = QPushButton(self.leftGroup)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setFont(font1)

        self.verticalLayout.addWidget(self.Settings)

        self.fromPhoto = QPushButton(self.leftGroup)
        self.fromPhoto.setObjectName(u"fromPhoto")
        self.fromPhoto.setFont(font1)

        self.verticalLayout.addWidget(self.fromPhoto)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(169, 89, 701, 501))
        self.manualPage = QWidget()
        self.manualPage.setObjectName(u"manualPage")
        self.showPhoto = QLabel(self.manualPage)
        self.showPhoto.setObjectName(u"showPhoto")
        self.showPhoto.setGeometry(QRect(3, 15, 571, 481))
        self.onePhoto = QPushButton(self.manualPage)
        self.onePhoto.setObjectName(u"onePhoto")
        self.onePhoto.setGeometry(QRect(590, 70, 75, 61))
        self.stackedWidget.addWidget(self.manualPage)
        self.autoPage = QWidget()
        self.autoPage.setObjectName(u"autoPage")
        self.showPhoto2 = QLabel(self.autoPage)
        self.showPhoto2.setObjectName(u"showPhoto2")
        self.showPhoto2.setGeometry(QRect(10, 10, 571, 481))
        self.startPhoto = QPushButton(self.autoPage)
        self.startPhoto.setObjectName(u"startPhoto")
        self.startPhoto.setGeometry(QRect(610, 50, 75, 61))
        self.stopPhoto = QPushButton(self.autoPage)
        self.stopPhoto.setObjectName(u"stopPhoto")
        self.stopPhoto.setGeometry(QRect(610, 130, 75, 61))
        self.endPhoto = QPushButton(self.autoPage)
        self.endPhoto.setObjectName(u"endPhoto")
        self.endPhoto.setGeometry(QRect(610, 200, 75, 61))
        self.stackedWidget.addWidget(self.autoPage)
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
        self.topName.setText(QCoreApplication.translate("MainWindow", u"\u7389\u7c73\u79cd\u5b50\u6d3b\u529b\u68c0\u6d4b\u7cfb\u7edf", None))
        self.leftGroup.setTitle("")
        self.manualPhoto.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u62cd\u7167", None))
        self.autoPhoto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u62cd\u7167", None))
        self.ratePhoto.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167\u901f\u7387", None))
        self.RGBsettings.setText(QCoreApplication.translate("MainWindow", u"RGB\u8bbe\u7f6e", None))
        self.HSVchannel.setText(QCoreApplication.translate("MainWindow", u"HSV\u901a\u9053", None))
        self.Configuration.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.fromPhoto.setText(QCoreApplication.translate("MainWindow", u"\u7167\u7247\u6eaf\u6e90", None))
        self.showPhoto.setText("")
        self.onePhoto.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167\u4e00\u6b21", None))
        self.showPhoto2.setText("")
        self.startPhoto.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u62cd\u7167", None))
        self.stopPhoto.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u62cd\u7167", None))
        self.endPhoto.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u62cd\u7167", None))
    # retranslateUi

