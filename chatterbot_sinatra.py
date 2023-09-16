from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Frankie', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.db')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language data
trainer.train('chatterbot.corpus.english')

# You can add more training data or customize responses here

if __name__ == "__main__":
    print("You can start chatting with the bot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Frankie: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Frankie:", response)