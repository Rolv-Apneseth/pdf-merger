import PyPDF2
import sys
import glob

inputs = sys.argv[1:]


def merge(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("Merged.pdf")

def main(inputs):

    if str(inputs[1]) == "all":
        pdfs = glob.iglob("*.pdf")
    else:
        pdfs = inputs[1:]
        for pdf in pdfs:
            if not pdf.endswith(".pdf"):
                pdfs.remove(pdf)

    try:
        if len(pdfs) > 1:
            merge(pdfs)
        else:
            print("There were not 2 or more valid pdf files specified.")
    except:
        print("There was a problem merging the files. Make sure all files specified are .pdf files and they all exist in the same directory as the PDF_merger_script.py")


if __name__ == "__main__":
    main(inputs)
