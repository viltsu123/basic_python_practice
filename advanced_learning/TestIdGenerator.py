'''
Test class for id generator
'''
import unittest
import re
import IdNumber

class TestIdGenerator(unittest.TestCase):

    def test_generate_id_should_generate_valid_id(self):
        id = IdNumber.generator()
        validhetu = r"^\d{6}[+-A]\d{3}[a-zA-Z0-9]$"
        match = re.search(validhetu, id)
        self.assertEqual(match.group(), id)

if __name__=='__main__':
    unittest.main()
