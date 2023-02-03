from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QMessageBox
import re


class ListWidget(QListWidget):
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(ListWidget, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        super(ListWidget, self).dragMoveEvent(event)
        
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            flag = True
            for url in event.mimeData().urls():
                reg = r'.*\.png$'
                reg1 = r'.*\.jpg$'
                
                if (re.match(reg, url.path()) is not None) or (re.match(reg1, url.path()) is not None):
                    self.addItem(url.path())
                else:
                    flag = False
            event.acceptProposedAction()
            if flag == False:
                msg = QMessageBox()
                msg.setWindowTitle("Предупреждение!")
                msg.setText("Были вставлены файлы с недопустимым расширением!")
                msg.setIcon(QMessageBox.Warning)

                msg.exec_()
        else:
            super(ListWidget,self).dropEvent(event)
 