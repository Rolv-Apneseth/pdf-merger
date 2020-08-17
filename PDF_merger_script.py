import PyPDF2
import sys
import glob

inputs = sys.argv[1:]


def merge(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("Merged.pdf")


if str(sys.argv[1]) == "all":
    pdfs = glob.iglob("*.pdf")
else:
    pdfs = sys.argv[1:]
    for pdf in pdfs:
        if not pdf.endswith(".pdf"):
            pdfs.remove(pdf)

try:
    merge(pdfs)
except:
    print("There was a problem merging the files. Make sure all files specified are .pdf files and they all exist in the same directory as the PDF_merger_script.py")


