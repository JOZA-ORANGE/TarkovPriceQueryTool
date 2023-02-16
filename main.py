import sys

from requests import get
import json
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtCore import Qt,  QByteArray, QSize
from UI.TarkovPriceQueryTool_UI import Ui_EFTPQ_UI
from function.UnimportantFunction import *
from threading import  Thread
from time import sleep

VERSION = "[client]0.1.2"
BASEURL = "http://server.eft.joza.fun"

class AppUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EFTPQ_UI()
        self.ui.setupUi(self)
        self.ui.pushButton_search.setEnabled(False)
        self.ui.label_tool_version_x.setText(VERSION)
        self.ui.comboBox_server_url.setCurrentText(BASEURL)

        thread_getNewVersion = Thread(target=self.getNewVersion,args=())
        thread_getNewVersion.start()

        # 点击按钮跳转
        self.ui.pushButton_github_logo.clicked.connect(toGithub)
        self.ui.pushButton_bilibili_logo.clicked.connect(toBilibili)
        self.ui.pushButton_toTarkovMarket.clicked.connect(toTarkovMarket)
        self.ui.pushButton_search.clicked.connect(self.threadFunc)

    # 获取公告
    def getNotice(self):
        pass

    # 启动更新线程
    def getNewVersion(self):
        self.getServerVersion()
        self.upgradeInfo()

    # 获取服务端版本号
    def getServerVersion(self):
        url = self.ui.comboBox_server_url.currentText()
        url = url + "/getServerVersion"
        try:
            res = get(url=url)
            if (res.status_code == 200):
                jsondata = json.loads(res.text)
                # 启用搜索按钮
                self.ui.pushButton_search.setEnabled(True)
                self.ui.label_server_version_x.setText(jsondata['ServerVersion'])
            else:
                self.ui.pushButton_search.setEnabled(False)
                self.ui.label_server_version_x.setText(" ! 获取版本失败(code:"+ res.status_code +")")
        except:
            self.ui.pushButton_search.setEnabled(False)
            self.ui.label_server_version_x.setText(" ! 无法连接服务器")





    # 获取更新信息
    def upgradeInfo(self):
        url = self.ui.comboBox_server_url.currentText()
        url = url + "/upgradeInfo"
        try:
            res = get(url=url)
            if (res.status_code == 200):
                self.ui.pushButton_search.setEnabled(True)
                jsondata = json.loads(res.text)
                if (VERSION != jsondata['clientVersion']):
                    self.ui.label_tool_version_x.setText(VERSION + " <有更新>" + jsondata['clientVersion'])
            else:
                self.ui.label_tool_version_x.setText(VERSION + " ! 获取更新失败(code:"+ res.status_code +")")
        except:
            self.ui.label_tool_version_x.setText(VERSION + " ! 无法连接服务器")


    # 新线程入口函数
    def threadFunc(self):
        self.ui.pushButton_search.setEnabled(False)
        self.ui.pushButton_search.setText("...")
        thread = Thread(target=self.searchItem,
                        args=()
                        )
        thread.start()

    # 锁定按钮
    def buttonLock(self):
        self.ui.pushButton_search.setEnabled(False)
        for i in range(5):
            self.ui.pushButton_search.setText(str(5-i))
            sleep(1)
        self.ui.pushButton_search.setText("搜索")
        self.ui.pushButton_search.setEnabled(True)

    # 请求ICON线程
    def getICON(self,url,i):
        res = get(url)
        bytedata = QByteArray()
        bytedata.append(res.content)
        pixmap = QPixmap()
        pixmap.loadFromData(bytedata.data())
        item = QTableWidgetItem()
        item.setIcon(QIcon(pixmap))
        item.setFlags(Qt.ItemIsEnabled)
        self.ui.tableWidget_item_list.setIconSize(QSize(64, 64))
        self.ui.tableWidget_item_list.setItem(i, 0, item)


    # 请求api搜索物品
    def searchItem(self):
        self.ui.tableWidget_item_list.setRowCount(0)
        params = {
            "itemName": self.ui.lineEdit_search.text(),
            "lang": self.ui.comboBox_lang.currentText()
        }
        url = self.ui.comboBox_server_url.currentText()
        url = url + "/getItemPrice"
        res = get(url=url, params=params)

        jsondata = json.loads(res.text)
        LEN = len(jsondata)
        if(len(jsondata)>=15):
            LEN = 15

        for i in range(LEN):
            print(i)
            self.ui.tableWidget_item_list.insertRow(i)
            # ----------------------------------------------
            thread_geticon = Thread(target=self.getICON,
                            args=(jsondata[i]['icon'],i)
                            )
            thread_geticon.start()
            # ----------------------------------------------
            item = QTableWidgetItem(jsondata[i]['name'])
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 1, item)
            # ----------------------------------------------
            item = QTableWidgetItem(str(jsondata[i]['price']))
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 2, item)
            # ----------------------------------------------
            item = QTableWidgetItem(str(jsondata[i]['basePrice']))
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 3, item)
            # ----------------------------------------------
            item = QTableWidgetItem(str(jsondata[i]['avg24hPrice']))
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 4, item)
            # ----------------------------------------------
            item = QTableWidgetItem(str(jsondata[i]['avg7daysPrice']))
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 5, item)
            # ----------------------------------------------
            item = QTableWidgetItem(jsondata[i]['updated'])
            item.setFlags(Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_item_list.setItem(i, 6, item)
        thread1 = Thread(target=self.buttonLock,
                        args=()
                        )
        thread1.start()


    # 获取物品价格走势
    def getPriceTrend(self):
        pass


if __name__ == "__main__":
    app = QApplication([])

    window = AppUI()
    window.show()

    sys.exit(app.exec_())