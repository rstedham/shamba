# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'name_dialog.ui'
#
# Created: Thu Jul 31 17:40:37 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_name(object):
    def setupUi(self, name):
        name.setObjectName("name")
        name.resize(336, 124)
        self.gridLayout = QtGui.QGridLayout(name)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtGui.QLabel(name)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.nameBox = QtGui.QLineEdit(name)
        self.nameBox.setObjectName("nameBox")
        self.gridLayout.addWidget(self.nameBox, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(name)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(name)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), name.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), name.reject)
        QtCore.QMetaObject.connectSlotsByName(name)

    def retranslateUi(self, name):
        name.setWindowTitle(QtGui.QApplication.translate("name", "Baseline scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("name", "Enter a name for the new baseline scenario", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    name = QtGui.QDialog()
    ui = Ui_name()
    ui.setupUi(name)
    name.show()
    sys.exit(app.exec_())

