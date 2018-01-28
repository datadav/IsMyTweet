from flask import request, url_for, render_template
from flask_api import FlaskAPI, status, exceptions
app = FlaskAPI(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')	


if __name__ == "__main__":
    app.run()