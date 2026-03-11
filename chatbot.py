import google.generativeai as genai

# Read API key
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Configure API
genai.configure(api_key=api_key)

# Correct model name
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Start chat session
chat = model.start_chat(history=[])

print("Chatbot started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)