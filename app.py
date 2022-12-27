import openai
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv('api_key')

@app.route('/chat', methods=['POST'])
def chat():

    # Get user input from request
    data = request.get_json()
    print("requests to chat", data)
    user_input = data['input']
    print("user_input", user_input)
    # Generate response from GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {user_input}\nBot:",
        temperature=0.5,
        max_tokens=128
    )
  
    # Get response text from GPT-3
    response_text = response['choices'][0]['text']
    
    # Return response as JSON
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run()
