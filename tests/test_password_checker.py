import pytest
from lib.password_checker import PasswordChecker


@pytest.mark.parametrize("input, expected",
    [
        ("01234", "Invalid password, must be 8+ characters.")
    ]
)
def test_password_checker_false(input, expected):
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check(input) == expected
    error_message = str(e.value)
    assert error_message == expected


@pytest.mark.parametrize("input, expected",
    [
        ("0123456789", True)
    ]
)
def test_password_checker_true(input, expected):
    password_checker = PasswordChecker()
    assert password_checker.check(input) == expected