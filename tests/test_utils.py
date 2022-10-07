"""Tests for utils module"""

from pprint import pformat

import re
from todi.utils import get_date


def _check_date_format(iso_date: str) -> bool:
    """
    Check if date has ISO format.
    :param iso_date: Date in ISO format.
    :return: Bool.
    """
    try:
        year, month, day = iso_date.split("-")
    except ValueError as error:
        print(pformat(error))
        return False
    return all(
        [
            int(day) in range(1, 31),
            int(month) in range(1, 12),
            int(year) >= 2022,
            len(year) == 4,
        ]
    )


def test_get_date() -> None:
    """
    Test get_date function from utils module.
    :return: None
    """
    tmp_date: str = get_date()
    assert _check_date_format(tmp_date)
    assert _check_date_format("20220-10-10") is False
    assert _check_date_format("202-10-10") is False
    assert _check_date_format("2022-13-10") is False
    assert _check_date_format("2022-10-32") is False
    assert _check_date_format("2022-00-10") is False
    assert _check_date_format("2022-10-00") is False
    assert _check_date_format("00-10-10") is False
    assert _check_date_format("2022-10") is False
    assert _check_date_format("2022") is False
    assert _check_date_format("2022-2-3-2-3") is False
