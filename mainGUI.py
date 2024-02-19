import tkinter as tk
from tkinter import filedialog, messagebox, font
from gtts import gTTS
import PyPDF2


def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_path.set(file_path)


def convert_pdf_to_mp3():
    try:
        pdf_file = pdf_path.get()
        if not pdf_file:
            messagebox.showerror("Error", "Please select a PDF file first.")
            return

        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + " "

        tts = gTTS(text=text, lang='en')
        output_file = pdf_file.replace('.pdf', '.mp3')
        tts.save(output_file)
        messagebox.showinfo("Success", f"MP3 file has been saved successfully:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



root = tk.Tk()
root.title("PDF to MP3 Converter")


root.geometry("500x300")


root.configure(bg='gray16')

title_font = font.Font(family="Helvetica", size=45, weight="bold")  # Define font
title_label = tk.Label(root, text="PDF TO MP3", bg='gray16', fg='gray69', font=title_font)
title_label.pack(pady=(80, 20))

pdf_path = tk.StringVar()

# Create the GUI layout with colors
tk.Label(root, text="PDF File:", bg='gray16', fg='white').pack(side=tk.LEFT, padx=10, pady=10)
entry = tk.Entry(root, textvariable=pdf_path, width=20)
entry.pack(side=tk.LEFT, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=select_pdf, bg='gray69', fg='black')
browse_button.pack(side=tk.LEFT, padx=10, pady=10)
convert_button = tk.Button(root, text="Convert to MP3", command=convert_pdf_to_mp3, bg='pink', fg='black')
convert_button.pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()
