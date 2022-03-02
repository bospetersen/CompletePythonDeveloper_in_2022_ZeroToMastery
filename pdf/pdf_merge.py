import os
import PyPDF2
import glob
import pprint as p
from datetime import datetime

# Sets path to the folder where the file running the program is
dir_path = os.path.dirname(os.path.realpath(__file__))

# scan directory for pdf-files
pdf_files = glob.glob(f'{dir_path}/input/*.pdf')
p.pprint(pdf_files)

merged_file_name = input('Enter filename for merged pdf: ')

# --- merge multiple pdf-files ---
mergeFile = PyPDF2.PdfFileMerger()
for pdf in pdf_files:
    mergeFile.append(PyPDF2.PdfFileReader(f'{pdf}', 'rb'))

# Current date time in local system
date_now = datetime.now().strftime('%Y%m%d_%H%M%S_%f')


# Save file
mergeFile.write(f"{dir_path}/output/{merged_file_name}_{date_now}.pdf")

# --- *** ---
