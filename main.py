import os
from PyPDF2 import PdfMerger
merger = PdfMerger()
folder_path=os.getcwd()
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        merger.append(filename)
merger.write("Final pdf.pdf")
merger.close()
