import pytest
from lib.gratitudes import Gratitudes


@pytest.mark.parametrize("input, expected",
                        [
                            ("Python", "Be grateful for: Python"),
                            ("VS Code", "Be grateful for: VS Code"),
                        ]
                    )
def test_gratitudes(input, expected):
    gratitudes = Gratitudes()
    gratitudes.add(input)
    assert gratitudes.format() == expected
