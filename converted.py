from PyQt4 import QtCore, QtGui
import sys



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class Window(QtGui.QMainWindow):
    def set_layout(self):
        """Creates the layout and initializes all objects""" 
        self.setWindowTitle("Title Goes Here") 
        self.setObjectName(_fromUtf8("self"))
        self.resize(522, 402)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calc_win = QtGui.QLineEdit(self.centralwidget)
        self.calc_win.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.calc_win.setFont(font)
        self.calc_win.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calc_win.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.calc_win.setReadOnly(True)
        self.calc_win.setObjectName(_fromUtf8("calc_win"))
        self.verticalLayout.addWidget(self.calc_win)
        self.num_layout = QtGui.QGridLayout()
        self.num_layout.setSpacing(20)
        self.num_layout.setObjectName(_fromUtf8("num_layout"))
        self.btn_7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.num_layout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_8 = QtGui.QPushButton(self.centralwidget)
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.num_layout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_9 = QtGui.QPushButton(self.centralwidget)
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.num_layout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.but_lp = QtGui.QPushButton(self.centralwidget)
        self.but_lp.setObjectName(_fromUtf8("but_lp"))
        self.num_layout.addWidget(self.but_lp, 4, 0, 1, 1)
        self.btn_6 = QtGui.QPushButton(self.centralwidget)
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.num_layout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_0 = QtGui.QPushButton(self.centralwidget)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.num_layout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_bksp = QtGui.QPushButton(self.centralwidget)
        self.btn_bksp.setObjectName(_fromUtf8("btn_bksp"))
        self.num_layout.addWidget(self.btn_bksp, 3, 0, 1, 1)
        self.btn_4 = QtGui.QPushButton(self.centralwidget)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.num_layout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtGui.QPushButton(self.centralwidget)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.num_layout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_1 = QtGui.QPushButton(self.centralwidget)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.num_layout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_2 = QtGui.QPushButton(self.centralwidget)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.num_layout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_sub = QtGui.QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(_fromUtf8("btn_sub"))
        self.num_layout.addWidget(self.btn_sub, 1, 3, 1, 1)
        self.btn_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.num_layout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_dot = QtGui.QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(_fromUtf8("btn_dot"))
        self.num_layout.addWidget(self.btn_dot, 3, 2, 1, 1)
        self.btn_div = QtGui.QPushButton(self.centralwidget)
        self.btn_div.setObjectName(_fromUtf8("btn_div"))
        self.num_layout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn_add = QtGui.QPushButton(self.centralwidget)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.num_layout.addWidget(self.btn_add, 0, 3, 1, 1)
        self.btn_mul = QtGui.QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(_fromUtf8("btn_mul"))
        self.num_layout.addWidget(self.btn_mul, 2, 3, 1, 1)
        self.but_mod = QtGui.QPushButton(self.centralwidget)
        self.but_mod.setObjectName(_fromUtf8("but_mod"))
        self.num_layout.addWidget(self.but_mod, 4, 3, 1, 1)
        self.btn_exp = QtGui.QPushButton(self.centralwidget)
        self.btn_exp.setObjectName(_fromUtf8("btn_exp"))
        self.num_layout.addWidget(self.btn_exp, 4, 2, 1, 1)
        self.btn_rp = QtGui.QPushButton(self.centralwidget)
        self.btn_rp.setObjectName(_fromUtf8("btn_rp"))
        self.num_layout.addWidget(self.btn_rp, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.num_layout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionReset = QtGui.QAction(self)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionUndo = QtGui.QAction(self)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionQuit_2 = QtGui.QAction(self)
        self.actionQuit_2.setObjectName(_fromUtf8("actionQuit_2"))
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionUndo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_2)
        self.menubar.addAction(self.menuFile.menuAction())
        

        

        self.setWindowTitle("self")
        self.calc_win.setText("0")
        self.btn_7.setText("7")
        self.btn_8.setText("8")
        self.btn_9.setText("9")
        self.but_lp.setText("(")
        self.btn_6.setText("6")
        self.btn_0.setText("0")
        self.btn_bksp.setText("Backspace")
        self.btn_4.setText("4")
        self.btn_5.setText("5")
        self.btn_1.setText("1")
        self.btn_2.setText("2")
        self.btn_sub.setText("-")
        self.btn_3.setText("3")
        self.btn_dot.setText(".")
        self.btn_div.setText("/")
        self.btn_add.setText("+")
        self.btn_mul.setText("*")
        self.but_mod.setText("%")
        self.btn_exp.setText("**")
        self.btn_rp.setText(")")
        self.menuFile.setTitle("File")
        self.actionReset.setText("Reset")
        self.actionQuit.setText("Quit")
        self.actionUndo.setText("Undo")
        self.actionQuit_2.setText("Quit")



    def __init__(self):
        """The initialization method, which intializes the actions of each button and shows the GUI""" 
        super(Window, self).__init__()
        self.set_layout()
        self.show()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(app.exec_())
