"""
A simple guestbook flask app.
"""
import flask
from index import Index
from add import Add


app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/add/',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)


