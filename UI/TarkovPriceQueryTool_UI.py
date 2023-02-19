# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TarkovPriceQueryTool_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EFTPQ_UI(object):
    def setupUi(self, EFTPQ_UI):
        if not EFTPQ_UI.objectName():
            EFTPQ_UI.setObjectName(u"EFTPQ_UI")
        EFTPQ_UI.resize(850, 793)
        EFTPQ_UI.setMinimumSize(QSize(850, 793))
        EFTPQ_UI.setMaximumSize(QSize(850, 793))
        EFTPQ_UI.setBaseSize(QSize(790, 800))
        EFTPQ_UI.setMouseTracking(False)
        EFTPQ_UI.setTabletTracking(False)
        icon = QIcon()
        icon.addFile(u"./resource/eft_logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        EFTPQ_UI.setWindowIcon(icon)
        EFTPQ_UI.setAutoFillBackground(False)
        self.label_server_url = QLabel(EFTPQ_UI)
        self.label_server_url.setObjectName(u"label_server_url")
        self.label_server_url.setGeometry(QRect(11, 10, 60, 30))
        self.label_server_url.setFrameShape(QFrame.Box)
        self.label_server_url.setTextFormat(Qt.AutoText)
        self.label_server_url.setAlignment(Qt.AlignCenter)
        self.comboBox_server_url = QComboBox(EFTPQ_UI)
        self.comboBox_server_url.setObjectName(u"comboBox_server_url")
        self.comboBox_server_url.setGeometry(QRect(70, 10, 421, 30))
        self.comboBox_server_url.setEditable(True)
        self.comboBox_server_url.setFrame(True)
        self.label_search = QLabel(EFTPQ_UI)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setGeometry(QRect(11, 50, 60, 30))
        self.label_search.setFrameShape(QFrame.Box)
        self.label_search.setTextFormat(Qt.AutoText)
        self.label_search.setAlignment(Qt.AlignCenter)
        self.lineEdit_search = QLineEdit(EFTPQ_UI)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(70, 50, 420, 30))
        self.tableWidget_item_list = QTableWidget(EFTPQ_UI)
        if (self.tableWidget_item_list.columnCount() < 8):
            self.tableWidget_item_list.setColumnCount(8)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.tableWidget_item_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.tableWidget_item_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget_item_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font);
        self.tableWidget_item_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget_item_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget_item_list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget_item_list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget_item_list.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget_item_list.rowCount() < 1):
            self.tableWidget_item_list.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_item_list.setItem(0, 0, __qtablewidgetitem8)
        self.tableWidget_item_list.setObjectName(u"tableWidget_item_list")
        self.tableWidget_item_list.setGeometry(QRect(10, 90, 831, 651))
        self.tableWidget_item_list.setMinimumSize(QSize(831, 651))
        self.tableWidget_item_list.setMaximumSize(QSize(831, 651))
        self.tableWidget_item_list.setIconSize(QSize(64, 64))
        self.tableWidget_item_list.setShowGrid(True)
        self.tableWidget_item_list.setGridStyle(Qt.SolidLine)
        self.tableWidget_item_list.setSortingEnabled(False)
        self.tableWidget_item_list.setWordWrap(True)
        self.tableWidget_item_list.setCornerButtonEnabled(True)
        self.tableWidget_item_list.setRowCount(1)
        self.tableWidget_item_list.horizontalHeader().setVisible(True)
        self.tableWidget_item_list.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_item_list.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget_item_list.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_item_list.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_item_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_item_list.verticalHeader().setVisible(False)
        self.tableWidget_item_list.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_item_list.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_item_list.verticalHeader().setDefaultSectionSize(70)
        self.tableWidget_item_list.verticalHeader().setHighlightSections(True)
        self.tableWidget_item_list.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_item_list.verticalHeader().setStretchLastSection(False)
        self.pushButton_search = QPushButton(EFTPQ_UI)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(500, 50, 121, 30))
        self.comboBox_lang = QComboBox(EFTPQ_UI)
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.setObjectName(u"comboBox_lang")
        self.comboBox_lang.setGeometry(QRect(500, 10, 121, 30))
        self.comboBox_lang.setEditable(True)
        self.comboBox_lang.setFrame(True)
        self.label_tool_version = QLabel(EFTPQ_UI)
        self.label_tool_version.setObjectName(u"label_tool_version")
        self.label_tool_version.setGeometry(QRect(92, 750, 72, 15))
        self.label_server_version = QLabel(EFTPQ_UI)
        self.label_server_version.setObjectName(u"label_server_version")
        self.label_server_version.setGeometry(QRect(92, 770, 85, 15))
        self.label_tool_version_x = QLabel(EFTPQ_UI)
        self.label_tool_version_x.setObjectName(u"label_tool_version_x")
        self.label_tool_version_x.setGeometry(QRect(164, 750, 411, 16))
        self.label_server_version_x = QLabel(EFTPQ_UI)
        self.label_server_version_x.setObjectName(u"label_server_version_x")
        self.label_server_version_x.setGeometry(QRect(180, 770, 391, 16))
        self.pushButton_github_logo = QPushButton(EFTPQ_UI)
        self.pushButton_github_logo.setObjectName(u"pushButton_github_logo")
        self.pushButton_github_logo.setGeometry(QRect(12, 752, 30, 30))
        self.pushButton_github_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_github_logo.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u"./resource/github_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_github_logo.setIcon(icon1)
        self.pushButton_github_logo.setIconSize(QSize(28, 28))
        self.pushButton_bilibili_logo = QPushButton(EFTPQ_UI)
        self.pushButton_bilibili_logo.setObjectName(u"pushButton_bilibili_logo")
        self.pushButton_bilibili_logo.setGeometry(QRect(51, 752, 30, 30))
        self.pushButton_bilibili_logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_bilibili_logo.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u"./resource/bilibili_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_bilibili_logo.setIcon(icon2)
        self.pushButton_bilibili_logo.setIconSize(QSize(28, 28))
        self.pushButton_toTarkovMarket = QPushButton(EFTPQ_UI)
        self.pushButton_toTarkovMarket.setObjectName(u"pushButton_toTarkovMarket")
        self.pushButton_toTarkovMarket.setGeometry(QRect(580, 750, 260, 32))
        self.pushButton_toTarkovMarket.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_toTarkovMarket.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.comboBox_server_url.raise_()
        self.lineEdit_search.raise_()
        self.label_server_url.raise_()
        self.label_search.raise_()
        self.tableWidget_item_list.raise_()
        self.pushButton_search.raise_()
        self.comboBox_lang.raise_()
        self.label_tool_version.raise_()
        self.label_server_version.raise_()
        self.label_tool_version_x.raise_()
        self.label_server_version_x.raise_()
        self.pushButton_github_logo.raise_()
        self.pushButton_bilibili_logo.raise_()
        self.pushButton_toTarkovMarket.raise_()

        # 自定义
        self.tableWidget_item_list.setColumnWidth(0, 70)
        self.tableWidget_item_list.setColumnWidth(1, 150)
        self.tableWidget_item_list.setColumnWidth(2, 120)
        self.tableWidget_item_list.setColumnWidth(3, 120)
        self.tableWidget_item_list.setColumnWidth(4, 120)
        self.tableWidget_item_list.setColumnWidth(5, 120)
        self.tableWidget_item_list.setColumnWidth(6, 120)
        self.tableWidget_item_list.setColumnWidth(7, 250)
        self.retranslateUi(EFTPQ_UI)

        QMetaObject.connectSlotsByName(EFTPQ_UI)
    # setupUi
    def retranslateUi(self, EFTPQ_UI):
        EFTPQ_UI.setWindowTitle(QCoreApplication.translate("EFTPQ_UI", u"\u9003\u79bb\u5854\u79d1\u592b\u5728\u7ebf\u8be2\u4ef7 - Made by JOZA", None))
        self.label_server_url.setText(QCoreApplication.translate("EFTPQ_UI", u"\u670d\u52a1\uff1a", None))
        self.comboBox_server_url.setPlaceholderText(QCoreApplication.translate("EFTPQ_UI", u"\u9009\u62e9\u63d0\u4f9b\u670d\u52a1\u63d0\u4f9b\u8005...", None))
        self.label_search.setText(QCoreApplication.translate("EFTPQ_UI", u"\u641c\u7d22\uff1a", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("EFTPQ_UI", u"\u8f93\u5165\u7269\u54c1\u540d\u79f0...", None))
        ___qtablewidgetitem = self.tableWidget_item_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EFTPQ_UI", u"\u7269\u54c1", None));
        ___qtablewidgetitem1 = self.tableWidget_item_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EFTPQ_UI", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_item_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EFTPQ_UI", u"\u8df3\u86a4\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.tableWidget_item_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EFTPQ_UI", u"\u5546\u4eba\u4ef7\u683c", None));
        ___qtablewidgetitem4 = self.tableWidget_item_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EFTPQ_UI", u"\u57fa\u7840\u4ef7\u683c", None));
        ___qtablewidgetitem5 = self.tableWidget_item_list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EFTPQ_UI", u"24h\u5747\u4ef7", None));
        ___qtablewidgetitem6 = self.tableWidget_item_list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EFTPQ_UI", u"7d\u5747\u4ef7", None));
        ___qtablewidgetitem7 = self.tableWidget_item_list.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EFTPQ_UI", u"\u66f4\u65b0\u65f6\u95f4", None));

        __sortingEnabled = self.tableWidget_item_list.isSortingEnabled()
        self.tableWidget_item_list.setSortingEnabled(False)
        self.tableWidget_item_list.setSortingEnabled(__sortingEnabled)

        self.pushButton_search.setText(QCoreApplication.translate("EFTPQ_UI", u"\u641c\u7d22", None))
        self.comboBox_lang.setItemText(0, QCoreApplication.translate("EFTPQ_UI", u"cn", None))
        self.comboBox_lang.setItemText(1, QCoreApplication.translate("EFTPQ_UI", u"en", None))
        self.comboBox_lang.setItemText(2, QCoreApplication.translate("EFTPQ_UI", u"ru", None))
        self.comboBox_lang.setItemText(3, QCoreApplication.translate("EFTPQ_UI", u"de", None))
        self.comboBox_lang.setItemText(4, QCoreApplication.translate("EFTPQ_UI", u"fr", None))
        self.comboBox_lang.setItemText(5, QCoreApplication.translate("EFTPQ_UI", u"es", None))
        self.comboBox_lang.setItemText(6, QCoreApplication.translate("EFTPQ_UI", u"cz", None))
        self.comboBox_lang.setItemText(7, QCoreApplication.translate("EFTPQ_UI", u"hu", None))
        self.comboBox_lang.setItemText(8, QCoreApplication.translate("EFTPQ_UI", u"tr", None))

        self.comboBox_lang.setPlaceholderText("")
        self.label_tool_version.setText(QCoreApplication.translate("EFTPQ_UI", u"\u5de5\u5177\u7248\u672c:", None))
        self.label_server_version.setText(QCoreApplication.translate("EFTPQ_UI", u"\u670d\u52a1\u5668\u7248\u672c:", None))
        self.label_tool_version_x.setText(QCoreApplication.translate("EFTPQ_UI", u"-", None))
        self.label_server_version_x.setText(QCoreApplication.translate("EFTPQ_UI", u"-", None))
        self.pushButton_github_logo.setText("")
        self.pushButton_bilibili_logo.setText("")
        self.pushButton_toTarkovMarket.setText(QCoreApplication.translate("EFTPQ_UI", u"\u6570\u636e\u6765\u6e90: tarkov-market.com", None))
    # retranslateUi

