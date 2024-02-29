from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return "<b>" + function() + "</b>"

    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        return "<em>" + function() + "</em>"

    return wrapper_func


def make_underlined(function):
    def wrapper_func():
        return "<u>" + function() + "</u>"

    return wrapper_func


@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph<p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmljZzBjc3g2cDk4Z2tlNjhsZzZ1cWdhM3dxbnF1YWo2Y21hN2w1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6MWahPArixa6I/giphy.gif" width=200>')


@app.route("/bye")
def bye():
    return "<p>Bye!<p>"


@app.route("/username/<name>")
def greet(name):
    return f"<p>Greetings to kox {name}!<p>"


if __name__ == "__main__":
    app.run(debug=True)
