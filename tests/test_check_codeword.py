from lib.check_codeword import check_codeword
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("horse", "Correct! Come in."),
        ("house", "Close, but nope."),
        ("potato", "WRONG!"),
    ],
)
def test_check_codeword(input, expected):
    assert check_codeword(input) == expected
