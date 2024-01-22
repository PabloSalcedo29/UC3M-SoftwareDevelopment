import unittest
from secure_all.storage.keys_json_store import KeysJsonStore
from secure_all.data.attribute_key import Key


class MyTestCase(unittest.TestCase):
    def test_singleton_keys_store(self):
        keys_json_1 = KeysJsonStore()
        keys_json_2 = KeysJsonStore()
        keys_json_3 = KeysJsonStore()
        keys_json_4 = KeysJsonStore()
        self.assertEqual(keys_json_1, keys_json_2)
        self.assertEqual(keys_json_2, keys_json_3)
        self.assertEqual(keys_json_3, keys_json_4)

        key_1 = Key("657244bdf89f067462e6a7f12b44749340f61030619f93bee391fbaf93361627").value
        key_2 = Key("657244bdf89f067462e6a7f12b44749340f61030619f93bee391fbaf93361627").value
        self.assertEqual(key_1, key_2)


if __name__ == '__main__':
    unittest.main()
