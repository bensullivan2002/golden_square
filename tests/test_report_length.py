import pytest
from lib.report_length import report_length

@pytest.mark.parametrize(
        "input, expected",
        [
            ("potato", "This string was 6 characters long."),
            ("antidisestablishmentarianism", "This string was 28 characters long.")
        ]
)
def test_report_length(input, expected):
    assert report_length(input) == expected
