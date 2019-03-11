# coding=utf-8

import os
import unittest


class TestBudd(unittest.TestCase):

    def setUp(self):
        os.environ['JSON_FOO'] = '{"foo": 100, "bar": "foo"}'
        os.environ['JSON_BAR'] = '3306'
        os.environ['JSON_FOO_BAR'] = '"root"'
        os.environ['RAW_FOO'] = 'utf8mb4'
        os.environ['RAW_BAR'] = '20'

    def test_budd(self):
        import budd.json.json as j
        import budd.raw.raw as r
        assert j["FOO"]["foo"] == 100
        assert j.FOO["foo"] == 100
        assert j["FOO"]["bar"] == "foo"
        assert j.FOO["bar"] == "foo"
        assert j["BAR"] == 3306
        assert j.BAR == 3306
        assert j["FOO_BAR"] == "root"
        assert j.FOO_BAR == "root"
        assert r["FOO"] == "utf8mb4"
        assert r.FOO == "utf8mb4"
        assert r["BAR"] == '20'
        assert r.BAR == "20"


if __name__ == "__main__":
    unittest.main()

