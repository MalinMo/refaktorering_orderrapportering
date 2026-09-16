import pandas as pd
import logging

from order_report.config import ReportConfig
from order_report.io import load_orders, save_report
from order_report.processing import calculate_order_value, calculate_overview, aggregate_by
from order_report.validation import validate_input, clean_data

logger = logging.getLogger(__name__)


def run_report(config: ReportConfig) -> dict[str, pd.DataFrame]:
    """Läser in, validerar, processar och sparar en orderrapport med fyra csv-filer"""

    data = load_orders(config.input_path)

    errors = validate_input(data)
    if errors:
        raise ValueError("Valideringen misslyckades: %s", "; ".join(errors))

    data = clean_data(data)
    data = calculate_order_value(data)

    overview = calculate_overview(data)
    overview_df = pd.DataFrame(
        {"metric": list(overview.keys()), "value": list(overview.values())}
    )

    sales_by_category = aggregate_by(data, "product_category")
    sales_by_region = aggregate_by(data, "region")
    returns_by_category = aggregate_by(data, "product_category", sort_by="return_rate")
    returns_by_category = returns_by_category.drop(columns="total_sales")                    # matchar originalets kolumner

    reports = {
        "overview": overview_df,
        "sales_by_category": sales_by_category,
        "sales_by_region": sales_by_region,
        "returns_by_category": returns_by_category,
    }
  
    save_report(overview_df, config.overview_path)
    save_report(sales_by_category, config.sales_by_category_path)
    save_report(sales_by_region, config.sales_by_region_path)
    save_report(returns_by_category, config.returns_by_category_path)

    logger.info("Orderrapporten är klar")

    return reports