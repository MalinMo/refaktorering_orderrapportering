"""Funktioner som validerar och städar indata"""

import pandas as pd

REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
    }

def validate_input(data: pd.DataFrame) -> list[str]:
    """Validerar att indata har rätt kolumner och innehåller rader"""

    errors: list[str] = []

    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        errors.append("Saknade kolumner: " + ", ".join(sorted(missing_columns)))

    if data.empty:
        errors.append("Datafilen innehåller inga rader.")

    return errors

def _fill_and_title_case(data: pd.DataFrame, column: str, default: str) -> None:
    """Fyller saknade värden med standardvärden och trimmar text och sätter Title case"""
    data[column] = data[column].fillna(default).astype(str).str.strip().str.title()


def _fill_numeric(data: pd.DataFrame, column: str, default: float) -> None:
    """Konverterar en kolumn till numeriskt värde och fyller ogiltiga eller saknade värden"""
    data[column] = pd.to_numeric(data[column], errors="coerce").fillna(default)

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Städar och normaliserar rådata och returnerar en ny DataFrame"""

    data = data.copy()

    _fill_and_title_case(data, "region", default="Unknown")
    _fill_and_title_case(data, "product_category", default="Unknown")

    _fill_numeric(data, "quantity", default=1)
    _fill_numeric(data, "discount", default=0)

    data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce")
    data["unit_price"] = data["unit_price"].fillna(data["unit_price"].median())

    data["returned"] = (
        data["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    return data