def start_chatbot():
    print("Chatbot: Hello! I am a rule-based AI. Type 'exit' to end the session.")

    while True:
        
        user_input = input("You: ").lower().strip()

        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        elif user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm just a bot, but I'm doing great!")

        elif user_input in ["what is your name", "your name"]:
            print("Chatbot: I am a rule-based chatbot created using Python.")

        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Bye! Take care 😊")

        
        else:
            print("Chatbot: Sorry, I don't understand that. Please try another command.")


if __name__ == "__main__":
    start_chatbot()