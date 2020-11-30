from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from datetime import datetime
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

@app.route('/')
def  index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent, current_time=datetime.utcnow())

def load_user(id):
    with open('users.json', 'r') as json_file:
        data = json.load(json_file)
    if id in data.keys():
        print(data[id])
        return data[id]  # returns the user name
    else:
        return False


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html'), 404

@app.route('/user/<id>')
def get_user(id):
    user_name = load_user(id)
    print("user name is:", user_name)
    if not user_name:
        abort(404)
    return render_template('user.html', name=user_name, id=id)


if __name__ == "__main__":
    app.run(debug=True)