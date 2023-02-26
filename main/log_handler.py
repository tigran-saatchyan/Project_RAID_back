"""Log handler module"""

import logging
import os

logging.basicConfig(
    filename=os.path.join('logs', 'main.log'),
    filemode='a',
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.DEBUG
)

# create logger for services application module
services_logger = logging.getLogger('services')
services_logger.setLevel(logging.INFO)

# create file handler and set level to debug
services_fh = logging.FileHandler(
    os.path.join('logs', 'services', 'services.log')
    )
services_fh.setLevel(logging.INFO)

# create formatter
services_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# add formatter to handler
services_fh.setFormatter(services_formatter)

# add handler to logger
services_logger.addHandler(services_fh)

# create logger for places module
dao_logger = logging.getLogger('dao')
dao_logger.setLevel(logging.INFO)

# create file handler and set level to debug
dao_fh = logging.FileHandler(os.path.join('logs', 'dao', 'dao.log'))
dao_fh.setLevel(logging.INFO)

# create formatter
dao_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# add formatter to handler
dao_fh.setFormatter(dao_formatter)

# add handler to logger
dao_logger.addHandler(dao_fh)

# create logger for places module
views_logger = logging.getLogger('views')
views_logger.setLevel(logging.INFO)

# create file handler and set level to debug
views_fh = logging.FileHandler(os.path.join('logs', 'views', 'views.log'))
views_fh.setLevel(logging.INFO)

# create formatter
views_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# add formatter to handler
views_fh.setFormatter(views_formatter)

# add handler to logger
views_logger.addHandler(views_fh)
