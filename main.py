from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

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
        <form action='/encrypt' methods='post'>
            
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>

            <label>
                <textarea name="text" type="textarea"></textarea>
            </label>

            <input type="submit"/>
        </form>
            
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/encrypt", methods=['get','post'])
def encrypt():
    rot = request.form['rot']
    text = reqeust.form['text']
    new_text = rotate_string(text,rot)
    return "<h1>{0}</h1>".format(new_text)

app.run()