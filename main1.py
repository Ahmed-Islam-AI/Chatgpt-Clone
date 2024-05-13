from flask import Flask, render_template, jsonify, request
import openai

# Set your OpenAI API key here
openai.api_key = "OpenAI API KEY"

app = Flask(__name__)


previous_chats = [
    {"question": "What's the weather today?", "answer": "The weather is sunny."},
    {"question": "Tell me a joke.", "answer": "Why did the chicken cross the road? To get to the other side!"},
]

@app.route("/")
def home():
    # Your code for rendering the template and displaying previous chats
    return render_template("index.html", previous_chats=previous_chats)


@app.route("/api", methods=["POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        
        # Use the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the desired engine
            prompt=question,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        answer = response["choices"][0]["text"]
        data = {"question": question, "answer": answer}
        
        # Store the question and answer in your database (not shown in this code)
        
        return jsonify(data)

    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
