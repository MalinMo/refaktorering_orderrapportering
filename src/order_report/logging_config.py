"""Central konfiguration av paketets logging."""

import logging

LOGGER_NAME = "order_report"


def configure_logging() -> None:
    """Konfigurerar logging för order_report"""

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False