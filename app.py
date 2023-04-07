from flask import Flask, render_template

# Simple backend server for dice game page

app = Flask(__name__)


# mapping for html page
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
