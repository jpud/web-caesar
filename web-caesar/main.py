from flask import Flask, request, redirect
from caesar import rotate_string
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>


    </head>
    <body>
        <form method="POST">
            <label for="caesar">Rotate By:</label>
            <input id="caeser" type="text" name="rot_number" value="" autofocus /><br>
            <label>
            <textarea name = "text_box">
            {0}
            </textarea>
            </label>
            <input type="submit" />
        
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot_number"]
    rot = int(rot)
    text = request.form["text_box"]
    content = rotate_string(text, rot)

    return form.format(content)

app.run()