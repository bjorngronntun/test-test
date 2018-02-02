from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    tall1 = randint(1,12)
    tall2 = randint(1,12)
    return 'Hva er {} ganger {}?'.format(tall1, tall2)

if __name__ == '__main__':
    app.run(port=5000)
