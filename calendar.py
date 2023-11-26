from base import get_dates
from PyQt6 import QtCore, QtGui, QtWidgets


class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if f'{date}' in get_dates():
            painter.setBrush(QtGui.QColor(200, 150, 150, 25))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = MyCalendar(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(60, 50, 471, 341))
        self.calendar.setObjectName("calendarWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.setCentralWidget(self.centralwidget)
        self.horizontalLayout_3.addWidget(self.calendar)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(250, 0))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 10))
        self.label_2.setText("")
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.events = QtWidgets.QLabel(parent=self.centralwidget)
        self.events.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.events.sizePolicy().hasHeightForWidth())
        self.events.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.events.setFont(font)
        self.events.setTabletTracking(False)
        self.events.setAcceptDrops(False)
        self.events.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.events.setScaledContents(False)
        self.events.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.events.setWordWrap(False)
        self.events.setObjectName("events")
        self.verticalLayout.addWidget(self.events)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 500))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.addevent = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addevent.setMinimumSize(QtCore.QSize(200, 0))
        self.addevent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addevent.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.addevent.setObjectName("addevent")
        self.verticalLayout_3.addWidget(self.addevent)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back.setMinimumSize(QtCore.QSize(100, 0))
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.events.setText(_translate("MainWindow", "Events"))
        self.addevent.setText(_translate("MainWindow", "Add event"))
        self.back.setText(_translate("MainWindow", "back"))