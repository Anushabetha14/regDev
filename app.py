from flask import Flask, render_template
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('index.html')  # Ensure 'index.html' is in the 'templates' folder

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()  # Open browser after 1.25 seconds
    app.run(debug=True)
