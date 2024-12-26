from typing import Union
from coded_flows.types import PILImage, NDArray, Bytes, BytesIOType


coded_flows_metadata = {
    "display_name": "Image Display",
    "description": "Image display",
    "type": "image",
    "icon": "photo-filled",
}


def image_display(image: Union[PILImage, NDArray, Bytes, BytesIOType]):
    pass
