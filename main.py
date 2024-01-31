from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Display key metrics on the home/summary page
    return render_template('home.html', metrics={})


if __name__ == '__main__':
    app.run(debug=True, port=8080)