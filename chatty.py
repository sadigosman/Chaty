import openai
# Chatty is a small chatting program using ChatGPT API from openai

# Set your OpenAI API key
api_key = "9E4M8xVtN"

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt(prompt, api_key):
    response = openai.Completion.create(
        engine="davinci-codex",  # You can choose a different engine if needed
        prompt=prompt,
        temperature=0.6,  # Controls the randomness of the output
        max_tokens=180,  # Maximum number of tokens (words) in the response
        top_p=1.0,  # Controls diversity
        frequency_penalty=0.0,  # Higher values encourage more diverse responses
        presence_penalty=0.0,  # Higher values encourage less repetition
        stop=["\n"]  # Stop generation at newlines
    )
    return response.choices[0].text.strip()

# Main loop
print("Hi this is Chaty! Type 'exit' to quite.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = chat_with_gpt(user_input, api_key)
    print("Chaty:", response)
