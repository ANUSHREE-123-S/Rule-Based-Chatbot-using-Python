print("🤖 Simple Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you? 😊")

    elif "name" in user:
        print("Bot: I am a simple Python chatbot created with if-else!")

    elif "help" in user:
        print("Bot: Sure! Tell me what you need help with.")

    elif "your age" in user or "age" in user:
        print("Bot: I don't have an age. I just run on Python code!")

    elif "time" in user:
        print("Bot: Sorry, I can’t tell the time yet ⏳")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day 🎉")
        break

    else:
        print("Bot: I didn't understand that. Can you say it differently?")
