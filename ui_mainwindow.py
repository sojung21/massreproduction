# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Sep 22 19:33:28 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1358, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.rangedTable = QtGui.QTableView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangedTable.sizePolicy().hasHeightForWidth())
        self.rangedTable.setSizePolicy(sizePolicy)
        self.rangedTable.setMinimumSize(QtCore.QSize(420, 335))
        self.rangedTable.setMaximumSize(QtCore.QSize(430, 16777215))
        self.rangedTable.setFrameShadow(QtGui.QFrame.Sunken)
        self.rangedTable.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.rangedTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.rangedTable.setGridStyle(QtCore.Qt.SolidLine)
        self.rangedTable.setSortingEnabled(True)
        self.rangedTable.setObjectName(_fromUtf8("rangedTable"))
        self.rangedTable.horizontalHeader().setDefaultSectionSize(65)
        self.rangedTable.horizontalHeader().setMinimumSectionSize(20)
        self.rangedTable.horizontalHeader().setStretchLastSection(True)
        self.rangedTable.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.workingFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workingFrame.sizePolicy().hasHeightForWidth())
        self.workingFrame.setSizePolicy(sizePolicy)
        self.workingFrame.setMinimumSize(QtCore.QSize(550, 350))
        self.workingFrame.setObjectName(_fromUtf8("workingFrame"))
        self.horizontalLayout_2.addWidget(self.workingFrame)
        self.right_panel = QtGui.QVBoxLayout()
        self.right_panel.setObjectName(_fromUtf8("right_panel"))
        self.experimentIDLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentIDLineEdit.sizePolicy().hasHeightForWidth())
        self.experimentIDLineEdit.setSizePolicy(sizePolicy)
        self.experimentIDLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.experimentIDLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica Neue"))
        font.setItalic(True)
        self.experimentIDLineEdit.setFont(font)
        self.experimentIDLineEdit.setObjectName(_fromUtf8("experimentIDLineEdit"))
        self.right_panel.addWidget(self.experimentIDLineEdit)
        self.experimentdescriptionLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentdescriptionLineEdit.sizePolicy().hasHeightForWidth())
        self.experimentdescriptionLineEdit.setSizePolicy(sizePolicy)
        self.experimentdescriptionLineEdit.setMinimumSize(QtCore.QSize(200, 140))
        self.experimentdescriptionLineEdit.setMaximumSize(QtCore.QSize(200, 140))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica Neue"))
        font.setItalic(True)
        self.experimentdescriptionLineEdit.setFont(font)
        self.experimentdescriptionLineEdit.setFrame(True)
        self.experimentdescriptionLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.experimentdescriptionLineEdit.setObjectName(_fromUtf8("experimentdescriptionLineEdit"))
        self.right_panel.addWidget(self.experimentdescriptionLineEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.right_panel.addItem(spacerItem)
        self.bin_size = QtGui.QVBoxLayout()
        self.bin_size.setObjectName(_fromUtf8("bin_size"))
        self.binsizeLabel = QtGui.QLabel(self.centralwidget)
        self.binsizeLabel.setObjectName(_fromUtf8("binsizeLabel"))
        self.bin_size.addWidget(self.binsizeLabel)
        self.binsizeSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binsizeSlider.sizePolicy().hasHeightForWidth())
        self.binsizeSlider.setSizePolicy(sizePolicy)
        self.binsizeSlider.setMinimum(250)
        self.binsizeSlider.setMaximum(6000)
        self.binsizeSlider.setSingleStep(10)
        self.binsizeSlider.setProperty("value", 1000)
        self.binsizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.binsizeSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.binsizeSlider.setObjectName(_fromUtf8("binsizeSlider"))
        self.bin_size.addWidget(self.binsizeSlider)
        self.right_panel.addLayout(self.bin_size)
        self.hits = QtGui.QVBoxLayout()
        self.hits.setObjectName(_fromUtf8("hits"))
        self.allhitsRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.allhitsRadioButton.setChecked(True)
        self.allhitsRadioButton.setObjectName(_fromUtf8("allhitsRadioButton"))
        self.hits.addWidget(self.allhitsRadioButton)
        self.singlehitsRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.singlehitsRadioButton.setEnabled(False)
        self.singlehitsRadioButton.setObjectName(_fromUtf8("singlehitsRadioButton"))
        self.hits.addWidget(self.singlehitsRadioButton)
        self.multiplehitsRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.multiplehitsRadioButton.setEnabled(False)
        self.multiplehitsRadioButton.setObjectName(_fromUtf8("multiplehitsRadioButton"))
        self.hits.addWidget(self.multiplehitsRadioButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.minhitsLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.minhitsLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minhitsLineEdit.sizePolicy().hasHeightForWidth())
        self.minhitsLineEdit.setSizePolicy(sizePolicy)
        self.minhitsLineEdit.setMinimumSize(QtCore.QSize(35, 0))
        self.minhitsLineEdit.setMaximumSize(QtCore.QSize(35, 16777215))
        self.minhitsLineEdit.setBaseSize(QtCore.QSize(75, 0))
        self.minhitsLineEdit.setMaxLength(3)
        self.minhitsLineEdit.setObjectName(_fromUtf8("minhitsLineEdit"))
        self.horizontalLayout.addWidget(self.minhitsLineEdit)
        self.maxhitsLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.maxhitsLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxhitsLineEdit.sizePolicy().hasHeightForWidth())
        self.maxhitsLineEdit.setSizePolicy(sizePolicy)
        self.maxhitsLineEdit.setMinimumSize(QtCore.QSize(35, 10))
        self.maxhitsLineEdit.setMaximumSize(QtCore.QSize(35, 16777215))
        self.maxhitsLineEdit.setBaseSize(QtCore.QSize(75, 10))
        self.maxhitsLineEdit.setMaxLength(3)
        self.maxhitsLineEdit.setObjectName(_fromUtf8("maxhitsLineEdit"))
        self.horizontalLayout.addWidget(self.maxhitsLineEdit)
        self.hits.addLayout(self.horizontalLayout)
        self.right_panel.addLayout(self.hits)
        self.horizontalLayout_2.addLayout(self.right_panel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1358, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuLoad = QtGui.QMenu(self.menuEdit)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        self.menuExport_as = QtGui.QMenu(self.menuEdit)
        self.menuExport_as.setObjectName(_fromUtf8("menuExport_as"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_Recent = QtGui.QAction(MainWindow)
        self.actionOpen_Recent.setObjectName(_fromUtf8("actionOpen_Recent"))
        self.actionLoad = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../.designer/backup/document_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionAs_rng = QtGui.QAction(MainWindow)
        self.actionAs_rng.setObjectName(_fromUtf8("actionAs_rng"))
        self.actionAs_mr = QtGui.QAction(MainWindow)
        self.actionAs_mr.setObjectName(_fromUtf8("actionAs_mr"))
        self.actionLoad_rng = QtGui.QAction(MainWindow)
        self.actionLoad_rng.setObjectName(_fromUtf8("actionLoad_rng"))
        self.actionLoad_mr = QtGui.QAction(MainWindow)
        self.actionLoad_mr.setObjectName(_fromUtf8("actionLoad_mr"))
        self.action_LoadRNG = QtGui.QAction(MainWindow)
        self.action_LoadRNG.setObjectName(_fromUtf8("action_LoadRNG"))
        self.action_LoadMR = QtGui.QAction(MainWindow)
        self.action_LoadMR.setObjectName(_fromUtf8("action_LoadMR"))
        self.action_ExportAsRNG = QtGui.QAction(MainWindow)
        self.action_ExportAsRNG.setObjectName(_fromUtf8("action_ExportAsRNG"))
        self.action_ExportAsMR = QtGui.QAction(MainWindow)
        self.action_ExportAsMR.setObjectName(_fromUtf8("action_ExportAsMR"))
        self.actionTools = QtGui.QAction(MainWindow)
        self.actionTools.setObjectName(_fromUtf8("actionTools"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuLoad.addAction(self.action_LoadRNG)
        self.menuLoad.addAction(self.action_LoadMR)
        self.menuExport_as.addAction(self.action_ExportAsRNG)
        self.menuExport_as.addAction(self.action_ExportAsMR)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuLoad.menuAction())
        self.menuEdit.addAction(self.menuExport_as.menuAction())
        self.menuView.addAction(self.actionTools)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.experimentIDLineEdit.setText(_translate("MainWindow", "Experiment ID", None))
        self.experimentdescriptionLineEdit.setText(_translate("MainWindow", "Description/notes...", None))
        self.binsizeLabel.setText(_translate("MainWindow", "Bin size", None))
        self.allhitsRadioButton.setText(_translate("MainWindow", "All hits", None))
        self.singlehitsRadioButton.setText(_translate("MainWindow", "Single hits", None))
        self.multiplehitsRadioButton.setText(_translate("MainWindow", "Multiple hits", None))
        self.minhitsLineEdit.setText(_translate("MainWindow", "Min", None))
        self.maxhitsLineEdit.setText(_translate("MainWindow", "Max", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuLoad.setTitle(_translate("MainWindow", "Load...", None))
        self.menuExport_as.setTitle(_translate("MainWindow", "Export as...", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionNew.setText(_translate("MainWindow", "New...", None))
        self.actionNew.setToolTip(_translate("MainWindow", "Click to create a new project", None))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new project", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent", None))
        self.actionLoad.setText(_translate("MainWindow", "Load data...", None))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z", None))
        self.actionHistory.setText(_translate("MainWindow", "History", None))
        self.actionAs_rng.setText(_translate("MainWindow", "as .rng", None))
        self.actionAs_mr.setText(_translate("MainWindow", "as .mr", None))
        self.actionLoad_rng.setText(_translate("MainWindow", "Load .rng", None))
        self.actionLoad_mr.setText(_translate("MainWindow", "Load .mr", None))
        self.action_LoadRNG.setText(_translate("MainWindow", ".rng", None))
        self.action_LoadMR.setText(_translate("MainWindow", ".mr", None))
        self.action_ExportAsRNG.setText(_translate("MainWindow", ".rng", None))
        self.action_ExportAsMR.setText(_translate("MainWindow", ".mr", None))
        self.actionTools.setText(_translate("MainWindow", "Tools", None))

