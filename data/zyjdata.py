from PyQt4 import QtCore, QtGui, QtSql

import connection

class ZyjDataOp(QtSql.QSqlQueryModel):
    def __init__(self):
        super(ZyjDataOp, self).__init__()
        #if not connection.createConnection():
        #   sys.exit(1)
        #self.initModel()
        
    def doQuery(self, keyword=None):
        if not keyword :
            return
        else:
            queryStr = 'select docid,title,content from articles_vt where articles_vt match "'+keyword +'";'
            print queryStr
            self.setQuery(queryStr)
    
        
    def initModel(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('f.db')
        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\n"
                              "Click Cancel to exit."),
                QtGui.QMessageBox.Cancel)
            sys.exit(1)
        self.setQuery('select docid,title,content from articles_vt limit 0,100', db)
        #self.select()
        print self.record(0).value("content").toString().isEmpty()
        #model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        #model.select()
    
        self.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "Article")
        self.setHeaderData(2, QtCore.Qt.Horizontal, "Contens")
        pass
