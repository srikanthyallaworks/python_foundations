import pygal
from experiment import ExperimentResult


def build_chart_data_uri(results: ExperimentResult) -> str:
    """Builds a bar chart from the supplied experiment.

    Args:
        results (ExperimentResult): [description]

    Returns:
        str: SVG in the form of a data URI. Use it as the src for an element.
    """
    bar_chart = pygal.Bar()
    bar_chart.title = "Lorem ipsum sic dolor"
    bar_chart.x_labels = map(str, [dp.sum for dp in results])
    bar_chart.add("Sic ominet", [dp.roll_count for dp in results])

    return bar_chart.render_data_uri()
