from typing import Union
from coded_flows.types import List, DataSeries, NDArray, DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Line Chart Display",
    "description": "Display one line chart.",
    "type": "graph",
    "icon": "chart-line",
    "frame_type": "landscape",  # landscap, portrait, square, 200x300
    "options": [
        {
            "name": "encoding__y__field",
            "display_name": "values field for 'y'",
            "type": "input",
            "default": "y",
        }
    ],
    "vl_schema": {
        "data": {"name": "data"},
        "transform": [
            {"window": [{"op": "row_number", "as": "x"}]},
        ],
        "mark": {"type": "line", "color": ""},
        "encoding": {
            "x": {"field": "x", "type": "ordinal", "title": None},
            "y": {"field": "y", "type": "quantitative", "title": None},
        },
    },
}


def line_chart(y: Union[List, DataSeries, NDArray, DataRecords, DataFrame], options):
    pass
