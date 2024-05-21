# Simple Translation System

This repository contains a simple translation system implemented in Python. The system translates text from one language to another using pre-trained models from the Hugging Face Transformers library.

## Development Phase 1: Basic Translation System

### Overview

In this initial development phase, I created a basic translation system capable of translating text from Igbo to English using pre-trained translation models. The system was implemented as a Python script with a command-line interface.

### Features

- **Translation Functionality**: The system translates text from Igbo to English.
- **Pre-trained Models**: It utilizes pre-trained translation models from the Hugging Face Transformers library.
- **Simple CLI Interface**: Users interact with the system via a simple command-line interface.

## Development Phase 2: Enhanced Translation System

### Overview

In this updated version of the translation system, we've added an interactive command-line interface (CLI) with language detection, bidirectional translation, translation history tracking, and a "processing..." message during translation.

### Features

- **Interactive CLI**: Users can interact with the system via a command-line interface.
- **Language Detection**: The system automatically detects the language of the input text.
- **Bidirectional Translation**: Translation can be performed in both directions (e.g., Igbo to English and English to Igbo).
- **Translation History**: The system keeps track of translation history within the session.
- **Processing Message**: A "processing..." message is displayed while the translation is being performed.

## Development Phase 3

### New Features and Enhancements

- **Enhanced UI:**
  - Enlarged the application window to 500x300 pixels.
  - Added a welcome message at the top of the window.
  
- **Additional Languages:**
  - Added support for Spanish, French, and German.
  
- **Improved Model Selection:**
  - Implemented a dictionary to map language pairs to the correct Hugging Face model identifiers.
  - Ensured proper model selection based on detected source and target languages.

### Code Changes

- Added `LANGUAGE_PAIRS` dictionary to map language pairs to model names.
- Updated `perform_translation` function to use the correct model name based on the selected language pair.
- Enhanced the Tkinter GUI to include additional languages in the dropdown menu.

## Development Phase 4

### New Features and Enhancements

- **Enhanced UI:**
  - Enlarged the application window to 500x300 pixels.
  - Added a welcome message at the top of the window.
  
- **Additional Languages:**
  - Added support for Spanish, French, and German.
  
- **Voice Capabilities:**
  - Added speech-to-text functionality for input.

## Usage

1. **Run the application:**

    ```bash
    python translation_system.py
    ```

2. **Enter text to translate:**

    - Type the text you want to translate in the input box or click the "Speak" button to use voice input.

3. **Select target language:**

    - Choose the target language from the dropdown menu.

4. **Translate:**

    - Click the "Translate" button.
    - The application will detect the source language, perform the translation, and display the result.
    - The translated text will also be read aloud  

## Dependencies

The project relies on the following Python libraries:

- `tkinter`: For the graphical user interface.
- `transformers`: For the translation models.
- `langdetect`: For automatic language detection.
- `threading`: For handling the translation process without blocking the UI.

These dependencies are listed in the `requirements.txt` file.




### Usage

To use the translation system:

1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.8 or higher recommended).
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the script `translation.py`.
5. Follow the prompts to enter the text you want to translate.

### Example

```bash
python translation.py
