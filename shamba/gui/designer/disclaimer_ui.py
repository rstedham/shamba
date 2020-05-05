# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './shamba/disclaimer.ui'
#
# Created: Wed Jun 27 15:56:34 2012
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Disclaimer(object):
    def setupUi(self, Disclaimer):
        Disclaimer.setObjectName("Disclaimer")
        Disclaimer.resize(400, 524)
        self.verticalLayout = QtGui.QVBoxLayout(Disclaimer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splashImage = QtGui.QLabel(Disclaimer)
        self.splashImage.setMinimumSize(QtCore.QSize(320, 240))
        self.splashImage.setAlignment(QtCore.Qt.AlignCenter)
        self.splashImage.setObjectName("splashImage")
        self.verticalLayout.addWidget(self.splashImage)
        self.scrollArea = QtGui.QScrollArea(Disclaimer)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 223))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.disclaimerText = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.disclaimerText.setWordWrap(True)
        self.disclaimerText.setObjectName("disclaimerText")
        self.verticalLayout_2.addWidget(self.disclaimerText)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(Disclaimer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Disclaimer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Disclaimer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Disclaimer.reject)
        QtCore.QMetaObject.connectSlotsByName(Disclaimer)

    def retranslateUi(self, Disclaimer):
        Disclaimer.setWindowTitle(QtGui.QApplication.translate("Disclaimer", "disclaimer", None, QtGui.QApplication.UnicodeUTF8))
        self.disclaimerText.setText(QtGui.QApplication.translate("Disclaimer", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

