import pygal
from experiment import Experiment


def build_chart_data_uri(experiment: Experiment) -> str:
    """Builds a bar chart from the supplied experiment.

    Args:
        results (ExperimentResult): [description]

    Returns:
        str: SVG in the form of a data URI. Use it as the src for an element.
    """
    bar_chart = pygal.Bar()
    bar_chart.title = experiment.name
    bar_chart.x_labels = map(str, [dp.sum for dp in experiment.results])
    bar_chart.add("Sic ominet", [dp.frequency for dp in experiment.results])

    return bar_chart.render_data_uri()
