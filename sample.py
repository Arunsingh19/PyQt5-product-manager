import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Sample(QMainWindow):
    def __init__(self):
        super(Sample, self).__init__()
        self.setGeometry(10,10,1000,700)
        self.setWindowTitle("sample")
        self.ui()
        self.show()

    def ui(self):
        self.design()
        self.layout()

    def design(self):
        self.tb = self.addToolBar("sample")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addproduct = QAction(QIcon('icons/add.png'),"Add Product",self)
        self.tb.addAction(self.addproduct)
        self.addmember = QAction(QIcon('icons/user.png'),"Add member",self)
        self.tb.addAction(self.addmember)

        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab.addTab(self.tab1,"products")
        self.tab.addTab(self.tab2,"members")

        self.producttable = QTableWidget()
        self.producttable.setColumnCount(3)
        self.producttable.setColumnHidden(0,True)
        self.producttable.setHorizontalHeaderItem(0,QTableWidgetItem("product id"))
        self.producttable.setHorizontalHeaderItem(1,QTableWidgetItem("product name"))
        self.producttable.setHorizontalHeaderItem(2,QTableWidgetItem("price"))

        self.membertable = QTableWidget()
        self.membertable.setColumnCount(3)
        self.membertable.setColumnHidden(0,True)
        self.membertable.setHorizontalHeaderItem(0,QTableWidgetItem("member id"))
        self.membertable.setHorizontalHeaderItem(1,QTableWidgetItem("member name"))
        self.membertable.setHorizontalHeaderItem(2,QTableWidgetItem("dept"))

    def layout(self):
        self.mainlayout = QHBoxLayout()
        self.mainlayout.addWidget(self.producttable)
        self.


def main():
    App = QApplication(sys.argv)
    sample = Sample()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()



