# test_corepulse.py
"""
Tests for CorePulse module.
"""

import unittest
from corepulse import CorePulse

class TestCorePulse(unittest.TestCase):
    """Test cases for CorePulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CorePulse()
        self.assertIsInstance(instance, CorePulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CorePulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
