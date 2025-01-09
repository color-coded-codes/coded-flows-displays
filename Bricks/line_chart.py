from typing import Union
from coded_flows.types import List, DataSeries, NDArray, DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Line Chart Display",
    "description": "Display one line chart.",
    "type": "graph",
    "icon": "chart-line",
    "frame_type": "landscape",  # landscape, portrait, square, 200x300
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
        "mark": {"type": "line", "color": "#4c78a8"},
        "encoding": {
            "x": {"field": "x", "type": "ordinal", "title": ""},
            "y": {"field": "y", "type": "quantitative", "title": ""},
        },
    },
}


def line_chart(
    y: Union[List, DataSeries, NDArray, DataRecords, DataFrame], options
) -> Union[List, DataSeries, NDArray, DataRecords, DataFrame]:
    return y
