# -*- coding: utf-8 -*-

"""
Module implementing ZyjWin.
"""
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_zyj import Ui_ZyjWin
from viewArticle import ViewArticle
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
        self.strOldKeyword = ""
        
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.keywd = ""
        #self.data = ZyjDataOp()
        self.modelAll = QtSql.QSqlQueryModel()
        
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
        
        #QtCore.QObject.connect(self.contentTableview, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.contentTableview_clicked)
        #self.connect(self.contentTableview, SIGNAL("clicked(QModelIndex)"), self.getCurrentIndex)
        
        self.createContextMenu()
        
    def createContextMenu(self):        
        self.server_list_contextmenu = QtGui.QMenu(self)  
        #self.server_list_contextmenu.addAction(self.action_move2left) 
        #self.server_list_contextmenu.addSeparator()
        self.server_list_contextmenu.addAction(self.action_add_to_favouriate)  
        #self.server_list_contextmenu.addAction(self.action_edit_server)  
        #self.server_list_contextmenu.addAction(self.action_copy_server)  
        #self.server_list_contextmenu.addSeparator()
        #self.server_list_contextmenu.addAction(self.action_delete_server) 

    @pyqtSlot(QPoint)
    def on_tagsListWidget_customContextMenuRequested(self, point):
        """
        Slot documentation goes here.
        """
        self.server_list_contextmenu.exec_(self.tagsListWidget.mapToGlobal(point))   
        
    
    def getCurKeyword(self):
        return self.keywdPlainTextEdit.toPlainText()
    
    @QtCore.pyqtSignature("") 
    def on_searchButton_clicked(self):
        self.keywd = self.getCurKeyword()
        if self.keywd.isEmpty():
            return
        else:
            '''关键词改变，则表示开始新查询。这时要重置当前页的值为1。
            关键词和上次一样，不变，则继续搜索指定页内容。
            '''
            if self.strOldKeyword != self.keywd:
                self.strOldKeyword = self.keywd
                self.nPageCur = 1
            #self.model.doQuery(self.keywd)
            #qstringKeywd = QString(self.keywd)
            queryStrAll = "select docid,title,content from articles_vt where articles_vt match '%s' "%(self.keywd)
            queryStr =  queryStrAll + "limit %s,%s"% ((self.nPageCur-1)*self.nPagePer, self.nPagePer)
            #sql = "SELECT * FROM server WHERE platform='%s'" % platform
            print queryStr
            self.model.setQuery(queryStr)
            self.contentTableview.setModel(self.model)
            print self.model.rowCount()
            
            '''开始根据计算 结果总行数。可以显示到界面上。翻页用到
            '''
            self.modelAll.setQuery("select count(docid) from articles_vt where articles_vt match '%s'"%(self.keywd))
            rowcount = self.modelAll.record(0).value(0).toInt()[0]
            self.nPageCount = rowcount/self.nPagePer
            if rowcount > 0 and  self.nPageCount > 0:
                if rowcount%self.nPageCount > 0:
                    self.nPageCount = self.nPageCount +1
            else:
                self.nPageCount = 1   
            print '%s,%s'%(rowcount, self.nPageCount)
            '''开始根据docid生成 bookCombox内的book列表和 bookpartCombox内的bookparts列表
            '''
            self.modelAll.clear()
            self.modelAll.setQuery("select docid from articles_vt where articles_vt match '%s'"%self.keywd)
            i = 0
            '''bookdoclst存储 book列表'''
            bookdoclst = [] 
            while i< rowcount:
                #print 'i:%s'%i
                if i%self.nPagePer==0:
                    self.modelAll.fetchMore()
                bookdoclst.append(self.modelAll.record(i).value(0).toInt()[0])
                i = i+1
            i = 0
            
            '''计算搜索结果对应的bookpart列表'''
            querystr = ""
            while i< rowcount:
                querystr = querystr +('%s OR '%bookdoclst[i])
                i = i+1
            querystr = querystr.rstrip('OR ')
            querystr = "select docid,name from bkparts_vt where articleids match '%s'"%( querystr)
            self.modelAll.clear()
            self.modelAll.setQuery(querystr)
            print 'querystr: %s'%querystr
            while self.modelAll.canFetchMore():
                #print 'i:%s'%i
                self.modelAll.fetchMore()

            i = 0
            #partIDlst = []
            self.bookpartCombox.clear()
            while i<self.modelAll.rowCount():
                #print "%s"%self.modelAll.record(i).value(1).toString()
                #self.bookpartCombox.addItem(self.modelAll.record(i).value(0).toString()[0])
                self.bookpartCombox.addItem("%s"%(self.modelAll.record(i).value(1).toString()),"%d"%(self.modelAll.record(i).value(0).toInt()[0]))
                #print 'doclist[%s]= %s'%(i, doclst[i])
                i = i+1
                
            '''计算book列表'''
            querystr=""
            i = 0
            while i < self.modelAll.rowCount():
                querystr = querystr+('%s OR '%(self.modelAll.record(i).value(0).toInt()[0]))
                i = i+1
            querystr = querystr.rstrip('OR ')
            querystr = "select docid,name from books_vt where partids match '%s'"%( querystr)
            self.modelAll.clear()
            self.modelAll.setQuery(querystr)
            print 'querystr: %s'%querystr
            while self.modelAll.canFetchMore():
                #print 'i:%s'%i
                self.modelAll.fetchMore()

            i = 0
            #partIDlst = []
            self.bookCombox.clear()
            while i<self.modelAll.rowCount():
                #print "%s"%self.modelAll.record(i).value(1).toString()
                #self.bookCombox.addItem(self.modelAll.record(i).value(0).toString()[0])
                self.bookCombox.addItem("%s"%(self.modelAll.record(i).value(1).toString()),"%d"%(self.modelAll.record(i).value(0).toInt()[0]))
                #print 'doclist[%s]= %s'%(i, doclst[i])
                i = i+1
            
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
        

    def on_links(self):
        pass
    
    @pyqtSlot(QModelIndex)
    def on_contentTableview_clicked(self, index):
        '''for itm in index.data().toStringList():
            print itm.toLocal8Bit()
        print 'row: %d'%index.row()
        print 'column %d'%index.column()
        print type(index.model())'''
        strlstRecord = QStringList()
        for clm in [0, 1, 2]:
            strlstRecord.append( index.model().record(index.row()).value(clm).toString())
        
        self.viewdialog = ViewArticle(strlstRecord[1], strlstRecord[2])
        self.viewdialog.show()
        
    @pyqtSlot(QModelIndex)
    def on_contentTableview_activated(self, index):
        self.on_contentTableview_clicked(index)
        pass
        
        
        
