import logging.config
import os

import yaml

from config import config as conf


def init_config():
    with open(os.path.normpath(conf.LOGGING_CONFIG), "r") as file:
        _config = yaml.load(file, Loader=yaml.FullLoader)
    logging.config.dictConfig(_config)
