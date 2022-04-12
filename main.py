import logging

import uvicorn

from api import config as app_config
from api.app import prepare_app
from utils.logger import init_config

logger = logging.getLogger(__name__)


def run_app():
    app = prepare_app()
    uvicorn.run(
        app,
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        log_config=None,
        reload=False,
    )


if __name__ == "__main__":
    init_config()
    logger.info("test")
    run_app()
