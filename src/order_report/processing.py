"""Funktioner som utför beräkningar"""

import pandas as pd

def calculate_order_value(data: pd.DataFrame) -> pd.DataFrame:
    """Beräknar ordervärde och rabattvärde"""

    data = data.copy()
    data["order_value"] = data["quantity"] * data["unit_price"]
    data["discounted_value"] = data["order_value"] * (1 - data["discount"])

    return data


def calculate_overview(data: pd.DataFrame) -> dict:
    """Beräknar övergripande nyckeltal"""

    return {
        "total_sales": round(data["discounted_value"].sum(), 2,),
        "order_count": data["order_id"].nunique(),
        "return_count": int(data["returned"].sum()),
    }


def aggregate_by(data: pd.DataFrame, group_column: str, sort_by: str = "total_sales") -> pd.DataFrame:
    """Grupperar försäljning och returer utifrån en viss kolumn"""

    result = data.groupby(group_column, as_index=False,).agg(
    order_count=("order_id", "nunique"),
    total_sales=("discounted_value", "sum"),
    returns=("returned", "sum"),
    )
    result["total_sales"] = result["total_sales"].round(2)
    result["return_rate"] = (result["returns"]  / result["order_count"]).round(3)

    return result.sort_values("total_sales", ascending=False,).reset_index(drop=True)