from __future__ import annotations

import logging
import os


_LOGGING_CONFIGURED = False


def configure_logging() -> None:
    global _LOGGING_CONFIGURED

    if _LOGGING_CONFIGURED:
        return

    log_level_name = os.getenv("FASTAPI_BOOKING_LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    _LOGGING_CONFIGURED = True
