from PyQt5 import QtWidgets,uic
from PyQt5.QtGui import QPixmap
import sys
import os
from roll_functions import *
class roll(QtWidgets.QWidget):



    def __init__(self):
        super(roll, self).__init__()
        uic.loadUi('roll.ui',self)
        self.pushButton.clicked.connect(self.roll_dice)
    def roll_dice(self):
        first_number=random()
        self.pixmap = QPixmap('dice_{}.png'.format(first_number))
        self.label.setPixmap(self.pixmap)
        second_number=random()
        self.pixmap_2 = QPixmap('dice_{}.png'.format(second_number))
        self.label_4.setPixmap(self.pixmap_2)
        total_point_pc=first_number+second_number
        #-----------------------------------------user
        third_number=random()
        self.pixmap = QPixmap('dice_{}.png'.format(third_number))
        self.label_2.setPixmap(self.pixmap)
        fourth_number=random()
        self.pixmap_2 = QPixmap('dice_{}.png'.format(fourth_number))
        self.label_3.setPixmap(self.pixmap_2)
        total_point_user=third_number+fourth_number
        if total_point_user>total_point_pc:
            self.label_8.setText("Winn")
            self.label_7.setText("To Lose")
        elif total_point_user<total_point_pc:
            self.label_7.setText("Winn")
            self.label_8.setText("To Lose")
        elif total_point_user==total_point_pc:
            self.label_8.setText("Equal Try Again...")
            self.label_7.setText("Equal Try Again...")


app = QtWidgets.QApplication(sys.argv)
window = roll()
window.show()
app.exec_()
