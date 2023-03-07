import os
import time
import pyttsx3
import PyPDF2
import argparse

class AudioBook:
    def __init__(self, path):
        self.path = path
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def read_book(self):
        with open(self.path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            total_pages = pdf_reader.numPages
            for i in range(total_pages):
                page = pdf_reader.getPage(i)
                text = page.extractText()
                self.engine.say(text)
                self.engine.runAndWait()
                time.sleep(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Audio Book Reader')
    parser.add_argument('path', metavar='path', type=str, help='Path to the PDF file')
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print("Invalid file path. Please provide a valid path.")
        exit(0)
        
    audiobook = AudioBook(args.path)
    audiobook.read_book()
