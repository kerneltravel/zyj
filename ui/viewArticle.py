# -*- coding: utf-8 -*-

from Ui_viewarticle import Ui_viewArticle
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class ViewArticle(QDialog, Ui_viewArticle):
    def __init__(self, title="", content="", parent = None):
        #QMainWindow.__init__(self, parent)
        #Ui_viewArticle.__init__(self)
        super(ViewArticle, self).__init__(parent)
        #QDialog.__init__(self, parent)
        #viewArticle = QtGui.QDialog()
        self.setupUi(self)
        self.setWindowTitle(title)
        
        if content is not "":
            print content.toLocal8Bit()
            content = content.replace(u" \r\n", u"")
            content = content.replace(u"\\x", u"\n\n")
            #print content.toLocal8Bit()
        self.articleContent.setPlainText(content)
        #self.articleContent.
        #self.show()
