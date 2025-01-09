from typing import Union
from coded_flows.types import List, DataSeries, NDArray, DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Table Display",
    "description": "Display Table",
    "type": "table",
    "icon": "table-filled",
    "options": [
        {
            "name": "page_size",
            "display_name": "Page size",
            "type": "integer",
            "step": 5,
            "max": 1000,
            "min": 10,
            "default": 10,
        },
    ],
    "frame_type": "portrait",  # landscape, portrait, square, 200x300
}


def table(
    data: Union[List, DataSeries, NDArray, DataRecords, DataFrame],
    options,
) -> Union[List, DataSeries, NDArray, DataRecords, DataFrame]:
    return data
