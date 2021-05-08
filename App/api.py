from flask import Flask

api = Flask("Speech Recognition")

@api.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    api.run()