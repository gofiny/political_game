import logging

import uvicorn

from api import config as app_config
from api.app import prepare_app

logger = logging.getLogger(__name__)


def run_app():
    logger.info("Start application")
    app = prepare_app()
    uvicorn.run(
        app, host=app_config.APP_HOST, port=app_config.APP_PORT, log_config=None
    )


if __name__ == "__main__":
    run_app()
