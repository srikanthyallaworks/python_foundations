from typing import Final
import flask
import experiment
import chart


__app: Final = flask.Flask(__name__)


@__app.route("/")
def home():
    results = experiment.get_results()

    return flask.render_template_string(f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>My Experiment</title>
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='site.css') }}"  />
            </head>

            <body>
                <div class="body-content">
                    <img src='{chart.build_chart_data_uri(results)}'/>
                    <hr/>
                    <footer>
                        <p>&copy; 2020</p>
                    </footer>
                </div>
            </body>
        </html>
        """)


def run():
    __app.run("0.0.0.0", 5000)
