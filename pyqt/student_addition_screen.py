# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/student_addition_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
sys.path.insert(0, os.path.abspath(__file__ + "/../../"))
from modules.api.qr_handler import QrHandler

class AdditionScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.callback = None
        self.class_id = None

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.student_name_textbox = QtWidgets.QLineEdit()
        self.student_name_textbox.setObjectName("student_name_textbox")
        self.horizontalLayout_2.addWidget(self.student_name_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.student_id_textbox = QtWidgets.QLineEdit()
        self.student_id_textbox.setObjectName("student_id_textbox")
        self.horizontalLayout_3.addWidget(self.student_id_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.add_student_button = QtWidgets.QPushButton()
        self.add_student_button.clicked.connect(self.add_student)
        self.add_student_button.setObjectName("add_student_button")
        self.verticalLayout.addWidget(self.add_student_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.label.setText("Student Name")
        self.label_2.setText("Student ID")
        self.add_student_button.setText("Add Student")
        self.setLayout(self.horizontalLayout)
    def set_callback(self, callback):
        self.callback = callback
    def add_student(self):
        print("student adding process")
        student_name = self.student_name_textbox.text()
        student_id = self.student_id_textbox.text()
        if(student_name.replace(" ", "") == "" or student_id.replace(" ", "") == ""):
                return
        self.callback(student_name, student_id,self.class_id)
        self.student_name_textbox.setText("")
        self.student_id_textbox.setText("")
        self.hide()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())