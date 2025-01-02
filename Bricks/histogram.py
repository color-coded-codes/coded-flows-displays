from typing import Union
from coded_flows.types import List, DataSeries, NDArray, DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Histogram Display",
    "description": "One dimensional histogram",
    "type": "graph",
    "icon": "chart-histogram",
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
            "name": "encoding__x__bin__maxbins",
            "display_name": "max bins for 'x'",
            "type": "integer",
            "step": 5,
            "max": 300,
            "min": 5,
            "default": 40,
        },
    ],
    "frame_type": "portrait",  # landscape, portrait, square, 200x300
    "vl_schema": {
        "data": {"name": "data"},
        "mark": "bar",
        "encoding": {
            "x": {
                "bin": {"maxbins": 40},
                "field": "x",
                "type": "quantitative",
                "title": "",
            },
            "y": {"aggregate": "count", "title": ""},
        },
    },
}


def histogram(
    x: Union[List, DataSeries, NDArray, DataRecords, DataFrame],
    options,
):
    pass
