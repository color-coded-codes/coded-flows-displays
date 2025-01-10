from typing import Union
from coded_flows.types import DataRecords, DataFrame


coded_flows_metadata = {
    "display_name": "Geo Map Display",
    "description": "Display a geo coordinates in a map.",
    "type": "map",
    "icon": "map-2",
    "frame_type": "600x600",  # landscape, portrait, square, 200x300
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
            "name": "popup_field",
            "display_name": "values field for pop-up",
            "type": "input",
            "default": "popup",
        },
        {
            "name": "color_field",
            "display_name": "values field for marker color",
            "type": "input",
            "default": "color",
        },
    ],
}


def map_display(
    data: Union[DataRecords, DataFrame], options
) -> Union[DataRecords, DataFrame]:
    return data
