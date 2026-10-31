import sys
import logging

def error_message_detail(error:Exception, error_details: sys) -> str:
    """
    Extracts detailed error informatiom including name, line number and the error msg.

    :param error: The exception that occured.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error msg string.
    """
     # Extract traceback details (exception information)
    _,_, exc_tb = error_details.exc_info()

    # Get the file name where the exception occurred
    filename = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{filename}] at the line number [{line_number}]: {str(error)}"

    # Log the error for better tracking
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom excception class for handling errors in the US visa application
    """

    def __init__(self,error_message: str, error_detail: sys):
        """
        Initializes the USvisaExException with ta detailed error message

        :param error_message: A string describing the error
        :param error_detail: The sys module to access traceback details.
        """

        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message,error_detail)


    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message
