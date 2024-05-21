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
