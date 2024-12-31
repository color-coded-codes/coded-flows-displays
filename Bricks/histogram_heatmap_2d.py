from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Line Chart Display",
    "description": "Display one line chart.",
    "type": "graph",
    "icon": "chart-scatter",
    "options": [{"name": "separator", "type": "input", "default": "_"}],
    "frame_type": "500x500",  # landscap, portrait, square, 200x300
    "vl_schema": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "data": {"url": "data/movies.json"},
        "transform": [
            {
                "filter": {
                    "and": [
                        {"field": "x", "valid": True},
                        {"field": "y", "valid": True},
                    ]
                }
            }
        ],
        "mark": "rect",
        "encoding": {
            "x": {
                "bin": {"maxbins": 60},
                "field": "x",
                "type": "quantitative",
            },
            "y": {
                "bin": {"maxbins": 40},
                "field": "y",
                "type": "quantitative",
            },
            "color": {"aggregate": "count", "type": "quantitative"},
        },
        "config": {"view": {"stroke": "transparent"}},
    },
}


def histogram_heatmap_2d(values: Str, options):
    pass
