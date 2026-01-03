# 🌐 AI Language Translator

A robust, real-time language translation app built with Python and Streamlit. This tool leverages Google's translation API to provide instant text translation, featuring voice input (Speech-to-Text) and audio playback (Text-to-Speech) for a seamless user experience.

Developed as part of the CodeAlpha Internship program.

## 🚀 Features

*   **Multi-Language Support**: Translates text between 100+ supported languages.
*   **🎙️ Speech-to-Text (STT)**: Integrated microphone support allowing users to speak input text directly (powered by `streamlit-mic-recorder`).
*   **🔊 Text-to-Speech (TTS)**: Listen to the pronunciation of translated text (smartly handles unsupported audio languages).
*   **📋 One-Click Copy**: Built-in code block format for easy copying of translations.
*   **⚡ Auto-Detection**: Automatically identifies the source language.
*   **🛡️ Robust Error Handling**: Gracefully handles network interruptions and API limits.

## 🛠️ Tech Stack

*   **Frontend**: Streamlit (Custom CSS & Layouts)
*   **Translation Engine**: `deep-translator` (Google Translator API)
*   **Audio Processing**: `gTTS` (Google Text-to-Speech)
*   **Voice Input**: `streamlit-mic-recorder`

## ⚙️ Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**

    ```bash
    git clone https://github.com/igwekailota-beep/CodeAlpha_Tasks.git
    cd CodeAlpha_LanguageTranslator
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ How to Run

Start the Streamlit server:

```bash
streamlit run app.py
```

The app will open automatically in your default web browser (usually at `http://localhost:8501`).

*Note*: For the microphone feature to work, ensure you allow browser permission for audio recording.

## 📂 Project Structure

```plaintext
├── app.py                  # Main application interface and logic
├── translator_utils.py     # Helper functions for translation API
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## 🐛 Known Limitations

*   **Network Dependency**: The app requires an active internet connection to reach Google's servers.
*   **Audio Support**: While translation works for 100+ languages, audio playback (TTS) is limited to languages supported by Google's voice engine. The app detects this and alerts the user if audio is unavailable for a specific language.

## 🤝 Acknowledgments

*   CodeAlpha for the internship opportunity.
*   The open-source community for the amazing Python libraries (`deep-translator`, `gTTS`, `streamlit`).
