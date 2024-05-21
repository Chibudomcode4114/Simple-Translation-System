from transformers import MarianMTModel, MarianTokenizer

# Function to translate text
def translate(text, src_lang, tgt_lang):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    
    # Tokenize the text
    tokens = tokenizer(text, return_tensors="pt", padding= True)

    # Generate the translation
    translated_tokens = model.generate(**tokens)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    # Prints the translation
    return translation


# Example usage
if __name__ == "__main__":
    src_lang = "en" #Source language: English
    tgt_lang = "fr" #Target language: French
    text = "Hello, how are you?" #Text to translate


    translation = translate(text, src_lang, tgt_lang) 
    print(f"Original: {text}")
    print(f"Translation: {translation}")