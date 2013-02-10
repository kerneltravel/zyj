# -*- coding: utf-8 -*-

"""
Module implementing ZyjWin.
"""
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature, QString

from Ui_zyj import Ui_ZyjWin
#from data.zyjdata import ZyjDataLogic

class ZyjWin(QMainWindow, Ui_ZyjWin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.dataL = None
        self.nPageCount = None
        self.nPageCur = 1
        self.nPagePer = 100
        
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.keywd = ""
        #self.data = ZyjDataOp()
        
        self.model = QtSql.QSqlQueryModel()
        self.model.setQuery('select docid,title,content from articles_vt limit 0,%s'%self.nPagePer)
        print 'last sql error:'
        print self.model.lastError().text()
        #self.select()
        print self.model.record(0).value("content").toString().isEmpty()
        #model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        print '===========x=='
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Article")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Content")
        self.contentTableview.setModel(self.model)
        #self.contentTableview.show()
        
    @QtCore.pyqtSignature("") 
    def on_searchButton_clicked(self):
        self.keywd = self.keywdPlainTextEdit.toPlainText()
        if self.keywd.isEmpty():
            return
        else:
            #self.model.doQuery(self.keywd)
            #qstringKeywd = QString(self.keywd)
            queryStr = "select docid,title,content from articles_vt where articles_vt match '%s' limit %s,%s"% (self.keywd, 
                                                                                                                (self.nPageCur-1)*self.nPagePer, self.nPagePer)
            #sql = "SELECT * FROM server WHERE platform='%s'" % platform
            print queryStr
            self.model.setQuery(queryStr)
            self.contentTableview.setModel(self.model)
            print self.model.rowCount()
            
    @QtCore.pyqtSignature("")
    def on_bookCombox_Changed(self):
        pass
    
    @QtCore.pyqtSignature("")
    def on_bookpartCombox_Changed(self):
        pass
    
    @QtCore.pyqtSignature("")
    def on_preButton_clicked(self):
        if self.nPageCur > 0:
            self.nPageCur = self.nPageCur-1
            self.on_searchButton_clicked()
        pass
    
    @QtCore.pyqtSignature("")
    def on_nextButton_clicked(self):
        self.nPageCur = self.nPageCur+1
        self.on_searchButton_clicked()
    
    @QtCore.pyqtSignature("")
    def on_headButton_clicked(self):
        self.nPageCur = 1
        self.on_searchButton_clicked()
        pass
        
    def on_cell(self):
        pass
    def on_links(self):
        pass
