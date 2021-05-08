from flask import Flask, render_template
from speech_recognition import register_new_word, query_word

api = Flask("Speech Recognition", template_folder='templates')

@api.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    api.run(debug=True)
