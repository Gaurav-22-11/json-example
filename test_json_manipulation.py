import json_manipulation
import unittest

class TestJSONManipulation(unittest.TestCase):

    def test_read_json_file(self):
        data = json_manipulation.read_json_file("test_data.json")
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 3)

    def test_get_value_from_json(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        result = json_manipulation.get_value(data, 'key1')
        self.assertEqual(result, 'value1')

    def test_write_json_file(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        file_path = "output_data.json"
        json_manipulation.write_value(data, file_path)
        written_data = json_manipulation.read_json_file(file_path)
        self.assertEqual(data, written_data)

if __name__ == "__main__":
    unittest.main()
