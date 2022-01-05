from typing import Final
import flask
import experiment 
import chart


app: Final = flask.Flask(__name__)


def get_page(data_url: str) -> str:
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>My Experiment</title>
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='site.css') }}"  />
            </head>

            <body>
                <div class="body-content">
                    <img src='{data_url}'/>
                    <hr/>
                    <footer>
                        <p>&copy; 2020</p>
                    </footer>
                </div>
            </body>
        </html>
        """



@app.route("/")
def home():
    results = experiment.get_results() 
    content = get_page(chart.build_chart_data_uri(results))

    return flask.render_template_string(content)


def run():
    app.run("0.0.0.0", 5000)
