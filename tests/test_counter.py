from lib.counter import Counter
import pytest


@pytest.mark.parametrize("input_num, expected",
        [
            (5, "Counted to 5 so far."),
        ]
    )
def test_counter(input_num, expected):
    counter = Counter()
    counter.add(input_num)
    assert counter.report() == expected
    