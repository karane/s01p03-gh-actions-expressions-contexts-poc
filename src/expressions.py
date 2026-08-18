import json


def contains(haystack: str, needle: str) -> bool:
    return needle in haystack


def starts_with(value: str, prefix: str) -> bool:
    return value.startswith(prefix)


def format_message(template: str, *args: str) -> str:
    for i, arg in enumerate(args):
        template = template.replace(f"{{{i}}}", arg)
    return template


def to_json(value: dict) -> str:
    return json.dumps(value)


def from_json(value: str) -> dict:
    return json.loads(value)
