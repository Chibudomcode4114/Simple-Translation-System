import tkinter as tk
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
import threading

# Function to perform the translation
def perform_translation(text, src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated_tokens = model.generate(**tokens)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translation

# Function to handle the translation process
def translate_text():
    text = entry.get()  # Get input text from entry widget
    output_label.config(text="Processing...")  # Show "processing..." message
    src_lang = detect(text)  # Detect source language
    tgt_lang = tgt_lang_var.get()  # Get target language from dropdown menu

    # Run the translation in a separate thread to avoid blocking the UI
    def run_translation():
        translation = perform_translation(text, src_lang, tgt_lang)
        output_label.config(text=f"Translation: {translation}")

    threading.Thread(target=run_translation).start()

# Create Tkinter application window
root = tk.Tk()
root.title("Translation System")

# Input label and entry widget
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Target language dropdown menu
tgt_lang_label = tk.Label(root, text="Translate to:")
tgt_lang_label.pack()
tgt_lang_var = tk.StringVar(root)
tgt_lang_var.set("en")  # Default target language is English
tgt_lang_menu = tk.OptionMenu(root, tgt_lang_var, "en", "ig")  # English and Igbo options
tgt_lang_menu.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Output label
output_label = tk.Label(root, text="")
output_label.pack()

# Run Tkinter event loop
root.mainloop()
