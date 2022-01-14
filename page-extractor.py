import os
from PyPDF2 import PdfFileWriter, PdfFileReader
pages = [int(pagenumber.strip()) - 1 for pagenumber in input("Enter Pages of Interest: ").split(",")]
do_keep = True if input("Keep or Remove the selected pages? ") == "Keep" else False

input_dir = "input"
output_dir = "output"

for filename in os.listdir(input_dir):
    f = os.path.join(input_dir, filename)
    # checking if it is a PDF file
    if os.path.isfile(f) and filename.endswith("pdf"):
        infile = PdfFileReader(f, 'rb')
        output = PdfFileWriter()

        if do_keep:
            for i in pages:
                p = infile.getPage(i)
                output.addPage(p)
        else:
            num_pages = infile.getNumPages()
            for i in range(num_pages):
                if i not in pages:
                    p = infile.getPage(i)
                    output.addPage(p)

        with open(os.path.join(output_dir, filename), 'wb') as fo:
            output.write(fo)