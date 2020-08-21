from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MergerWindow(object):
    def setupUi(self, MergerWindow):
        MergerWindow.setObjectName("MergerWindow")
        MergerWindow.resize(420, 245)
        self.centralwidget = QtWidgets.QWidget(MergerWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pdf_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.pdf_list_widget.setGeometry(QtCore.QRect(5, 5, 410, 190))
        self.pdf_list_widget.setObjectName("pdf_list_widget")

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(20, 200, 55, 20))
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setObjectName("add_button")

        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(80, 200, 75, 20))
        self.remove_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_button.setObjectName("remove_button")

        self.add_folder_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_folder_button.setGeometry(QtCore.QRect(40, 220, 100, 20))
        self.add_folder_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_folder_button.setObjectName("add_folder_button")

        self.output_button = QtWidgets.QPushButton(self.centralwidget)
        self.output_button.setGeometry(QtCore.QRect(185, 200, 105, 25))
        self.output_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.output_button.setObjectName("output_button")

        self.merge_button = QtWidgets.QPushButton(self.centralwidget)
        self.merge_button.setGeometry(QtCore.QRect(320, 200, 80, 25))
        self.merge_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.merge_button.setObjectName("merge_button")

        MergerWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MergerWindow)
        QtCore.QMetaObject.connectSlotsByName(MergerWindow)

    def retranslateUi(self, MergerWindow):
        _translate = QtCore.QCoreApplication.translate
        MergerWindow.setWindowTitle(_translate("MergerWindow", "PDF Merger"))
        self.add_button.setText(_translate("MergerWindow", "Add pdf"))
        self.remove_button.setText(_translate("MergerWindow", "Remove pdf"))
        self.add_folder_button.setText(_translate("MergerWindow", "Add all from folder"))
        self.output_button.setText(_translate("MergerWindow", "Select output folder"))
        self.merge_button.setText(_translate("MergerWindow", "Merge pdfs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MergerWindow = QtWidgets.QMainWindow()
    ui = Ui_MergerWindow()
    ui.setupUi(MergerWindow)
    MergerWindow.show()
    sys.exit(app.exec_())
