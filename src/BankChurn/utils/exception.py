import sys
import os

# Add the parent directory of src to the Python module search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

# Now you can import the logger module
from src.BankChurn import logging


def get_error_message(error, error_details:sys) -> str:
    """
    Returns a formatted error message containing the file name, line number, and error message
    
    :param error: The error message
    :param error_details: The error details returned by the sys module
    :return: A formatted error message
    """
    _,_,exc_tb = error_details.exc_info()
      
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename, # file_name
        exc_tb.tb_lineno,                   # line_number
        str(error)          # Error message
    )
         
    # Configure logging to log the error message to a file
    logging.basicConfig(
        filename='error.log',  # Log file name
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        level=logging.ERROR  # Log level
    )
    
    # Log the error message
    logging.error(error_message)
         
    return error_message
 
class CustomException(Exception):
    """
    Custom exception class that formats and logs an error message
    """
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)   
        self.error_message = get_error_message(error_message, error_details=error_details) 
        
    def __str__(self) -> str:
        return self.error_message
    
    
    
if __name__ == "__main__":    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)
