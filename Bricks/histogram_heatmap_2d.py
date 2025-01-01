from typing import Union
from coded_flows.types import List, DataSeries, NDArray, DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "2D Histogram Heatmap",
    "description": "2D Histogram Heatmap.",
    "type": "graph",
    "icon": "chart-scatter",
    "options": [
        {
            "name": "encoding__x__field",
            "display_name": "values field for 'x'",
            "type": "input",
            "default": "x",
        },
        {
            "name": "encoding__x__type",
            "display_name": "'x' field type",
            "type": "select",
            "choices": [
                "quantitative",
                "ordinal",
                "nominal",
            ],
            "default": "quantitative",
        },
        {
            "name": "encoding__y__field",
            "display_name": "values field for 'y'",
            "type": "input",
            "default": "y",
        },
        {
            "name": "encoding__y__type",
            "display_name": "'y' field type",
            "type": "select",
            "choices": [
                "quantitative",
                "ordinal",
                "nominal",
            ],
            "default": "quantitative",
        },
        {
            "name": "encoding__x__bin__maxbins",
            "display_name": "max bins for 'x'",
            "type": "integer",
            "step": 5,
            "max": 300,
            "min": 5,
            "default": 40,
        },
        {
            "name": "encoding__y__bin__maxbins",
            "display_name": "max bins for 'y'",
            "type": "integer",
            "step": 5,
            "max": 300,
            "min": 5,
            "default": 40,
        },
    ],
    "frame_type": "500x500",  # landscap, portrait, square, 200x300
    "vl_schema": {
        "data": {"name": "data"},
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
                "bin": {"maxbins": 40},
                "field": "x",
                "type": "quantitative",
                "title": None,
            },
            "y": {
                "bin": {"maxbins": 40},
                "field": "y",
                "type": "quantitative",
                "title": None,
            },
            "color": {"aggregate": "count", "type": "quantitative"},
        },
        "config": {"view": {"stroke": "transparent"}},
    },
}


def histogram_heatmap_2d(
    x: Union[List, DataSeries, NDArray, DataRecords, DataFrame],
    y: Union[List, DataSeries, NDArray, DataRecords, DataFrame],
    options,
):
    pass
