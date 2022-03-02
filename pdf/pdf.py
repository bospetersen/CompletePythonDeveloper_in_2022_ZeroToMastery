import PyPDF2 
import pprint as p
import os


# Sets path to the folder where the file running the program is
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/dummy.pdf', 'rb') as file:
  reader = PyPDF2.PdfFileReader(file)

  # --- Rotate ---
  page = reader.getPage(0)
  rotatedPage = page.rotateCounterClockwise(90)
  # print(page.rotateCounterClockwise(90))
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)
  with open(f'{dir_path}/dummy_rotated.pdf', 'wb') as new_file:
    writer.write(new_file)
  # --- *** ---
  
  # # --- Reader ---
  # print(reader.documentInfo['/Author'])
  # print(reader.documentInfo['/Producer'])
  # print('='*100)
  # p.pprint(reader.getPage(0))
  # print(content['/Contents'])
  # # --- *** ---