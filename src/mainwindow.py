# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_sniffer(object):
    def setupUi(self, sniffer):
        if not sniffer.objectName():
            sniffer.setObjectName(u"sniffer")
        sniffer.resize(754, 637)
        self.centralwidget = QWidget(sniffer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.device_list = QComboBox(self.centralwidget)
        self.device_list.setObjectName(u"device_list")

        self.gridLayout_5.addWidget(self.device_list, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.packet_list = QTableWidget(self.centralwidget)
        if (self.packet_list.columnCount() < 7):
            self.packet_list.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.packet_list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.packet_list.setObjectName(u"packet_list")

        self.gridLayout_2.addWidget(self.packet_list, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 0, 1, 3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.packet_binary = QTextEdit(self.centralwidget)
        self.packet_binary.setObjectName(u"packet_binary")
        self.packet_binary.setReadOnly(True)

        self.gridLayout_4.addWidget(self.packet_binary, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 4, 0, 1, 3)

        self.bpf_filter = QLineEdit(self.centralwidget)
        self.bpf_filter.setObjectName(u"bpf_filter")

        self.gridLayout_5.addWidget(self.bpf_filter, 1, 1, 1, 1)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout_5.addWidget(self.start_button, 0, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.packet_detail = QTreeWidget(self.centralwidget)
        self.packet_detail.setObjectName(u"packet_detail")

        self.gridLayout_3.addWidget(self.packet_detail, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 3, 0, 1, 3)

        self.filter_button = QPushButton(self.centralwidget)
        self.filter_button.setObjectName(u"filter_button")

        self.gridLayout_5.addWidget(self.filter_button, 1, 2, 1, 1)

        sniffer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(sniffer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 754, 22))
        sniffer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(sniffer)
        self.statusbar.setObjectName(u"statusbar")
        sniffer.setStatusBar(self.statusbar)

        self.retranslateUi(sniffer)

        QMetaObject.connectSlotsByName(sniffer)
    # setupUi

    def retranslateUi(self, sniffer):
        sniffer.setWindowTitle(QCoreApplication.translate("sniffer", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("sniffer", u"Devices", None))
        self.label_2.setText(QCoreApplication.translate("sniffer", u"Filter", None))
        ___qtablewidgetitem = self.packet_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sniffer", u"No.", None));
        ___qtablewidgetitem1 = self.packet_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sniffer", u"Time", None));
        ___qtablewidgetitem2 = self.packet_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sniffer", u"Source", None));
        ___qtablewidgetitem3 = self.packet_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sniffer", u"Desination", None));
        ___qtablewidgetitem4 = self.packet_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("sniffer", u"Length", None));
        ___qtablewidgetitem5 = self.packet_list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("sniffer", u"Protocol", None));
        ___qtablewidgetitem6 = self.packet_list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("sniffer", u"Info", None));
        self.packet_binary.setHtml(QCoreApplication.translate("sniffer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bpf_filter.setText("")
        self.bpf_filter.setPlaceholderText(QCoreApplication.translate("sniffer", u"BPF filter", None))
        self.start_button.setText(QCoreApplication.translate("sniffer", u"Start Capture", None))
        ___qtreewidgetitem = self.packet_detail.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("sniffer", u"Packet Detail Info", None));
        self.filter_button.setText(QCoreApplication.translate("sniffer", u"Filtering", None))
    # retranslateUi

