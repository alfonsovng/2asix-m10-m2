from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <!doctype html>
    <html>
    <head>
    <title>La meva primera web amb Python & Flask</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug = True)