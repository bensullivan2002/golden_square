import pytest
from lib.present import Present


@pytest.mark.parametrize("input, expected",
                        [
                            ("Gift", "A contents has already been wrapped."),
                            ("Rubbish gift", "A contents has already been wrapped.")
                        ]
                    )
def test_wrap(input, expected):
    present = Present()
    present.wrap(input)
    with pytest.raises(Exception) as e:
        present.wrap(input)
    error_message = str(e.value)
    assert error_message == expected


@pytest.mark.parametrize("expected",
                        [
                            ("No contents have been wrapped."),
                        ]
                    )
def test_unwrap(expected):
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == expected
