from typing import Final
from collections import Counter
import flask
import pygal
from dice import Cup

app: Final = flask.Flask(__name__)  # Create an instance of the class for our use


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


def get_data_url() -> str:
    bar_chart = pygal.Bar()
    bar_chart.title = "Lorem ipsum sic dolor"

    cup: Final = Cup(10)
    sums = [cup.roll() for _ in range(50000)]
    counts = sorted(Counter(sums).items(), key=lambda kvp: kvp[0])

    bar_chart.x_labels = map(str, [kvp[0] for kvp in counts])
    bar_chart.add("Sic ominet", [kvp[1] for kvp in counts])

    return bar_chart.render_data_uri()


@app.route("/")
def home():
    bar_chart = get_data_url()
    content = get_page(bar_chart)

    return flask.render_template_string(content)


def main():
    app.run("0.0.0.0", 5000)


if __name__ == "__main__":
    main()
