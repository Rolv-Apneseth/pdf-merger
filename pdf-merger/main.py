import sys
import os
import PyPDF2
from PyQt5 import QtCore, QtGui, QtWidgets

import assets.merger_window


class Merger(assets.merger_window.Ui_MergerWindow):
    """Adds functionality to ui defined in merger_window.py"""

    def __init__(self):
        self.pdfs = []
        self.output_folder = os.getcwd()

    def merge_pdfs(self, pdfs, output_folder):
        """Final Function which merges given pdfs, and outputs the Mrged.pdf into the selected output folder"""

        # Initialising the file merger from PyPDF2
        merger = PyPDF2.PdfFileMerger()

        # Loops through the pdfs given and adds each in turn to the merger object
        for pdf in pdfs:
            merger.append(pdf)

        # Merger object then used to merge pdf files into one pdf which is then written to the given output folder
        out_path = os.path.join(output_folder, "Merged.pdf")
        merger.write(out_path)

    def choose_file_path(self):
        """QFileDialog pop up allows you to select a file, and that file path is returned"""

        path = QtWidgets.QFileDialog.getOpenFileName()
        return path[0]

    def choose_folder_path(self):
        """QFileDialog pop up allows you to select a folder, and that file path is returned"""

        path = QtWidgets.QFileDialog.getExistingDirectory()
        return path

    def on_clicked_add_button(self):
        """Adds a single chosen item to the list widget and the self.pdfs list"""

        file = self.choose_file_path()

        # Adds selected pdf file to self.pdfs list if it is a pdf file and is not already in self.pdfs
        if file.endswith(".pdf") and file not in self.pdfs:
            self.pdf_list_widget.addItem(file)
            self.pdfs.append(file)

    def on_clicked_remove_button(self):
        """Removes the selected item from the list widget and from the self.pdfs list"""

        row = self.pdf_list_widget.currentRow()

        # If there is a valid item in the list selected, removes this item from the list and from self.pdfs
        if not self.pdf_list_widget.item(row) == None:
            file = self.pdf_list_widget.item(row).text()
            if file in self.pdfs:
                self.pdfs.remove(file)
            self.pdf_list_widget.takeItem(row)

    def on_clicked_add_folder_button(self):
        """Adds all pdf files from a chosen directory to the list widget and to the self.pdfs list. Items added in alphabetical order."""

        folder = self.choose_folder_path()

        # Adds all pdf files from a chosen directory to the list widget and to self.pdfs, if it is a valid directory path
        if os.path.isdir(folder):
            for file in sorted(os.listdir(folder)):
                if file.endswith(".pdf") and file not in self.pdfs:
                    self.pdf_list_widget.addItem(os.path.join(folder, file))
                    self.pdfs.append(file)

    def on_changed_path(self):
        """Changes path displayed on the lineedit at the bottom of the gui to show the updated output path."""

        self.output_path_lineedit.setText(
            os.path.join(self.output_folder, "Merged.pdf"))

    def on_clicked_output_button(self):
        """Sets the self.output_folder to a chosen directory path. Also calls self.on_changed_path."""

        folder = self.choose_folder_path()

        if os.path.isdir(folder):
            self.output_folder = folder

        self.on_changed_path()

    def on_clicked_merge_button(self):
        """Calls self.merge_pdfs function with self.pdfs and self.output_folder, then closes the main window."""

        self.merge_pdfs(self.pdfs, self.output_folder)
        main_window.close()

    def give_functionality(self):
        self.add_button.clicked.connect(self.on_clicked_add_button)
        self.merge_button.clicked.connect(self.on_clicked_merge_button)
        self.output_button.clicked.connect(self.on_clicked_output_button)
        self.remove_button.clicked.connect(self.on_clicked_remove_button)
        self.add_folder_button.clicked.connect(
            self.on_clicked_add_folder_button)
        self.on_changed_path()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Merger()
    ui.setupUi(main_window)
    ui.give_functionality()
    main_window.show()
    sys.exit(app.exec_())
