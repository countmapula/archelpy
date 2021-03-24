import datetime

def time_message(message, arcpy): 
    """ A simple standard method for logging time stamped 
        messages in arcpy.

        Parameters
        ----------

        message: str 
            The message that you want to print. 
        
        arcpy: module
            Pass arcpy object as an argument.

    """
    time_now = "{0:%Y%m%d %H%M}".format(datetime.datetime.now())
    arcpy.AddMessage("{}: {}".format(time_now, message))