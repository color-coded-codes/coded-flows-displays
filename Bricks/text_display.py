from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Text Display",
    "description": "Displaying text, script or code.",
    "type": "text",
    "icon": "abc",
    "options": [
        {
            "name": "lang",
            "display_name": "select a language",
            "type": "select",
            "choices": [
                "apacheconf",
                "bash",
                "batch",
                "cmake",
                "docker",
                "excel",
                "git",
                "javascript",
                "jinja2",
                "json",
                "latex",
                "makefile",
                "markdown",
                "nginx",
                "powershell",
                "python",
                "regex",
                "sql",
                "text",
                "uri",
                "xml",
                "yaml",
            ],
            "default": "text",
        },
    ],
}


def text_display(text: Str, options) -> Str:
    return text
