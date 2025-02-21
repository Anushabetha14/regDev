from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('index.html')  # Ensure 'index.html' is inside 'templates' folder

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get port dynamically for deployment
    app.run(host='0.0.0.0', port=port)
