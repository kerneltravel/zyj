# -*- coding: utf-8 -*-

"""
Module implementing ZyjWin.
"""
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature, QString

from Ui_zyj import Ui_ZyjWin
#from data.zyjdata import *

class ZyjWin(QMainWindow, Ui_ZyjWin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.keywd = ""
        #self.data = ZyjDataOp()
        
        self.model = QtSql.QSqlQueryModel()
        self.model.setQuery('select docid,title,content from articles_vt limit 0,100')
        print 'last sql error:'
        print self.model.lastError().text()
        #self.select()
        print self.model.record(0).value("content").toString().isEmpty()
        #model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        #model.select()
        print '===========x=='
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Article")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Content")
        self.contentTableview.setModel(self.model)
        #self.contentTableview.show()
        
        
    def on_searchButton_clicked(self):
        self.keywd = self.keywdPlainTextEdit.toPlainText()
        if self.keywd.isEmpty():
            return
        else:
            #self.model.doQuery(self.keywd)
            #qstringKeywd = QString(self.keywd)
            queryStr = "select docid,title,content from articles_vt where articles_vt match '%s'" % self.keywd
            #sql = "SELECT * FROM server WHERE platform='%s'" % platform
            print queryStr
            self.model.setQuery(queryStr)
            self.contentTableview.setModel(self.model)
            
