import atexit
from PyQt4 import QtCore, QtGui, QtSql
from ui.zyjwin import ZyjWin

@atexit.register
def appExit():
    pass

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('f.db')
    print db.lastError().text()
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
            QtGui.qApp.tr("Unable to establish a database connection.\n"
                          "This example needs SQLite support. Please read "
                          "the Qt SQL driver documentation for information "
                          "how to build it.\n\n"
                          "Click Cancel to exit."),
            QtGui.QMessageBox.Cancel)
        sys.exit(1)
    calculator = ZyjWin()
    calculator.show()
    sys.exit(app.exec_())
