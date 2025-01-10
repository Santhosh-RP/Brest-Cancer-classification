import logging
import os

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging settings
LOG_FILE = os.path.join(LOG_DIR, "project.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def get_logger(module_name):
    """
    Returns a logger instance for the given module.

    Args:
        module_name (str): Name of the module for which the logger is created.

    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(module_name)

