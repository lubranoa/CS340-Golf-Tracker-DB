from flask import flask
import os

# Configuration

app = Flask(__name__)

# Routes

@app.route('/')
def root():
    return "Welcome to our Golf Tracker Database!"

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT',15432))
    app.run(port=port)
    