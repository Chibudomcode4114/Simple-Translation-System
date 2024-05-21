from transformers import MarianMTModel, MarianTokenizer

# Function to translate text
def translate(text, src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the text
    tokens = tokenizer(text, return_tensors="pt", padding=True)

    # Generate translation
    translated_tokens = model.generate(**tokens)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translation

# Example usage
if __name__ == "__main__":
    src_lang = "en"  # Source language: Igbo
    tgt_lang = "ig"  # Target language: English
    # text = "Kedu ka ị mere?"  # Example text in Igbo
    text = "How are you?"  # Example text in English

    translation = translate(text, src_lang, tgt_lang)
    print(f"Original: {text}")
    print(f"Translation: {translation}")
