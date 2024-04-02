import pytest
from lib.string_builder import StringBuilder


@pytest.mark.parametrize("input, expected",
                        [
                            ("potato", "potato"),
                        ]
                    )
def test_string_builder_add_and_output(input, expected):
    string = StringBuilder()
    string.add(input)
    assert string.output() == expected


@pytest.mark.parametrize("input, expected",
                        [
                            ("potato", 6),
                        ]
                    )
def test_string_builder_add_and_size(input, expected):
    string = StringBuilder()
    string.add(input)
    assert string.size() == expected
