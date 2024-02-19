import PyPDF2
from gtts import gTTS
import sys
import os

def pdfReading(PdfPath):
    text=""
    with open(PdfPath,'rb') as f:
        pdfReader = PyPDF2.PdfReader(f)
        for pageNum in range(len(pdfReader.pages)):
            currPage = pdfReader.pages[pageNum]
            text += currPage.extract_text() + " "
    return text

def ConvertMP3(text, outputFile):
    tts = gTTS(text=text,lang='en')
    tts.save(outputFile)
    print(f"MP3 file saved as {outputFile}")


PDFFILE = sys.argv[1]
outputName = "Narrated"+PDFFILE[:len(PDFFILE)-4]+".mp3"
pdfTxt = pdfReading(PDFFILE)
ConvertMP3(pdfTxt,outputName)