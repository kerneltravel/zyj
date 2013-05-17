# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\python\zyj.git\zyj\ui\viewarticle.ui'
#
# Created: Fri May 17 20:20:45 2013
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

class Ui_viewArticle(object):
    def setupUi(self, viewArticle):
        viewArticle.setObjectName(_fromUtf8("viewArticle"))
        viewArticle.setWindowModality(QtCore.Qt.ApplicationModal)
        viewArticle.resize(413, 411)
        viewArticle.setSizeGripEnabled(True)
        self.horizontalLayout = QtGui.QHBoxLayout(viewArticle)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.articleContent = QtGui.QPlainTextEdit(viewArticle)
        self.articleContent.setObjectName(_fromUtf8("articleContent"))
        self.verticalLayout.addWidget(self.articleContent)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(viewArticle)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(viewArticle)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(viewArticle)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), viewArticle.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), viewArticle.reject)
        QtCore.QMetaObject.connectSlotsByName(viewArticle)

    def retranslateUi(self, viewArticle):
        viewArticle.setWindowTitle(_translate("viewArticle", "view", None))
        self.okButton.setText(_translate("viewArticle", "&OK", None))
        self.cancelButton.setText(_translate("viewArticle", "&Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    viewArticle = QtGui.QDialog()
    ui = Ui_viewArticle()
    ui.setupUi(viewArticle)
    viewArticle.show()
    sys.exit(app.exec_())

