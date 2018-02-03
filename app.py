from flask import Flask, render_template
from random import randint
import json

app = Flask(__name__)

with open('data/data.json') as f:
    data = json.load(f)
@app.route('/')
def home():
    tall1 = randint(1,12)
    tall2 = randint(1,12)
    return 'Hva er {} ganger {}?'.format(tall1, tall2)

@app.route('/test')
def test():
    land = data['land']
    return render_template('test.html', land=land)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
