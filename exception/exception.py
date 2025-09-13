import sys

class CustomException:
    def __init__(self,err_mess,error_detail:sys):
        self.err_mess = err_mess
        _,_,error_tb = error_detail.exc_info()
    
        self.line_no = error_tb.tb_lineno
        self.file_name = error_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        temp = "Error occure in python script: \n File Path : [{0}]\nLine No. : [{1}]\nError Message : [{2}]".format(self.file_name,self.line_no,str(self.err_mess))
        return temp
    