from flask import Flask, render_template, jsonify, request
import openai

# Set your OpenAI API key here
openai.api_key = "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"


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the desired engine
                prompt=question,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            answer = response["choices"][0]["text"]
            data = {"question": question, "answer": answer}
            mongo.db.chats.insert_one({"question": question, "answer": answer})
            return jsonify(data)

    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

