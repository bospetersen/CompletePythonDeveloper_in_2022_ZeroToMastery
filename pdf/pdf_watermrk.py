import os
import PyPDF2
# import glob
import pprint as p
# from datetime import datetime


# Sets path to the folder where the file running the program is
dir_path = os.path.dirname(os.path.realpath(__file__))

template = PyPDF2.PdfFileReader(open(f"{dir_path}/output/inv1234__20220104_091318_211269.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open(f"{dir_path}/setup/wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

# p.pprint(template)
# p.pprint(watermark)

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open(f"{dir_path}/output/marked.pdf", "wb") as file:
    output.write(file)

# p.pprint(page)