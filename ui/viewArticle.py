# -*- coding: utf-8 -*-

from Ui_viewarticle import Ui_viewArticle
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class ViewArticle(QDialog, Ui_viewArticle):
    def getKeywordsHtml(self, kws, content, fontsize=13):
        if len(content)!=0:
            kws.replace(u" ", u"")
            for word in kws:
                newwd = u"<font size=%d><strong>%s</strong></font>"% (fontsize,word)
                content = content.replace(word, newwd)
            
            print content.toLocal8Bit()
        return content
            

    def __init__(self, keywords="", title="", content="", parent = None):
        #QMainWindow.__init__(self, parent)
        #Ui_viewArticle.__init__(self)
        super(ViewArticle, self).__init__(parent)
        #QDialog.__init__(self, parent)
        #viewArticle = QtGui.QDialog()
        self.setupUi(self)
        self.setWindowTitle(title)
        
        #self.keywd = u"感冒"
        self.content = ""
        
        if len(content) != 0:
            print content.toLocal8Bit()
            content = content.replace(u" \r\n", u"")
            content = content.replace(u"\\x", u"\n\n")
            #print content.toLocal8Bit()
        #self.articleContent.setPlainText(content)
        self.articleContent.appendHtml(self.getKeywordsHtml(keywords, content))
        self.articleContent.moveCursor(QTextCursor.Start)
