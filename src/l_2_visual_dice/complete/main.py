from typing import Final
from collections import Counter
import flask
import pygal
from dice import Cup

app: Final = flask.Flask(__name__)    # Create an instance of the class for our use


@app.route("/")
def home():
    bar_chart = pygal.Bar()
    bar_chart.title = 'Lorem ipsum sic dolor'

    cup: Final = Cup(10)
    sums = [cup.roll() for _ in range(50000)]
    counts = sorted(Counter(sums).items(), key=lambda kvp: kvp[0])

    bar_chart.x_labels = map(str, [kvp[0] for kvp in counts])
    bar_chart.add('Sic ominet', [kvp[1] for kvp in counts])

    return bar_chart.render_response()


def main():
    app.run('0.0.0.0', 5000)


if __name__ == "__main__":
    main()
