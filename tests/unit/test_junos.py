# Tests in this file corresponds to /jnpr/junos/__init__.py

import unittest
import sys

import pytest
from mock import patch

__author__ = "Nitin Kumar"
__credits__ = "Jeremy Schulman"


@pytest.mark.unit
class TestJunosInit(unittest.TestCase):
    def test_warning(self):
        with patch.object(sys.modules["sys"], "version_info", (2, 6, 3)) as mock_sys:
            from jnpr import junos

            self.assertEqual(mock_sys, (2, 6, 3))
