from src.expressions import contains, starts_with, format_message, to_json, from_json


def test_contains_finds_substring():
    assert contains("refs/heads/feature/login", "feature/")


def test_contains_rejects_missing_substring():
    assert not contains("refs/heads/main", "feature/")


def test_starts_with_matches_prefix():
    assert starts_with("refs/tags/v1.2.3", "refs/tags/")


def test_format_message_substitutes_placeholders():
    assert format_message("Hello, {0}! Build {1}.", "Karane", "42") == "Hello, Karane! Build 42."


def test_to_json_and_from_json_round_trip():
    payload = {"os": "ubuntu-latest", "run_number": 7}
    encoded = to_json(payload)
    assert from_json(encoded) == payload
