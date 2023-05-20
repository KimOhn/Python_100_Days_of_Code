from flask import Flask
import random

app = Flask(__name__)

def color_decorate(function):
    def wrapper_fun():
        rand_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        return f"<h1 style = color:'{rand_color}';>"  + function() + "</h1>"

@app.route('/')
def intro():
    return "<h1>Guess a number</h1>"

guess = random.choice(range(0,9))

@app.route('/<int:number>')
def user_guess(number):
    if number < guess:
        return "<h1 style = color: 'red';> Too low </h1>" \
    "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number >guess:
        return "<h1 style = color: 'blue';> Too high</h1>" \
    "<img src = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return "<h1 style = color: 'green';> correct</h1>" \
    "<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"

if __name__ == "__main__":
    app.run(debug=True)