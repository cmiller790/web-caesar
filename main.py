from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():


    form = '''

    <! DOCTYPE html>
    <html>
        <head>
        <style>
            form {
                background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        <form action="/" method="POST">
        <p><label>Rotate by:<input type="text" name="rot" placeholder="0"'/></label></p>
        <p><textarea name="text"></textarea><input type="submit" value="Submit"/></p>
    </form>
        </body>
    </html>
            

    '''

    return form 

@app.route("/", methods=['POST'])
def encrypt():
    
    txt = request.form["text"]
    rotation = int(request.form["rot"])

    message = rotate_string(txt, rotation)

    encrypted_message = "<h2>message</h2>"

    return encrypted_message

app.run()