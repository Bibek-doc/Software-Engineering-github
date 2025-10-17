from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello Flask!</p>"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

@app.route("/bye")
def bye():
    return "<p>Bye Flask!</p>"

if __name__ == "__main__":
    app.run(debug=True)
