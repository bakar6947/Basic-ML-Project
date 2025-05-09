import sys
from src.logger import logging



def error_message_detail(error, error_detail: sys):
    '''
    This function is used to get the error message details.
    '''
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name: [{file_name}] line number: [{line_number}] & error message [{error}]"
    return error_message
    

# Create Custom Exception Classes
class CustomException(Exception):
    
    def __init__(self, error_message, error_detail: sys):
        '''
        This function is used to initialize the custom exception class.
        '''
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
        
        
        
# Test Custom Exception and Logging
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)
