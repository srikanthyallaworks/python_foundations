from typing import Final
import flask
import experiment
import chart


__app: Final = flask.Flask(__name__)


@__app.route("/")
def home():
    results = experiment.run_experiment("Looorem ipsum")

    return flask.render_template_string(
        f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>My Experiment</title>
            </head>
            <body>
                <img src='{chart.build_chart_data_uri(results)}'/>
            </body>
        </html>
        """
    )


def run():
    __app.run("0.0.0.0", 5000)
