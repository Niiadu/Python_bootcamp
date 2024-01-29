from flask import Flask
import time

app = Flask(__name__)

def make_bold(bold):
    def new_function():
        return f"<b>{bold()}</b>"
    return new_function


def make_emphasis(emphasis):
    def new_emphasis():
        return f"<em>{emphasis()}</em>"
    return new_emphasis


def make_underlined(underlined):
    def new_underlined():
        return f"<u>{underlined()}</u>"
    return new_underlined

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello World!'


@app.route("/<name>")
def nii(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()

# def rotate_function(function):
#
#     def new_function():
#         time.sleep(2)
#         function()
#         function()
#     return new_function

# whats_this = rotate_function()
# whats_this()

# @rotate_function
# def say_hello():
#     print("hello")
#
# @rotate_function
# def say_bye():
#     print("bye")
#
# @rotate_function
# def say_how():
#     print("How are you?")
#
# decorated_function = rotate_function(say_how)
# decorated_function()