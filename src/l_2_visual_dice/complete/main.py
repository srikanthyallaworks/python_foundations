from dice import Die, Cup
from typing import Final
import flask

app = flask.Flask(__name__)    # Create an instance of the class for our use


ts: Final = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>xyzzzzzzzzzzzz</title>
    </head>
    <body>
        <div class="body-content">
            <h1>Hello World!</h1>
        </div>
    </body>
</html>
'''


@app.route("/")
def home():
    return flask.render_template_string(ts)


def main():
    app.run('0.0.0.0', 5000)


if __name__ == "__main__":
    main()
