from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Portfolio')


if __name__ == '__main__':
    app.run()
