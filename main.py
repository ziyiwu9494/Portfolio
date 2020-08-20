from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['TESTING'] = True

cards = [
    {"title": "Physics", "image_uri": "https://www.dropbox.com/s/n02enkvriy3povm/Physics.png?raw=1", "description": "Physics E&M statics modeling and graphing in Python. ", "github": "https://github.com/ziyiwu9494/Physics", },
    {"title": "Blockian", "image_uri": "https://www.dropbox.com/s/xswwcp0v0qinfu6/Blockian.png?raw=1", "description": "Square Block 3rd-person shooter created using Java Canvas", "demo": "https://www.dropbox.com/s/dg2bglvqlcr9w0q/Team431.jar?dl=0"},
    {"title": "Breakout", "image_uri": "https://www.dropbox.com/s/nohfvrlujopx7gp/Breakout.png?raw=1", "description": "Atari breakout in Java Canvas with a couple fun new features.", "demo": "https://www.dropbox.com/s/l9saskwks2dikjv/Ziyi%20Wu%20Breakout540p.jar?dl=0"},
]


@app.route('/')
def index():
    return render_template('index.html', title='Home', cards=cards)


if __name__ == '__main__':
    app.run()
