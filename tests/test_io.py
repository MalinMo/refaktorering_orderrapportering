import pytest

from pathlib import Path
from order_report.io import load_orders


def test_load_orders_raises_filenotfounderror_for_missing_file():
    with pytest.raises(FileNotFoundError):
        load_orders(Path("data/does_not_exist.csv"))