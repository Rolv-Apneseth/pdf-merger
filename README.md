# pdf-merger
 Simple program to merge pdf files together, with a gui made in pyqt5. One of my first programs.

## What I learned
* Building GUI's using PyQt5 and Qt designer
* Filtering different file types to only target PDF files
* Use of OOP
* Merging of PDF files using PyPDF2

## Installation
1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/).
2. Clone the repository by opening your command line/terminal and run: ```git clone https://github.com/Rolv-Apneseth/pdf-merger.git```
    * Note: if you don't have git, it can be downloaded from [here](https://git-scm.com/downloads).
3. Install the requirements for the program.
    * In your terminal, navigate to the cloned directory and run: ```python3 -m pip install -r requirements.txt```
4. To run the actual program, navigate further into the pdf-merger folder and run: ```python3 main.py```

## Usage
1. Add PDFs either individually by clicking either add pdf or add all from folder. This will add the PDF(s) path to the list displayed
    * Please note that the order in which the pdfs are added to the list is important since this is the order they will be merged in.
2. To remove any PDF you didn't mean to add, select the pdf path and click on remove pdf
3. Select an output folder, where the merged pdf will be placed. This can be done by clicking on select output folder
    * The path under Current output path will be changed. Note that you can also edit the name of the .pdf file itself at the end of the full folder path
4. When all the pdfs you want merged are selected, click on merge pdfs

Alternatively, you can run ```python3 assets/pdf_merger_script.py path/1.pdf path/2.pdf``` in the terminal, giving the pdf file full path names (remember to switch \ for / as a \ is an escape character) as arguments, or give argument "all" to merge all pdfs in the current working directory.
