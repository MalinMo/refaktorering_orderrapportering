import pytest

from pathlib import Path
from order_report.io import load_orders


def test_load_orders_raises_filenotfounderror_for_missing_file():
    with pytest.raises(FileNotFoundError):
        load_orders(Path("data/does_not_exist.csv"))


def test_load_orders_reads_valid_csv(tmp_path):
    csv_path = tmp_path / "orders.csv"
    csv_path.write_text("order_id,region\n1,East\n2,West\n")

    result = load_orders(csv_path)

    assert len(result) == 2
    assert list(result.columns) == ["order_id", "region"]