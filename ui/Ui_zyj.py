# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\python\zyj_pyqt\ui\zyj.ui'
#
# Created: Sat Mar 02 10:25:23 2013
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
        ZyjWin.resize(701, 627)
        self.centralwidget = QtGui.QWidget(ZyjWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.searchlabel = QtGui.QLabel(self.centralwidget)
        self.searchlabel.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.searchlabel.setObjectName(_fromUtf8("searchlabel"))
        self.keywdPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.keywdPlainTextEdit.setGeometry(QtCore.QRect(20, 30, 151, 31))
        self.keywdPlainTextEdit.setObjectName(_fromUtf8("keywdPlainTextEdit"))
        self.bookCombox = QtGui.QComboBox(self.centralwidget)
        self.bookCombox.setGeometry(QtCore.QRect(20, 70, 151, 22))
        self.bookCombox.setObjectName(_fromUtf8("bookCombox"))
        self.tagsListWidget = QtGui.QListWidget(self.centralwidget)
        self.tagsListWidget.setGeometry(QtCore.QRect(525, 100, 161, 461))
        self.tagsListWidget.setObjectName(_fromUtf8("tagsListWidget"))
        item = QtGui.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        self.tagsLabel = QtGui.QLabel(self.centralwidget)
        self.tagsLabel.setGeometry(QtCore.QRect(530, 70, 91, 16))
        self.tagsLabel.setObjectName(_fromUtf8("tagsLabel"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(180, 30, 111, 31))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.contentTableview = QtGui.QTableView(self.centralwidget)
        self.contentTableview.setGeometry(QtCore.QRect(20, 100, 481, 441))
        self.contentTableview.setObjectName(_fromUtf8("contentTableview"))
        self.bookpartCombox = QtGui.QComboBox(self.centralwidget)
        self.bookpartCombox.setGeometry(QtCore.QRect(180, 70, 151, 22))
        self.bookpartCombox.setObjectName(_fromUtf8("bookpartCombox"))
        self.headButton = QtGui.QPushButton(self.centralwidget)
        self.headButton.setGeometry(QtCore.QRect(150, 550, 111, 31))
        self.headButton.setObjectName(_fromUtf8("headButton"))
        self.preButton = QtGui.QPushButton(self.centralwidget)
        self.preButton.setGeometry(QtCore.QRect(270, 550, 111, 31))
        self.preButton.setObjectName(_fromUtf8("preButton"))
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(390, 550, 111, 31))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        ZyjWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ZyjWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ZyjWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ZyjWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ZyjWin.setStatusBar(self.statusbar)

        self.retranslateUi(ZyjWin)
        QtCore.QMetaObject.connectSlotsByName(ZyjWin)
        ZyjWin.setTabOrder(self.keywdPlainTextEdit, self.bookCombox)
        ZyjWin.setTabOrder(self.bookCombox, self.tagsListWidget)

    def retranslateUi(self, ZyjWin):
        ZyjWin.setWindowTitle(_translate("ZyjWin", "Traditional Chinese Medicine Manual", None))
        self.searchlabel.setText(_translate("ZyjWin", "I\'d search...", None))
        __sortingEnabled = self.tagsListWidget.isSortingEnabled()
        self.tagsListWidget.setSortingEnabled(False)
        item = self.tagsListWidget.item(0)
        item.setText(_translate("ZyjWin", "理", None))
        item = self.tagsListWidget.item(1)
        item.setText(_translate("ZyjWin", "法", None))
        item = self.tagsListWidget.item(2)
        item.setText(_translate("ZyjWin", "方", None))
        item = self.tagsListWidget.item(3)
        item.setText(_translate("ZyjWin", "药", None))
        item = self.tagsListWidget.item(4)
        item.setText(_translate("ZyjWin", "其他", None))
        self.tagsListWidget.setSortingEnabled(__sortingEnabled)
        self.tagsLabel.setText(_translate("ZyjWin", "Quick Link:", None))
        self.searchButton.setText(_translate("ZyjWin", "search", None))
        self.headButton.setText(_translate("ZyjWin", "Head", None))
        self.preButton.setText(_translate("ZyjWin", "Pre", None))
        self.nextButton.setText(_translate("ZyjWin", "Next", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ZyjWin = QtGui.QMainWindow()
    ui = Ui_ZyjWin()
    ui.setupUi(ZyjWin)
    ZyjWin.show()
    sys.exit(app.exec_())

