# 🌐 AI Language Translator

A robust, real-time language translation app built with Python and Streamlit. This tool leverages Google's translation API to provide instant text translation, featuring voice input (Speech-to-Text) and audio playback (Text-to-Speech) for a seamless user experience.

Developed as part of the CodeAlpha Internship program.

## 🚀 Usage

There are two ways to use the AI Language Translator:

### 1. Accessing the Live App (Recommended)

You can access the live, deployed application directly in your browser without any installation:

[**➡️ Live Demo: https://lingua-flow.streamlit.app/**](https://lingua-flow.streamlit.app/)

### 2. Running Locally

If you want to run the application on your own machine, follow these steps:

#### Prerequisites

- Python 3.11. You can download it from [python.org](https://www.python.org/downloads/).

#### Installation and Setup

1.  **Clone the repository**

    ```bash
    git clone https://github.com/igwekailota-beep/CodeAlpha_Tasks.git
    cd CodeAlpha_LanguageTranslator
    ```

2.  **Create and Activate a Virtual Environment**

    ```bash
    # Create the virtual environment using Python 3.11
    py -3.11 -m venv venv

    # Activate the virtual environment
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

#### How to Run

Start the Streamlit server:

```bash
py -3.11 -m streamlit run app.py
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
*   **Speech-to-Text Latency**: The voice input feature processes audio after the user has finished speaking. The time it takes to display the transcribed text depends on the length of the audio and network speed, which may result in a noticeable delay.

## 🤝 Acknowledgments

*   CodeAlpha for the internship opportunity.
*   The open-source community for the amazing Python libraries (`deep-translator`, `gTTS`, `streamlit`).
