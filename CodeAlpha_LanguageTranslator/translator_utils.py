from deep_translator import GoogleTranslator

def get_supported_languages():
    """
    Returns a dictionary of supported languages.
    Example: {'english': 'en', 'spanish': 'es', ...}
    """
    # FIXED: Instantiated the class () and used the correct method name
    return GoogleTranslator().get_supported_languages(as_dict=True)

def translate_text(text, target_lang):
    """
    Translates text to the target language.
    Source is set to 'auto' to handle any input language.
    """
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)