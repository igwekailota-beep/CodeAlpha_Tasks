import streamlit as st
import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import warnings

warnings.filterwarnings('ignore')

# --- NLTK Data Check and Download ---
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/wordnet')
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    st.info("Downloading necessary NLTK data (punkt, wordnet, stopwords). This may take a moment...")
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('stopwords', quiet=True)
    st.success("NLTK data downloaded successfully!")


# --- Load Q&A Data ---
@st.cache_data
def load_qa_data(file_path):
    """Loads Q&A data from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['questions']

# --- Text Preprocessing ---
lemmatizer = nltk.stem.WordNetLemmatizer()
stop_words = set(nltk.corpus.stopwords.words('english'))

def preprocess_text(text):
    """Tokenizes, lemmatizes, and removes punctuation/stopwords."""
    # Lowercase and tokenize
    tokens = nltk.word_tokenize(text.lower())
    # Remove punctuation and stopwords, then lemmatize
    lemmas = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation and token not in stop_words]
    return " ".join(lemmas)


# --- Find Best Match ---
def find_best_match(user_query, questions_data):
    """Finds the best matching question from the dataset using TF-IDF and Cosine Similarity."""
    if not user_query.strip():
        return None, 0.0

    processed_query = preprocess_text(user_query)
    question_texts = [q['question'] for q in questions_data]
    processed_questions = [preprocess_text(q) for q in question_texts]

    # Vectorize the questions and the user query
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_questions)
    query_vector = vectorizer.transform([processed_query])

    # Calculate cosine similarity
    similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Find the best match
    best_match_index = similarities.argmax()
    max_similarity = similarities[0, best_match_index]

    # Define a threshold for a "good" match
    if max_similarity > 0.2: # Threshold can be adjusted
        return questions_data[best_match_index]['answer'], max_similarity
    else:
        return "I'm sorry, I don't have an answer to that. Could you try rephrasing your question?", max_similarity


# --- Streamlit UI ---
st.set_page_config(page_title="University FAQ Bot", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("About the Bot")
    st.markdown("""
        This is a simple FAQ chatbot for a university.
        
        **How it works:**
        1.  You ask a question.
        2.  The bot preprocesses your question (tokenization, lemmatization).
        3.  It uses a **TF-IDF Vectorizer** to convert your question and the pre-defined questions into numerical vectors.
        4.  **Cosine Similarity** is then used to find the question in its database that is most similar to yours.
        5.  The bot returns the corresponding answer.
        
        This project was created as part of the CodeAlpha internship program.
    """)
    st.markdown("---")
    st.markdown("Created by a CodeAlpha Intern.")


# --- Main Chat Interface ---
st.title("🎓 University FAQ Chatbot")
st.write("Ask me anything about the university!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Load the Q&A data
qa_data = load_qa_data('CodeAlpha_FAQ_Chatbot/qa_data.json')

# React to user input
if prompt := st.chat_input("Ask a question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get bot response
    answer, similarity = find_best_match(prompt, qa_data)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(answer)
        # Optionally display similarity score for debugging/interest
        # st.write(f"(Similarity: {similarity:.2f})")

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})
