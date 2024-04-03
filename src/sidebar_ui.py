# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 604)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/thunderstorm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(".\\icon/thunderstorm.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/home_color.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.view3d_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.view3d_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view3d_2.setIcon(icon2)
        self.view3d_2.setIconSize(QtCore.QSize(25, 25))
        self.view3d_2.setCheckable(True)
        self.view3d_2.setAutoExclusive(True)
        self.view3d_2.setObjectName("view3d_2")
        self.verticalLayout_2.addWidget(self.view3d_2)
        self.view2d_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.view2d_2.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/2d_color.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view2d_2.setIcon(icon3)
        self.view2d_2.setIconSize(QtCore.QSize(25, 25))
        self.view2d_2.setCheckable(True)
        self.view2d_2.setAutoExclusive(True)
        self.view2d_2.setObjectName("view2d_2")
        self.verticalLayout_2.addWidget(self.view2d_2)
        self.other_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.other_2.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/more.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.other_2.setIcon(icon4)
        self.other_2.setIconSize(QtCore.QSize(25, 25))
        self.other_2.setCheckable(True)
        self.other_2.setAutoExclusive(True)
        self.other_2.setObjectName("other_2")
        self.verticalLayout_2.addWidget(self.other_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_btn_2.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/switch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/thunderstorm.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\icon/home_color.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon6)
        self.home_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.view3d_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.view3d_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\icon/3d-cube.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/3d-cube.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.view3d_1.setIcon(icon7)
        self.view3d_1.setIconSize(QtCore.QSize(25, 25))
        self.view3d_1.setCheckable(True)
        self.view3d_1.setAutoExclusive(True)
        self.view3d_1.setObjectName("view3d_1")
        self.verticalLayout.addWidget(self.view3d_1)
        self.view2d_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.view2d_1.setText("")
        self.view2d_1.setIcon(icon3)
        self.view2d_1.setIconSize(QtCore.QSize(25, 25))
        self.view2d_1.setCheckable(True)
        self.view2d_1.setAutoExclusive(True)
        self.view2d_1.setObjectName("view2d_1")
        self.verticalLayout.addWidget(self.view2d_1)
        self.other_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.other_1.setText("")
        self.other_1.setIcon(icon4)
        self.other_1.setIconSize(QtCore.QSize(25, 25))
        self.other_1.setCheckable(True)
        self.other_1.setAutoExclusive(True)
        self.other_1.setObjectName("other_1")
        self.verticalLayout.addWidget(self.other_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(25, 25))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/main-menu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon8)
        self.change_btn.setIconSize(QtCore.QSize(25, 25))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.IsGrid = QtWidgets.QCheckBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IsGrid.sizePolicy().hasHeightForWidth())
        self.IsGrid.setSizePolicy(sizePolicy)
        self.IsGrid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IsGrid.setObjectName("IsGrid")
        self.gridLayout_9.addWidget(self.IsGrid, 0, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 0, 0, 1, 1)
        self.fileBox = QtWidgets.QComboBox(self.page_2)
        self.fileBox.setEditable(True)
        self.fileBox.setObjectName("fileBox")
        self.fileBox.addItem("")
        self.fileBox.addItem("")
        self.fileBox.addItem("")
        self.fileBox.addItem("")
        self.fileBox.addItem("")
        self.gridLayout_9.addWidget(self.fileBox, 1, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 0, 2, 1, 1)
        self.modeBox = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBox.sizePolicy().hasHeightForWidth())
        self.modeBox.setSizePolicy(sizePolicy)
        self.modeBox.setEditable(True)
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.gridLayout_9.addWidget(self.modeBox, 0, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 1, 4, 1, 1)
        self.radarBox = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radarBox.sizePolicy().hasHeightForWidth())
        self.radarBox.setSizePolicy(sizePolicy)
        self.radarBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radarBox.setEditable(True)
        self.radarBox.setObjectName("radarBox")
        self.radarBox.addItem("")
        self.radarBox.addItem("")
        self.radarBox.addItem("")
        self.radarBox.addItem("")
        self.radarBox.addItem("")
        self.gridLayout_9.addWidget(self.radarBox, 0, 1, 1, 1)
        self.dateBox = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBox.sizePolicy().hasHeightForWidth())
        self.dateBox.setSizePolicy(sizePolicy)
        self.dateBox.setEditable(True)
        self.dateBox.setObjectName("dateBox")
        self.gridLayout_9.addWidget(self.dateBox, 0, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_9)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.page_2)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_6.addWidget(self.openGLWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 2, 0, 1, 1)
        self.threshHold = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshHold.sizePolicy().hasHeightForWidth())
        self.threshHold.setSizePolicy(sizePolicy)
        self.threshHold.setObjectName("threshHold")
        self.gridLayout_11.addWidget(self.threshHold, 0, 4, 1, 1)
        self.slider_3d_x = QtWidgets.QSlider(self.page_2)
        self.slider_3d_x.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.slider_3d_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_3d_x.setObjectName("slider_3d_x")
        self.gridLayout_11.addWidget(self.slider_3d_x, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)
        self.slider_3d_y = QtWidgets.QSlider(self.page_2)
        self.slider_3d_y.setOrientation(QtCore.Qt.Horizontal)
        self.slider_3d_y.setObjectName("slider_3d_y")
        self.gridLayout_11.addWidget(self.slider_3d_y, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 4, 1, 1)
        self.slider_3d_z = QtWidgets.QSlider(self.page_2)
        self.slider_3d_z.setOrientation(QtCore.Qt.Horizontal)
        self.slider_3d_z.setObjectName("slider_3d_z")
        self.gridLayout_11.addWidget(self.slider_3d_z, 2, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_17.addWidget(self.comboBox_2, 0, 5, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_17.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_17.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_17.addWidget(self.checkBox_2, 0, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_17.addWidget(self.label_15, 0, 2, 1, 1)
        self.radarBox_2 = QtWidgets.QComboBox(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radarBox_2.sizePolicy().hasHeightForWidth())
        self.radarBox_2.setSizePolicy(sizePolicy)
        self.radarBox_2.setObjectName("radarBox_2")
        self.gridLayout_17.addWidget(self.radarBox_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_17.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_17.addWidget(self.label_19, 1, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_17.addWidget(self.comboBox_3, 1, 5, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.page_3)
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.verticalLayout_10.addWidget(self.openGLWidget_2)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.fileBox.setCurrentIndex(0)
        self.modeBox.setCurrentIndex(-1)
        self.radarBox.setCurrentIndex(-1)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.view3d_1.toggled['bool'].connect(self.view3d_2.setChecked) # type: ignore
        self.view2d_1.toggled['bool'].connect(self.view2d_2.setChecked) # type: ignore
        self.other_1.toggled['bool'].connect(self.other_2.setChecked) # type: ignore
        self.view3d_2.toggled['bool'].connect(self.view3d_1.setChecked) # type: ignore
        self.view2d_2.toggled['bool'].connect(self.view2d_1.setChecked) # type: ignore
        self.other_2.toggled['bool'].connect(self.other_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.home_btn_1, self.home_btn_2)
        MainWindow.setTabOrder(self.home_btn_2, self.view3d_2)
        MainWindow.setTabOrder(self.view3d_2, self.view2d_2)
        MainWindow.setTabOrder(self.view2d_2, self.other_2)
        MainWindow.setTabOrder(self.other_2, self.exit_btn_1)
        MainWindow.setTabOrder(self.exit_btn_1, self.other_1)
        MainWindow.setTabOrder(self.other_1, self.view3d_1)
        MainWindow.setTabOrder(self.view3d_1, self.slider_3d_y)
        MainWindow.setTabOrder(self.slider_3d_y, self.change_btn)
        MainWindow.setTabOrder(self.change_btn, self.view2d_1)
        MainWindow.setTabOrder(self.view2d_1, self.slider_3d_z)
        MainWindow.setTabOrder(self.slider_3d_z, self.slider_3d_x)
        MainWindow.setTabOrder(self.slider_3d_x, self.threshHold)
        MainWindow.setTabOrder(self.threshHold, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.radarBox)
        MainWindow.setTabOrder(self.radarBox, self.modeBox)
        MainWindow.setTabOrder(self.modeBox, self.fileBox)
        MainWindow.setTabOrder(self.fileBox, self.IsGrid)
        MainWindow.setTabOrder(self.IsGrid, self.exit_btn_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thesis Titian "))
        self.logo_label_3.setText(_translate("MainWindow", "TITAN"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.view3d_2.setText(_translate("MainWindow", "3D View"))
        self.view2d_2.setText(_translate("MainWindow", "2D View"))
        self.other_2.setText(_translate("MainWindow", "Others"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Thesis 232"))
        self.label_4.setText(_translate("MainWindow", "Home Page"))
        self.IsGrid.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>grid file or not</p></body></html>"))
        self.IsGrid.setText(_translate("MainWindow", "IS GRID FILE"))
        self.label_13.setText(_translate("MainWindow", "RADAR"))
        self.fileBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>choose file</p></body></html>"))
        self.fileBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>choose file</p></body></html>"))
        self.fileBox.setItemText(0, _translate("MainWindow", "All file"))
        self.fileBox.setItemText(1, _translate("MainWindow", "File 2"))
        self.fileBox.setItemText(2, _translate("MainWindow", "File 3"))
        self.fileBox.setItemText(3, _translate("MainWindow", "File 4"))
        self.fileBox.setItemText(4, _translate("MainWindow", "File 5"))
        self.label_14.setText(_translate("MainWindow", "DATE"))
        self.modeBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>mode name</p></body></html>"))
        self.modeBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>mode name</p></body></html>"))
        self.modeBox.setItemText(0, _translate("MainWindow", "Mode 1"))
        self.modeBox.setItemText(1, _translate("MainWindow", "Mode 2"))
        self.modeBox.setItemText(2, _translate("MainWindow", "Mode 3"))
        self.modeBox.setItemText(3, _translate("MainWindow", "Mode 4"))
        self.modeBox.setItemText(4, _translate("MainWindow", "Mode 5"))
        self.label_16.setText(_translate("MainWindow", "MODE"))
        self.label_17.setText(_translate("MainWindow", "FILE"))
        self.radarBox.setToolTip(_translate("MainWindow", "Radar name"))
        self.radarBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>radar name</p><p><br/></p></body></html>"))
        self.radarBox.setItemText(0, _translate("MainWindow", "Name radar 1"))
        self.radarBox.setItemText(1, _translate("MainWindow", "Name radar 2"))
        self.radarBox.setItemText(2, _translate("MainWindow", "Name radar 3"))
        self.radarBox.setItemText(3, _translate("MainWindow", "Name radar 4"))
        self.radarBox.setItemText(4, _translate("MainWindow", "Name radar 5"))
        self.dateBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>DD/MM/YY</p><p><br/></p></body></html>"))
        self.dateBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>DD/MM/YY</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Z aixs"))
        self.threshHold.setToolTip(_translate("MainWindow", "<html><head/><body><p>press enter to confirm thresh hold</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "X axis"))
        self.label_5.setText(_translate("MainWindow", "Threshold"))
        self.label_3.setText(_translate("MainWindow", "Y axis"))
        self.label_12.setText(_translate("MainWindow", "Others opt"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Others"))
        self.label_8.setText(_translate("MainWindow", "Customers Page"))
        self.label_9.setText(_translate("MainWindow", "Search Page"))
        self.label_10.setText(_translate("MainWindow", "User Page"))
import resource_rc
