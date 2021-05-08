from flask import Flask
from speech_recognition import register_new_word, query_word

api = Flask("Speech Recognition")

@api.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    api.run()
