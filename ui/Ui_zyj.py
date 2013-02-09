# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\python\zyj_pyqt\ui\zyj.ui'
#
# Created: Tue Jan 29 21:44:44 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ZyjWin(object):
    def setupUi(self, ZyjWin):
        ZyjWin.setObjectName(_fromUtf8("ZyjWin"))
        ZyjWin.resize(696, 600)
        self.centralwidget = QtGui.QWidget(ZyjWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.searchlabel = QtGui.QLabel(self.centralwidget)
        self.searchlabel.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.searchlabel.setObjectName(_fromUtf8("searchlabel"))
        self.keywdPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.keywdPlainTextEdit.setGeometry(QtCore.QRect(20, 30, 151, 31))
        self.keywdPlainTextEdit.setObjectName(_fromUtf8("keywdPlainTextEdit"))
        self.categoryCbox = QtGui.QComboBox(self.centralwidget)
        self.categoryCbox.setGeometry(QtCore.QRect(20, 70, 151, 22))
        self.categoryCbox.setObjectName(_fromUtf8("categoryCbox"))
        self.categoryCbox.addItem(_fromUtf8(""))
        self.tagsListWidget = QtGui.QListWidget(self.centralwidget)
        self.tagsListWidget.setGeometry(QtCore.QRect(525, 100, 161, 461))
        self.tagsListWidget.setObjectName(_fromUtf8("tagsListWidget"))
        self.tagsLabel = QtGui.QLabel(self.centralwidget)
        self.tagsLabel.setGeometry(QtCore.QRect(530, 70, 91, 16))
        self.tagsLabel.setObjectName(_fromUtf8("tagsLabel"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.contentTableview = QtGui.QTableView(self.centralwidget)
        self.contentTableview.setGeometry(QtCore.QRect(20, 100, 481, 461))
        self.contentTableview.setObjectName(_fromUtf8("contentTableview"))
        ZyjWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ZyjWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ZyjWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ZyjWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ZyjWin.setStatusBar(self.statusbar)

        self.retranslateUi(ZyjWin)
        QtCore.QMetaObject.connectSlotsByName(ZyjWin)
        ZyjWin.setTabOrder(self.keywdPlainTextEdit, self.categoryCbox)
        ZyjWin.setTabOrder(self.categoryCbox, self.tagsListWidget)

    def retranslateUi(self, ZyjWin):
        ZyjWin.setWindowTitle(_translate("ZyjWin", "Traditional Chinese Medicine Manual", None))
        self.searchlabel.setText(_translate("ZyjWin", "I\'d search...", None))
        self.categoryCbox.setItemText(0, _translate("ZyjWin", "category", None))
        self.tagsLabel.setText(_translate("ZyjWin", "Quick Link:", None))
        self.searchButton.setText(_translate("ZyjWin", "search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ZyjWin = QtGui.QMainWindow()
    ui = Ui_ZyjWin()
    ui.setupUi(ZyjWin)
    ZyjWin.show()
    sys.exit(app.exec_())

