import streamlit as st
from translator_utils import translate_text, get_supported_languages
from gtts import gTTS, lang as tts_lang_check
import io
from streamlit_mic_recorder import speech_to_text
from requests.exceptions import ConnectionError

# --- 1. Page Configuration ---
st.set_page_config(page_title="CodeAlpha Translator", page_icon="🌐", layout="centered")

# --- 2. Custom CSS for Styling ---
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Sidebar (About & Help) ---
with st.sidebar:
    st.header("About 📚")
    st.info("This AI-powered translator is a project for the CodeAlpha internship. It uses advanced translation models to provide accurate and context-aware translations.")
    st.markdown("---")
    st.header("How to Use 🚀")
    st.markdown("""
    1. **Speak** 🎙️ or **Type** ✍️ your text.
    2. **Select** source (auto) and target languages.
    3. **Click** 'Translate'.
    4. **Listen** 🔊 or **Copy** 📋 the result.
    """)
    st.caption("Developed by CodeAlpha Intern")

# --- 4. Main App Header ---
st.title("🎨 AI Language Translator")
st.markdown("Translate text instantly with a modern touch.")

# --- 5. Language Selection (Columns) ---
col1, col2 = st.columns(2)
languages = get_supported_languages()
lang_options = list(languages.keys())

with col1:
    # Just a visual label, we use 'auto' logic mostly
    st.selectbox("Source Language", ["auto"] + lang_options)

with col2:
    target_language = st.selectbox("Target Language", lang_options, index=lang_options.index('spanish') if 'spanish' in lang_options else 0)

# --- 6. Input Area with Speech-to-Text (Batch) ---
st.write("### Enter text to translate:")

# Initialize session state for the source text if it doesn't exist
if 'source_text' not in st.session_state:
    st.session_state.source_text = ""

# Create columns for the layout
input_col, mic_col = st.columns([6, 1])

# Logic for the microphone input
with mic_col:
    st.write("##") # Vertical spacer
    text_from_mic = speech_to_text(
        language='en',
        start_prompt="🎙️",
        stop_prompt="🛑",
        key='stt_batch_btn' # Use a unique key
    )

# Logic Before Widget: Check for new mic input and update state BEFORE drawing the text area
if text_from_mic and text_from_mic != st.session_state.source_text:
    st.session_state.source_text = text_from_mic

# Logic for the text area
with input_col:
    # The text_area is now drawn. It is bound to session_state via its key.
    # On the *next* run after a state update, it will show the new text.
    # To make it update instantly, we must use the value parameter.
    # However, the user wants to revert to the simple batch mode.
    # The simplest way is to just key it to the session state.
    # Let's ensure the full pattern is robust.
    source_text_from_area = st.text_area(
        label="Input Text",
        label_visibility="collapsed",
        height=150,
        key="source_text", # Binds this widget to st.session_state.source_text
        placeholder="Type here or click the mic to speak..."
    )

# Final determination of source text for translation logic below
source_text = st.session_state.source_text

# --- 7. Translation & Output Logic ---
if st.button("Translate 🚀"):
    if source_text:
        try:
            # Get the language code (e.g., 'english' -> 'en')
            target_code = languages[target_language]

            # 1. Perform Translation
            with st.spinner('Translating...'):
                translated_text = translate_text(source_text, target_code)

            # 2. Show Success
            st.success("Translation Complete!")

            # 3. Display Result (Using st.code for the built-in Copy Button)
            st.markdown("### Translated Text:")
            st.code(translated_text, language=None)

            # 4. Text-to-Speech (With "Supported Language" Check)
            st.markdown("### Listen:")
            
            # Check if the target language is supported by Google TTS
            supported_tts_langs = tts_lang_check.tts_langs()
            
            if target_code in supported_tts_langs:
                # Create audio in memory (no file saved)
                tts = gTTS(text=translated_text, lang=target_code)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                st.audio(audio_bytes, format='audio/mp3')
            else:
                # Fallback for languages like Igbo ('ig')
                st.info(f"Audio playback is not currently available for {target_language}.")

        except ConnectionError:
            st.error("⚠️ Network Error: Please checks your internet connection.")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to translate.")

# --- 8. Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center;'>Built with ❤️ using Streamlit & Python</div>", unsafe_allow_html=True)