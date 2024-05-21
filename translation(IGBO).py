from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
import sacremoses


# Function to translate text from one language to another
def translate(text, src_lang, tgt_lang):
    print("Processing...")

    try:
        model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

        # Tokenize the text
        tokens = tokenizer(text, return_tensors="pt", padding=True)

        # Generate translation
        translated_tokens = model.generate(**tokens)
        translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return translation
    except Exception as e:
        return f"Error: {e}"

# Interactive CLI with language detection, bidirectional translation,error handling, and history
if __name__ == "__main__":
    print("Welcome to the Translation System")
    history = []
    # src_lang = "en"  # Source language: Igbo
    # tgt_lang = "ig"  # Target language: English
    src_lang = input("Enter the source language: \ne.g., 'ig' for Igbo, 'en' for English\n").strip()
    tgt_lang = input("Enter the target language: \ne.g., 'ig' for Igbo, 'en' for English\n").strip()


    while True:
        text = input("Enter text to translate (or type 'exit' to quit): ").strip()
        if text.lower() == "exit":
            print("Exiting Translation System...")
            print("Translation History:")
            for i, (src, tgt) in enumerate(history):
                print(f"{i+1}. {src} -> {tgt}")
            break

        try:
            detected_lang = detect(text)
            print(f"Detected source language: {detected_lang}")
            # if detected_lang == 'en':
            #     src_lang = 'en'
            #     tgt_lang = 'ig'
            # elif direction == 'ig':
            #      src_lang = detected_lang
            #      tgt_lang = 'ig'
            # else:
            #     src_lang = detected_lang
            #     tgt_lang = 'en'
            direction = input("Translate to (en for English, ig for Igbo): ").strip().lower()
            if direction == 'en':
                src_lang = detected_lang
                tgt_lang = 'en'

                # I added this line
            print(f"Source language: {src_lang}")

            translation = translate(text, src_lang, tgt_lang)
            print(f"Translation: {translation}")
            # history.append((text, translation))
            history.append(f"{text} ({src_lang}) -> {translation} ({tgt_lang})")

        except Exception as e:
                print(f"Error: {e}")
                print("Could not detect language or translate the text. Please try again.")
                
