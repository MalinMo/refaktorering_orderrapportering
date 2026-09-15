import pandas as pd
import pytest

from order_report.validation import validate_input, clean_data

def test_validate_input_returns_no_errors_for_valid_data(valid_source):
    errors = validate_input(valid_source)
    assert errors == []


def test_validate_input_reports_missing_columns(valid_source):
    data = valid_source.drop(columns=["region"])
    errors = validate_input(data)
    assert any("region" in error for error in errors)


def test_validate_input_reports_empty_dataframe(valid_source):
    data = valid_source.iloc[0:0]
    errors = validate_input(data)
    assert any("inga rader" in error for error in errors)


@pytest.mark.parametrize(
    "column, raw_value, expected_value",
        [
            ("region", "east", "East"),
            ("product_category", "home", "Home")
        ],
)
def test_clean_data_title_case(valid_source, column, raw_value, expected_value):
    valid_source[column] = raw_value
    result = clean_data(valid_source)
    assert result.loc[0, column] == expected_value


@pytest.mark.parametrize(
    "column", ["region", "product_category"]
)
def test_clean_data_fills_str(valid_source, column):
    valid_source[column] = None
    result = clean_data(valid_source)
    assert result.loc[0, column] == "Unknown"

@pytest.mark.parametrize(
    "column, raw_value, expected_value",
        [
            ("quantity", "", 1),
            ("discount", "", 0.0)
        ],
)
def test_clean_data_fills_numeric(valid_source, column, raw_value, expected_value):
    valid_source[column] = raw_value
    result = clean_data(valid_source)
    assert result.loc[0, column] == expected_value


def test_clean_data_fills_invalid_unit_price_with_median_of_multiple_rows(valid_source):
    data = pd.concat([valid_source] * 3, ignore_index=True)
    data["unit_price"] = ["100.0", "200.0", "two"]
    result = clean_data(data)
    assert result.loc[2, "unit_price"] == 150.0

@pytest.mark.parametrize(
        "raw_value, expected_value",
        [
            ("true", True),
            (" True ", True),
            ("yes", True),
            ("Yes", True),
            ("1", True),
            ("ja", True),
            ("Ja", True),
            ("false", False),
            ( "False" , False),
            ("no", False),
            ("No", False),
            ("0", False),
            ("nej", False),
            ("Nej", False),
    ],
)
def test_clean_data_returned_column(valid_source, raw_value, expected_value):
    valid_source["returned"] = raw_value
    result = clean_data(valid_source)
    assert result.loc[0, "returned"] == expected_value


def test_clean_data_returned_column_fills_missing(valid_source):
    valid_source["returned"] = None
    result = clean_data(valid_source)
    assert result.loc[0, "returned"] == False

