import unittest

from knockDetection_functions import callback

class TestKnockDetection(unittest.TestCase):
    def test_area(self):
        # Ensure when channel 17 is set on RPI a knock is detected
        mockChannel = 17
        self.assertEqual(callback(mockChannel),mockChannel)
