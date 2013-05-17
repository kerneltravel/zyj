# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from Ui_bookmark import Ui_Bookmark

#sqlite> create table bookmarks(id int primary key ,showname text,comments text,
#artids text,modifiedate text);
class Bookmark(QDialog, Ui_Bookmark):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.model = QSqlQueryModel()
        self.model.setQuery('select * from bookmarks;')
        print self.model.lastError().text()
        #self.treeWidgetSearchResultBmk.setHeaderLabels(QStringList("name").append("article"))
        self.treeWidgetSearchResultBmk.setColumnCount(2)
        headlst =QStringList("name")<<("article")
        print headlst.count()
        self.treeWidgetSearchResultBmk.setHeaderItem(QTreeWidgetItem(headlst))
        #print self.treeWidgetSearchResultBmk.headerItem().text(0)
        i = 0
        print self.model.record(0).value("showname").toString()
        while i < self.model.rowCount():
            print self.model.record(i).value("showname").toString()            
            print self.model.record(i).value("artids").toString()
            self.treeWidgetSearchResultBmk.insertTopLevelItem(i, QTreeWidgetItem(
                                                                                 QStringList()<<self.model.record(i).value("showname").toString()
                                                                                 <<self.model.record(i).value("artids").toString()
                                                                                 ))
            i = i+1
    pass

def createConnection():         
    if __name__ == "__main__":
        db=QSqlDatabase.addDatabase("QSQLITE") 
        db.setDatabaseName("../f.db") 
        return db.open()
    else:
        return None
    
if __name__ == "__main__":
    import sys
    if not createConnection():
        print 'error open database'
    app = QtGui.QApplication(sys.argv)
    
    bookmark = Bookmark()
    #print bookmark.__dict__
    bookmark.show()
    sys.exit(app.exec_())
