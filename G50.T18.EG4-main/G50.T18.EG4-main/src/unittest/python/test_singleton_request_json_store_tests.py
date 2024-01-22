import unittest
from secure_all.storage.request_json_store import RequestJsonStore
from secure_all.data.attribute_validate_code import ValidateCode


class MyTestCase(unittest.TestCase):
    def test_singleton_request_store(self):
        request_json_1 = RequestJsonStore()
        request_json_2 = RequestJsonStore()
        request_json_3 = RequestJsonStore()
        request_json_4 = RequestJsonStore()
        self.assertEqual(request_json_1, request_json_2)
        self.assertEqual(request_json_2, request_json_3)
        self.assertEqual(request_json_3, request_json_4)

        request_1 = ValidateCode("d2a7ca3223cd13b9a61f0e092aaaa140").value
        request_2 = ValidateCode("d2a7ca3223cd13b9a61f0e092aaaa140").value
        self.assertEqual(request_1, request_2)


if __name__ == '__main__':
    unittest.main()
