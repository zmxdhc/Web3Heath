# test_web3heath.py
"""
Tests for Web3Heath module.
"""

import unittest
from web3heath import Web3Heath

class TestWeb3Heath(unittest.TestCase):
    """Test cases for Web3Heath class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Heath()
        self.assertIsInstance(instance, Web3Heath)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Heath()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
