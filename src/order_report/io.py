import logging
import pandas as pd

from pathlib import Path

logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    """Läser in orderdata fån en csv-fil"""

    logger.info("Läser in data från %s", path)
    try:
        data = pd.read_csv(path)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Hittar inte datafilen: {path}") from error
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"Datafilen är tom: {path}") from error

    logger.info("Läste in %d rader", len(data))
    return data


def save_report(data: pd.DataFrame, path: Path) -> None:
    """Sparar en DataFrame som en csv-fil och skapar mappen om den saknas"""

    path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(path, index=False)
    logger.info("Sparade %s", path)