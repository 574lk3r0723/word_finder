from flask import Flask, request, render_template
from finder import find_word_on_website

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        word = request.form['word']
        url = request.form['url']
        print(f"Searching for word: {word} on URL: {url}")  # Debug statement
        result = find_word_on_website(word, url)
        print(f"Result: {result}")  # Debug statement
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
