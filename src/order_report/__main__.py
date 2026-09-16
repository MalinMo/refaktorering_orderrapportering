"""Start av programmet"""
import logging

from order_report import ReportConfig, run_report
from order_report.logging_config import configure_logging, LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


def main() -> int:
    try:
        run_report(ReportConfig())
        return 0
    except (FileNotFoundError, ValueError) as error:
        logger.error("Kunde inte skapa rapporten: %s", error)
        return 1
    except Exception:
        logger.exception("Ett oväntat fel stoppade programmet")
        raise

if __name__ == "__main__":
    configure_logging()
    raise SystemExit(main())