import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "hi": ["Hello!", "Hi there!"],
    "how are you": ["I'm fine. How are you?", "Doing great!"],
    "your name": ["I'm a Python Chatbot."],
    "bye": ["Goodbye!", "See you later!"]
}

print("🤖 ChatBot Started (type 'exit' to quit)\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Bye!")
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand.")
