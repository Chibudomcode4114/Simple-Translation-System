import tkinter as tk
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
import threading

# Mapping source and target languages to the correct Hugging Face model identifiers
LANGUAGE_PAIRS = {
    ("en", "ig"): "Helsinki-NLP/opus-mt-en-ig",
    ("ig", "en"): "Helsinki-NLP/opus-mt-ig-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    # Add more language pairs as needed
}

# Function to perform the translation
def perform_translation(text, src_lang, tgt_lang):
    model_name = LANGUAGE_PAIRS.get((src_lang, tgt_lang))
    if not model_name:
        return "Translation model not available for this language pair."
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
root.title("Simple Translation System")
root.geometry("500x300")  # Set window size to 500x300 pixels

# Welcome message
welcome_label = tk.Label(root, text="Welcome to my Simple Translation System", font=("Helvetica", 16))
welcome_label.pack(pady=10)

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
# Adding more language options: Spanish (es), French (fr), German (de)
tgt_lang_menu = tk.OptionMenu(root, tgt_lang_var, "en", "ig", "es", "fr", "de")
tgt_lang_menu.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Run Tkinter event loop
root.mainloop()
