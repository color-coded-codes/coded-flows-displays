from typing import Union
from coded_flows.types import DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Line Chart Display",
    "description": "Display one line chart.",
    "type": "map",
    "icon": "map-2",
    "frame_type": "500x500",  # landscape, portrait, square, 200x300
    "options": [
        {
            "name": "latitude_field",
            "display_name": "values field for latitude",
            "type": "input",
            "default": "lat",
        },
        {
            "name": "longitude_field",
            "display_name": "values field for longitude",
            "type": "input",
            "default": "lon",
        },
        {
            "name": "zoom",
            "display_name": "zoom level",
            "type": "integer",
            "step": 1,
            "max": 18,
            "min": 0,
            "default": 13,
        },
    ],
}


def map_display(
    data: Union[DataRecords, DataFrame], options
) -> Union[DataRecords, DataFrame]:
    return data
