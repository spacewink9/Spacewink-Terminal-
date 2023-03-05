import logging
import os

LOG_FILENAME = 'spacewink_terminal.log'
LOG_LEVEL = logging.DEBUG


def setup_logging():
    """Set up logging for the application"""
    # Check if log folder exists, and create it if it doesn't
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a log file with the given filename and set the logging level
    logging.basicConfig(filename=f'logs/{LOG_FILENAME}', level=LOG_LEVEL,
                        format='%(asctime)s %(levelname)-8s %(message)s')


def log_error(error_message):
    """Log an error message"""
    logging.error(error_message)


def log_info(info_message):
    """Log an informational message"""
    logging.info(info_message)
