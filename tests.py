import unittest
from unittest.mock import patch

def test_extra_feature():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        my_function()
        self.assertEqual(fake_out.getvalue().strip(), 'output value')
