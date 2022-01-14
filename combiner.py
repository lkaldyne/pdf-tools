import os
from PyPDF2 import PdfFileWriter, PdfFileReader

input_dir = "input"
output_dir = "output"
output = PdfFileWriter()


for filename in sorted(os.listdir(input_dir)):
    f = os.path.join(input_dir, filename)
    # checking if it is a PDF file
    if os.path.isfile(f) and filename.endswith("pdf"):
        infile = PdfFileReader(f, 'rb')

        num_pages = infile.getNumPages()
        for i in range(num_pages):
            p = infile.getPage(i)
            output.addPage(p)

with open(os.path.join(output_dir, "merged.pdf"), 'wb') as fo:
    output.write(fo)