PDF to MP3 Converter
This repository contains two Python scripts for converting PDF documents to MP3 audio files, making it easier to listen to text documents on the go. One script is designed for command-line use, offering a quick way for users familiar with terminal or command prompt environments to convert files. The other script provides a graphical user interface (GUI) for users who prefer a more visual interaction method.

Features
Command-Line PDF to MP3 Converter: A simple script that takes the file name as an argument and converts it to an MP3 file using Google's Text-to-Speech (TTS) technology.
GUI PDF to MP3 Converter: A graphical application that allows users to select a PDF file through a file dialog, convert it to MP3, and save the output with minimal clicks.
Installation
To use these scripts, you'll need Python installed on your system along with the PyPDF2 and gtts libraries. The GUI script additionally requires Tkinter, which is included with most Python installations.

Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/pdf-to-mp3-converter.git
Navigate to the cloned repository:
bash
Copy code
cd pdf-to-mp3-converter
Install the required Python packages:
Copy code
pip install PyPDF2 gtts
Usage
Command-Line Script
Run the command-line script by specifying the PDF file path as an argument:

bash
Copy code
python pdf_to_mp3_cli.py path/to/your/document.pdf
GUI Script
Launch the GUI application and follow the on-screen instructions to select a PDF file and convert it:

Copy code
python pdf_to_mp3_gui.py
Dependencies
PyPDF2: A Pure-Python library built as a PDF toolkit.
gTTS: A Python library and CLI tool to interface with Google Translate's text-to-speech API.
Tkinter: The standard GUI toolkit for Python, used for the GUI-based script.
Contributing
Contributions to improve the scripts are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

