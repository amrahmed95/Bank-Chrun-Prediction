import os
import sys
import logging

# Define the logging string format
logging_str = "[%(asctime)s: %(lineno)d - %(name)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory to store the log files
log_dir = "logs"

# Define the log file path
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
# Set the log level to INFO
# Set the log format
# Add a file handler to store logs in the log file
# Add a stream handler to display logs on the console
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Get the logger for the current module
# The logger is named "Bank Churn Project Logger"
logger = logging.getLogger("Bank Churn Project Logger")

# The logger is used throughout the project to log messages
