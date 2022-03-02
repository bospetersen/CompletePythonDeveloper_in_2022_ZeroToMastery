# Python script to PDF to Audio
# https://pypi.org/project/pyttsx3/
import os
import PyPDF2
import pyttsx3
import textract

# import pprint as p
# from datetime import datetime
# import glob

# Sets path to the folder where the file running the program is
dir_path = os.path.dirname(os.path.realpath(__file__))


text = textract.process(f"{dir_path}/main/crow-peacock.pdf", encoding='ascii')
text.decode('utf-8')
print(text)
print("="*150)

# pdfreader = PyPDF2.PdfFileReader(
#     open(f'{dir_path}/main/crow-peacock.pdf', 'rb'))
speaker = pyttsx3.init()
# for page_num in range(pdfreader.numPages):
    # extracting text from the PDF
    # text = pdfreader.getPage(page_num)
    # text.extractText()
    # Removes unnecessary spaces and break lines
    # cleaned_text = str(text).strip().replace('\n', ' ')

print(text)  # Print the text from PDF
    # txt = speaker.say(cleaned_text) 
           
    ## Let The Speaker Speak The Text
    # Saving Text In a audio file 'story.mp3'
speaker.save_to_file(text, f'{dir_path}/main/story.mp3')
speaker.runAndWait()
speaker.stop()
