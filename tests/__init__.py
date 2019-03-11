# coding=utf-8

import os
import unittest


class TestBudd(unittest.TestCase):

    def setUp(self):
        os.environ['J_FOO'] = '{"foo": 100, "bar": "foo"}'
        os.environ['J_BAR'] = '3306'
        os.environ['J_FOO_BAR'] = '"root"'
        os.environ['R_FOO'] = 'utf8mb4'
        os.environ['R_BAR'] = '20'

    def test_budd(self):
        import budd.json.j as j
        import budd.raw.r as r
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

