# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dPCR_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1711, 1172)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ControllerLayout = QtWidgets.QGridLayout()
        self.ControllerLayout.setObjectName("ControllerLayout")
        self.verticalLayout_6.addLayout(self.ControllerLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExporsureSlider = QtWidgets.QSlider(self.groupBox_3)
        self.ExporsureSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ExporsureSlider.setObjectName("ExporsureSlider")
        self.horizontalLayout.addWidget(self.ExporsureSlider)
        self.ExposureLabel = QtWidgets.QLabel(self.groupBox_3)
        self.ExposureLabel.setObjectName("ExposureLabel")
        self.horizontalLayout.addWidget(self.ExposureLabel)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GainSlider = QtWidgets.QSlider(self.groupBox_3)
        self.GainSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GainSlider.setObjectName("GainSlider")
        self.horizontalLayout_3.addWidget(self.GainSlider)
        self.GainLabel = QtWidgets.QLabel(self.groupBox_3)
        self.GainLabel.setObjectName("GainLabel")
        self.horizontalLayout_3.addWidget(self.GainLabel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_5.addWidget(self.toolButton)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.detectCurrentBtn = QtWidgets.QPushButton(self.groupBox)
        self.detectCurrentBtn.setObjectName("detectCurrentBtn")
        self.gridLayout.addWidget(self.detectCurrentBtn, 0, 0, 1, 1)
        self.detectAllBtn = QtWidgets.QPushButton(self.groupBox)
        self.detectAllBtn.setObjectName("detectAllBtn")
        self.gridLayout.addWidget(self.detectAllBtn, 0, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_6.setStretch(0, 8)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.resultTab = QtWidgets.QWidget()
        self.resultTab.setObjectName("resultTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.resultTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.resultLayout = QtWidgets.QGridLayout()
        self.resultLayout.setObjectName("resultLayout")
        self.gridLayout_5.addLayout(self.resultLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.resultTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ImgAnalysisLayout = QtWidgets.QGridLayout()
        self.ImgAnalysisLayout.setObjectName("ImgAnalysisLayout")
        self.gridLayout_2.addLayout(self.ImgAnalysisLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1711, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "dPCR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "相机控制"))
        self.label.setText(_translate("MainWindow", "相机曝光："))
        self.ExposureLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "增益："))
        self.GainLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "文件位置："))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox.setTitle(_translate("MainWindow", "检测"))
        self.detectCurrentBtn.setText(_translate("MainWindow", "检测当前"))
        self.detectAllBtn.setText(_translate("MainWindow", "检测所有"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "控制"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultTab), _translate("MainWindow", "结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图像处理"))

