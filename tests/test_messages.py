#######################################################################
# Unit tests for archelpy.messages
#######################################################################

import unittest
from unittest.mock import Mock, patch

from archelpy.messages import time_message  # Our code

""" Mocks let us check that we're calling third-party libraries in the 
    way we expect, without actually invoking them.  

    This is particularly useful with arcpy which is huge and takes a 
    considerable time to load. 

    The Mock object will absorb any kind of interaction or input. 

    https://stackoverflow.com/a/63291174

"""
mock_arcpy = Mock()  # The real arcpy remains undisturbed


class HelpyMessagesTestCase(unittest.TestCase):
    """ Check that KF logic invokes arcpy with the correct parameters. 

        We're creating a class which inherits useful testing features 
        from unittest.TestCase. 

    """
    @patch("archelpy.messages.datetime")
    def testAddMessageParameters(self, patch_datetime):
        """ Uses assert_called_with() to make sure that our code passes 
            the right parameters to arcpy. 

            We're using a patch for the datetime module imported in 
            messages.py

        """
        # Mock the result of datetime.datetime.now() to a known value
        patch_datetime.datetime.now.return_value = datetime.datetime(
            2021, 3, 24, 9, 26, 00, 000000)
        # Test parameters
        timestamp = "20210324 0926"
        message = "Hello world!"
        expected = "{}: {}".format(timestamp, message) 
        # Invoke our function
        time_message(
            message,
            mock_arcpy # pass arcpy as an argument in mix-in style
        )

        """ Use the arcpy Mock object to validate that 
            AddMessage is called with the appropriate 
            parameters. 
        """
        mock_arcpy.AddMessage.assert_called_with(
            expected  # I.e. arcpy.AddMessage("20210324 0926: Hello world!")
        )

if __name__ == '__main__':
    unittest.main()
