"""
Safe utility functions — no vulnerabilities.
"""
import json
import re


def sanitize(text: str) -> str:
    """Remove dangerous characters from input."""
    return re.sub(r"[<>\'\"%;()&|`$]", "", text)


def format_greeting(name: str) -> str:
    """Safe greeting."""
    safe = sanitize(name)
    return f"Hello, {safe}!"


def parse_config(path: str) -> dict:
    """Read config file safely."""
    with open(path) as f:
        return json.load(f)
