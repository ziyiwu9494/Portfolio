from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['TESTING'] = True

card = [
    {"title": "", "image_uri": "", "description": "", "github": "", "demo": ""},
    {"title": "", "image_uri": "", "description": "", "github": "", "demo": ""},
    {"title": "", "image_uri": "", "description": "", "github": "", "demo": ""},
    {"title": "", "image_uri": "", "description": "", "github": "", "demo": ""},
]


@app.route('/')
def index():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run()
