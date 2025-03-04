import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help?"]],
    [r"how are you ?", ["I'm good, thank you!", "I'm just a chatbot, but I'm doing fine!"]],
    [r"what is your name ?", ["I'm an NLTK chatbot.", "You can call me ChatBot!"]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]],
    [r"(.*)", ["I'm not sure how to respond to that.", "Could you rephrase that?"]]
]
lemmatizer = WordNetLemmatizer()
chatbot = Chat(pairs, reflections)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]  # Lemmatization
    return tokens

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        text = input("You: ").lower()
        if text == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(text)
        print("Chatbot:", response)

start_chat()
