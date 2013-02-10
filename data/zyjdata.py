from PyQt4 import QtCore, QtGui, QtSql


class ZyjData(QtSql.QSqlQueryModel):
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

class ZyjDataLogic:
    def __init__(self):
        self.d = ZyjData()
        self.PageModel = None
        self.nPageCount = 0
        self.nArticlePerPage = 0
        self.oldQuery = None
        
    def update_article(self, title, content, tags):
        pass
    def delete_article(self, docid):
        pass
    def get_article(self, docid):
        pass
    '''def keywordResult(self, keyword, resutStartFrom):
        pass
        '''
    def getCurPageModel(self):
        pass
