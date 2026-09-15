import pandas as pd
import pytest

@pytest.fixture
def valid_source():
    return pd.DataFrame(
        {
            "order_id": ["O0008"],
            "order_date": ["2026-01-13"],
            "customer_id": ["C025"],
            "region": ["East"],
            "product_category": ["Home"],
            "quantity": ["4.0"],
            "unit_price": ["599.0"],
            "discount": ["0.05"],
            "returned": ["false"],
        }
    )