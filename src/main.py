# PySide6-uic mainwindow.ui -o mainwindow.py
# pip install -r requirements.txt
import os
import sys
import time
from queue import Queue

from scapy.all import *
from scapy.all import IP
from scapy.utils import hexdump
from scapy.arch.common import compile_filter

from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QTreeWidgetItem

from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_sniffer

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.ui = Ui_sniffer()
        self.setWindowTitle("Sniffer")
        self.ui.setupUi(self)
        self.bind()
        self.init_device()
        self.init_packet_list()
        self.init_packet_binary()
        self.packets = []
        self.packet_counter = 0
        self.start_time = 0
        self.sniffer = None
        self.bpf = None
        self.capture_device = None
        self.file_name = ""
        self.ui.filter_button.setEnabled(False)

    def bind(self):
        self.ui.device_list.activated.connect(self.select_device)
        self.ui.start_button.clicked.connect(self.start_capture)
        self.ui.filter_button.clicked.connect(self.filter_pcap)
        self.ui.packet_list.cellPressed.connect(self.show_packet_detail)

    def init_device(self):
        self.ui.device_list.clear()
        for device in get_working_ifaces():
            self.ui.device_list.addItem(device.name)
            print(device)

    def select_device(self,value):
        for device in get_working_ifaces():
            if device.name == value:
                self.capture_device = device

    def init_packet_list(self):
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.ui.packet_list.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.ui.packet_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.packet_list.verticalHeader().setVisible(False)
        self.ui.packet_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    def init_packet_binary(self):
        self.ui.packet_binary.setFontPointSize(14.0)
        self.ui.packet_binary.setReadOnly(True)

    def capture_recall(self,packet):
        if not packet:
            return
        self.packets.append(packet)
        row = self.ui.packet_list.rowCount()
        self.ui.packet_list.insertRow(row)

        self.packet_counter += 1
        self.ui.packet_list.setItem(row,0,QTableWidgetItem(str(self.packet_counter)))

        self.ui.packet_list.setItem(row,1,QTableWidgetItem(str(f"{(time.time()-self.start_time):6f}")))

        if IP in packet:
            self.ui.packet_list.setItem(row,2,QTableWidgetItem(packet[IP].src))
            self.ui.packet_list.setItem(row,3,QTableWidgetItem(packet[IP].dst))
        else:
            self.ui.packet_list.setItem(row,2,QTableWidgetItem(packet.src))
            self.ui.packet_list.setItem(row,3,QTableWidgetItem(packet.dst))         

        self.ui.packet_list.setItem(row,4,QTableWidgetItem(str(len(packet))))

        layer = 0
        while True:
            if packet.getlayer(layer) == None or packet.getlayer(layer).name == "Raw" or packet.getlayer(layer).name == "Padding":
                break
            layer += 1 

        self.ui.packet_list.setItem(row,5,QTableWidgetItem(packet.getlayer(layer-1).name))

        info = str(packet.summary())
        item = QTableWidgetItem(info)
        item.packet = packet
        self.ui.packet_list.setItem(row, 6, item)
    
    def start_capture(self):
        if self.sniffer:
            self.sniffer.stop()
            self.sniffer = None
            self.ui.start_button.setText("Start")
            self.ui.device_list.setEnabled(True)
            self.ui.bpf_filter.setEnabled(True)
            self.ui.filter_button.setEnabled(True)
            self.ui.bpf_filter.clear()
            return

        bpf_exp = self.ui.bpf_filter.text()
        self.sniffer = AsyncSniffer(
            iface=self.capture_device,
            prn=self.capture_recall,
            filter=bpf_exp,
        )
        self.file_name = ""
        self.packet_counter = 0
        self.start_time = time.time()

        self.ui.start_button.setText("Stop")
        self.ui.device_list.setEnabled(False)
        self.ui.bpf_filter.setEnabled(False)
        self.ui.filter_button.setEnabled(False)
        self.ui.packet_list.clearContents()
        self.ui.packet_list.setRowCount(0)
        self.ui.packet_detail.clear()
        self.ui.packet_binary.clear()
        self.sniffer.start()

    def show_packet_detail(self,row,col):
        packet = self.packets[row]
        self.ui.packet_binary.setText(hexdump(packet, dump=True))

        self.ui.packet_detail.clear()
        
        idx = 0
        while True:
            layer = packet.getlayer(idx)
            if layer == None:
                break

            item = QTreeWidgetItem(self.ui.packet_detail)
            item.layer = layer
            item.setText(0,layer.name)

            for k,v in layer.fields.items():
                c = QTreeWidgetItem(item)
                c.setText(0,f"{k}: {v}")
            idx += 1 

    def filter_pcap(self):
        print(self.file_name)
        if self.file_name == "":
            now_time = datetime.now().strftime( "%Y%m%d%H%M%S" )
            self.file_name = "./pcap/data_{0}.pcap".format(now_time)
            o_open_file= PcapWriter(self.file_name, append=True)
            print("write",len(self.packets))
            for packet in self.packets:
                o_open_file.write(packet)

        self.ui.packet_detail.clear()
        self.ui.packet_binary.clear()
        bpf_exp = self.ui.bpf_filter.text()
        self.packet_counter = 0
        self.ui.packet_list.clearContents()
        self.ui.packet_list.setRowCount(0)
        sniff(iface = None,prn = self.capture_recall,filter = bpf_exp, offline = self.file_name)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()