from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Line Chart Display",
    "description": "Display one line chart.",
    "type": "graph",
    "icon": "chart-histogram",
    "options": [{"name": "separator", "type": "input", "default": "_"}],
    "frame_type": "landscape",  # landscap, portrait, square, 200x300
    "vl_schema": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "transform": [
            {"window": [{"op": "row_number", "as": "x"}]},
        ],
        "mark": {"type": "line", "color": ""},
        "encoding": {
            "x": {"field": "x", "type": "ordinal", "title": None},
            "y": {"field": "values", "type": "quantitative", "title": None},
        },
    },
}


def histogram(values: Str, options):
    pass
