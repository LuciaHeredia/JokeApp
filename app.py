from flask import Flask, render_template
import jokeApi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', joke_text=jokeApi.get_joke())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)