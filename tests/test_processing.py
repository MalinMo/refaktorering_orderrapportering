import pandas as pd

from order_report.processing import calculate_order_value, calculate_overview, aggregate_by

def test_calculate_order_value():
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100.00],
            "discount": [0.1],

        }
    )

    result = calculate_order_value(data)

    assert result.loc[0, "order_value"] == 200.0
    assert result.loc[0, "discounted_value"] == 180.0


def test_calculate_overview():
    data = pd.DataFrame(
        {
            "discounted_value": [180.0, 20.0, 200.0],
            "order_id": ["00001", "00002", "00003"],
            "returned": [False, False, True],
        }
    )

    result = calculate_overview(data)

    assert result["total_sales"] == 400.0
    assert result["order_count"] == 3
    assert result["return_count"] == 1


def test_aggregate_by_calculates_totals_per_group():
    data = pd.DataFrame({
        "order_id": ["00001", "00002", "00003"],
        "product_category": ["Home", "Books", "Home"],
        "discounted_value": [180.0, 20.0, 200.0],
        "returned": [False, False, True],
    })

    result = aggregate_by(data, "product_category")

    home_row = result.loc[result["product_category"] == "Home"].iloc[0]
    assert home_row["order_count"] == 2
    assert home_row["total_sales"] == 380.0
    assert home_row["return_rate"] == 0.5